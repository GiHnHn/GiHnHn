"""Recipe taste regression, reorganized from the 2024 submitted model.
The model is unchanged; filename alignment, deterministic vocabulary and CLI were
added for the 2026 portfolio. This does not reproduce the historical metric.
"""
from pathlib import Path
import argparse
import csv
import json
import re

TASTES = ["Spicy_Score", "Sweet_Score", "Salty_Score", "Umami_Score"]

def load_rows(recipe_dir, score_file):
    """Join ingredient files to labels by filename, never by filesystem order."""
    rows = []
    with Path(score_file).open(encoding="utf-8-sig", newline="") as stream:
        labels = list(csv.DictReader(stream, delimiter="\t"))
    seen = set()
    for label in labels:
        name = label["Recipe"]
        if Path(name).name != name or name in seen:
            raise ValueError(f"Invalid or duplicate recipe filename: {name}")
        seen.add(name)
        file = Path(recipe_dir) / name
        ingredients = {}
        active = False
        for line in file.read_text(encoding="utf-8").splitlines():
            if line.startswith("== ["):
                active = line.strip() in ("== [재료] ==", "== [양념] ==")
                continue
            if not active:
                continue
            match = re.fullmatch(r"\s*(.+?):\s*(\d+(?:[.,]\d+)?)\s*g\s*", line)
            if match:
                ingredient, amount = match.groups()
                ingredients[ingredient] = ingredients.get(ingredient, 0) + float(amount.replace(",", "."))
        if not ingredients:
            raise ValueError(f"No gram-based ingredients in {name}")
        rows.append((name, ingredients, [float(label[t]) for t in TASTES]))
    if len(rows) < 5:
        raise ValueError("At least five labeled recipes are required.")
    return rows

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--recipes", required=True, type=Path)
    parser.add_argument("--scores", required=True, type=Path)
    parser.add_argument("--epochs", default=1000, type=int)
    parser.add_argument("--batch-size", default=32, type=int)
    parser.add_argument("--output", type=Path, default=Path("model"))
    parser.add_argument("--check-data", action="store_true")
    args = parser.parse_args()
    rows = load_rows(args.recipes, args.scores)
    if args.check_data:
        print(json.dumps({"matched_recipes":len(rows), "labels":"filename-aligned"}, ensure_ascii=False))
        return
    import numpy as np
    import tensorflow as tf
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error, mean_squared_error
    from tensorflow.keras import Sequential
    from tensorflow.keras.layers import Input, Dense, Dropout
    from tensorflow.keras.losses import Huber

    tf.keras.utils.set_random_seed(42)
    train_ids, val_ids = train_test_split(range(len(rows)), test_size=0.4, random_state=42)
    vocabulary = sorted({ingredient for i in train_ids for ingredient in rows[i][1]})
    def vectorize(indices):
        x = np.asarray([[rows[i][1].get(k, 0.0) for k in vocabulary] for i in indices], dtype="float32")
        y = np.asarray([rows[i][2] for i in indices], dtype="float32")
        return x, y
    x_train, y_train = vectorize(train_ids)
    x_val, y_val = vectorize(val_ids)
    model = Sequential([Input((len(vocabulary),)), Dense(256, activation="relu"),
                        Dropout(0.3), Dense(128, activation="relu"), Dropout(0.3),
                        Dense(64, activation="relu"), Dense(4, activation="linear")])
    model.compile(optimizer="adam", loss=Huber(), metrics=["mae"])
    model.fit(x_train, y_train, validation_data=(x_val, y_val),
              epochs=args.epochs, batch_size=args.batch_size, verbose=0)
    pred = model.predict(x_val, verbose=0)
    metrics = {"mae":float(mean_absolute_error(y_val,pred)),
               "rmse":float(np.sqrt(mean_squared_error(y_val,pred))),
               "train_rows":len(train_ids), "validation_rows":len(val_ids),
               "epochs":args.epochs, "note":"Validation against proxy labels; not a human taste test."}
    args.output.mkdir(parents=True, exist_ok=True)
    model.save(args.output/"model.keras")
    (args.output/"vocabulary.json").write_text(json.dumps(vocabulary,ensure_ascii=False),encoding="utf-8")
    (args.output/"metrics.json").write_text(json.dumps(metrics,indent=2),encoding="utf-8")
    print(json.dumps(metrics))
if __name__ == "__main__":
    main()

