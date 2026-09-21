# 레시피 재료로 예측하는 네 가지 맛

**재료 종류와 양을 입력받아 매운맛·단맛·짠맛·감칠맛 점수를 예측한 개인 머신러닝 프로젝트입니다.**

2024.2학기 · 머신러닝 기말 프로젝트 · 개인  
Python · TensorFlow/Keras · pandas · NumPy · scikit-learn

## 문제와 접근

같은 닭볶음탕도 재료 비율에 따라 맛이 달라집니다. 이를 수치로 표현하기 위해 레시피를 수집하고, 재료 이름을 통일하고, 서로 다른 계량 단위를 g으로 환산했습니다.

보고서상 수집 규모는 **705건**입니다. 이번 정리 과정에서 최종 재료 파일과 점수표를 파일명으로 대조했을 때는 **449건**이 연결됐습니다. 수집 건수와 현재 확인 가능한 학습 입력 건수를 구분합니다.

## 정답이 부족할 때 내린 선택

사용자 댓글이 충분하지 않아, 댓글만으로 네 가지 맛의 정답을 만들기 어려웠습니다. 보고서에서는 재료별 맛 기여도를 정의한 규칙과 댓글 분석을 **8:2**로 결합하는 대리 정답 설계를 설명합니다.

이 점수는 사람이 실제로 맛보고 평가한 정답이 아닙니다. 따라서 모델의 오차는 **대리 정답을 얼마나 비슷하게 예측했는지**를 나타내며, 실제 맛 예측 정확도로 해석하지 않습니다.

## 모델

```text
재료 이름·g 단위 양 → 고정 길이 벡터
→ Dense(256) → Dropout(0.3)
→ Dense(128) → Dropout(0.3)
→ Dense(64) → Dense(4, linear)
```

Adam · Huber loss · MAE/RMSE 확인

MSE, MAE, Huber loss와 모델 크기 등을 비교했습니다. 최종 소스의 모델 구조를 기준으로 기록하고, 보고서의 배치 크기·학습 횟수와 소스가 다른 부분은 [실험 기록](EXPERIMENTS.md)에 구분했습니다.

## 파일 구성

- [original_model.py](original_model.py): 제출 HWP의 마지막 모델·검증 부분을 복원한 기록. 누락된 Dropout import만 보완했습니다.
- [train.py](train.py): 2026년 정리 시 재료 파일과 정답을 **파일명으로 연결**하도록 정리한 실행본. 모델 구조는 유지했습니다.
- [EXPERIMENTS.md](EXPERIMENTS.md): 당시 결과와 현재 확인 범위, 남은 한계.

원문 레시피·댓글·가중치 파일은 이 저장소에 포함하지 않습니다.

## 실행

```sh
pip install -r requirements.txt
python train.py --recipes data/recipes --scores data/flavor_scores.tsv --check-data
python train.py --recipes data/recipes --scores data/flavor_scores.tsv --epochs 1000 --batch-size 32
```

재료 파일은 `== [재료] ==` 또는 `== [양념] ==` 아래에 `양파: 160g` 형태로 기록합니다. 점수표는 탭 구분 파일이며 다음 열을 사용합니다.

```text
Recipe  Spicy_Score  Sweet_Score  Salty_Score  Umami_Score
```

`Recipe` 열에는 해당 재료 파일의 파일명을 넣습니다. 실행 후 모델, 재료 사전, 검증 지표가 `model/`에 저장됩니다.

## 남은 과제

조리 순서·시간·온도와 사람의 관능평가를 입력·정답에 반영해야 범용성을 검증할 수 있습니다. 드물게 쓰이는 재료와 비정상적인 레시피에 대한 성능도 별도 확인이 필요합니다.
