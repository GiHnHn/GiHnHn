# 한기헌 | 프로젝트 포트폴리오

LLM을 웹 서비스와 외부 도구에 연결하고, 제한된 데이터로 모델을 설계한 경험을 정리했습니다. 각 프로젝트에서 무엇을 구현했는지와 함께, 어떤 선택을 했고 무엇이 아직 한계인지 기록합니다.

[GitHub 프로필](https://github.com/GiHnHn) · [제출용 포트폴리오 PDF](https://github.com/GiHnHn/GiHnHn/blob/main/portfolio.pdf)

## 프로젝트

| 프로젝트 | 핵심 내용 | 기간 | 자료 |
|---|---|---|---|
| **장금이 — AI 요리 어시스턴트** | 텍스트·이미지 레시피 생성, 조리 중 대화와 음성 안내, n8n 도구 연동 | 2025.03–06 · 3인 팀 | [README · 코드](https://github.com/GiHnHn/GiHnHn/tree/main/projects/jang-geum-i) |
| **레시피 맛 척도 예측** | 재료를 g 단위로 통일하고 대리 정답을 설계한 4출력 회귀 모델 | 2024.2학기 · 개인 | [README · 코드](https://github.com/GiHnHn/GiHnHn/tree/main/projects/recipe-taste) |
| **와인 품질 분류** | 상관분석과 RandomForest 중요도를 비교한 변수 선택 및 신경망 실험 | 2025.1학기 · 개인 | [README · 코드](https://github.com/GiHnHn/GiHnHn/tree/main/projects/wine-quality) |

## 기술을 선택한 이유

- **장금이:** 자체 파인튜닝 모델의 응답 품질과 지연을 검토한 뒤, GPT API와 외부 도구를 연결하는 방향으로 전환했습니다.
- **맛 예측:** 충분한 사용자 평가가 없어 재료 기반 규칙과 댓글 분석을 이용한 대리 정답을 설계했습니다. 실제 관능평가와의 차이도 한계로 남겼습니다.
- **와인 분류:** 변수를 많이 넣는 것보다 입력 특성과 모델 크기를 비교하는 데 집중했습니다. 당시 검증 절차의 데이터 누출 가능성까지 함께 기록했습니다.

## 사용 기술

**AI·데이터:** LLM API, n8n, TensorFlow/Keras, scikit-learn, pandas, NumPy  
**웹:** React, Express, MongoDB, Firebase  
**연동:** 이미지 입력, 음성 합성, 쇼핑 검색 API, 자막 수집 노드

## 기록 기준

이 저장소는 대학 프로젝트의 선별본입니다. 팀 결과와 개인 프로젝트를 구분하고, 과거 보고서의 수치를 새로 재현한 결과처럼 제시하지 않습니다. 당시 코드와 2026년 정리 과정에서 수정한 부분은 [정리 기록](https://github.com/GiHnHn/GiHnHn/blob/main/docs/curation.md)에 구분했습니다.
