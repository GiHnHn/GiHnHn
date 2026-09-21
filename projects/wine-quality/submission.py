#=============================
import tensorflow as tf
import random as rn
import numpy as np

seed_num = 1  # seed_num 값을 변경하지 말 것
np.random.seed(seed_num)
rn.seed(seed_num)
tf.random.set_seed(seed_num)
#=============================

import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import os

df = pd.read_csv('HW02_dataset.csv', sep=';')


corr_matrix = df.corr()


corr_with_quality = corr_matrix['quality'].drop('quality')


corr_sorted = corr_with_quality.abs().sort_values(ascending=False)

print("=== quality와 상관계수 절댓값 순서 ===")
print(corr_sorted)


from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder



X_all = df.drop(columns=['quality'])
y_all = df['quality']

le = LabelEncoder()
y_enc = le.fit_transform(y_all)

rf = RandomForestClassifier(n_estimators=200, random_state=1, n_jobs=-1)
rf.fit(X_all, y_enc)

feat_importances = pd.Series(rf.feature_importances_, index=X_all.columns)
feat_importances_sorted = feat_importances.sort_values(ascending=False)

print("=== RandomForest 기반 속성 중요도 순서 ===")
print(feat_importances_sorted)




selected_features = [
    'alcohol',
    'volatile acidity',
    'sulphates',
    'citric acid',
    'total sulfur dioxide',
    'density',
    'chlorides',
    'fixed acidity',
    'pH'
]
           

X = df[selected_features].values
Y = df['quality'].values

label_encoder = LabelEncoder()
Y_encoded = to_categorical(label_encoder.fit_transform(Y))

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y_encoded,
    test_size=0.15,
    shuffle=True,
    random_state=seed_num
)


model = Sequential()
model.add(Dense(64, input_dim=X.shape[1], activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.4))
model.add(Dense(32, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.3))
model.add(Dense(Y_encoded.shape[1], activation='softmax'))


model.compile(
    loss='categorical_crossentropy',
    optimizer='sgd',
    metrics=['accuracy']
)

MODEL_DIR = './model/'
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)

modelpath = os.path.join(MODEL_DIR, "{epoch:02d}-{val_accuracy:.5f}.keras")


history = model.fit(
    X_train, Y_train,
    validation_data=(X_test, Y_test),
    epochs=40,
    batch_size=10,
    verbose=1
)

test_loss, test_acc = model.evaluate(X_test, Y_test, verbose=0)
print(f"\n[Loss]: {test_loss:.4f}")
print(f"[Accuracy]: {test_acc:.4f}")

y_acc   = history.history['accuracy']
y_vacc  = history.history['val_accuracy']
y_loss  = history.history['loss']
y_vloss = history.history['val_loss']

epochs_range = np.arange(1, len(y_acc) + 1)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(epochs_range, y_acc,   marker='.', c='blue',  label='Train Acc')
plt.plot(epochs_range, y_vacc,  marker='.', c='red',   label='Val   Acc')
plt.title('Epoch vs. Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(epochs_range, y_loss,   marker='.', c='blue',  label='Train Loss')
plt.plot(epochs_range, y_vloss,  marker='.', c='red',   label='Val   Loss')
plt.title('Epoch vs. Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()


