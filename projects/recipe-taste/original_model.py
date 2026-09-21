# 2024 submitted source, restored from HWP. Missing Dropout import repaired.
import os

import re

# 폴더 경로 설정

folder_path = './recipes_superfinal'

def parse_recipe(file_path):

    # 2차원 배열로 저장할 리스트

    ingredients_list = []

    amounts_list = []

    

    with open(file_path, 'r', encoding='utf-8') as f:

        lines = f.readlines()

    

    current_category = None  # '재료' or '양념'

    

    for line in lines:

        line = line.strip()

        

        if line.startswith('== [재료] =='):

            current_category = '재료'

        elif line.startswith('== [양념] =='):

            current_category = '양념'

        elif current_category:

            match = re.match(r"([가-힣]+): (\d+[\.,]?\d*)g", line)

            if match:

                ingredient = match.group(1)

                amount = float(match.group(2).replace(',', '.'))  # ','를 '.'으로 변환하여 실수로 처리

                

                if current_category == '재료':

                    ingredients_list.append(ingredient)

                    amounts_list.append(amount)

                elif current_category == '양념':

                    ingredients_list.append(ingredient)

                    amounts_list.append(amount)

    # 2차원 배열로 반환

    recipe_data = [{"ingredients": ingredients_list, "amounts": amounts_list}]

    

    return recipe_data

def process_recipes(folder_path):

    # 폴더 내 모든 텍스트 파일을 순회

    all_recipe_data = []

    

    for file_name in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file_name)

        if file_name.endswith('.txt') and os.path.isfile(file_path):

            # 텍스트 파일 처리

            recipe_data = parse_recipe(file_path)

            all_recipe_data.extend(recipe_data)

    

    return all_recipe_data

# 실행

recipes = process_recipes(folder_path)

print(recipes)

# 재료와 시즈닝 배열

ingredients = [

    "가지", "간마늘", "간장", "감자", "갓김치", "건고추", "고구마", "고사리", "고추", "굵은 소금",

    "김치", "김치 국물", "깨소금", "깻잎", "꽈리고추", "넙적당면", "느타리버섯", "다시마", "다시마물",

    "다진 마늘", "다진 생강", "단호박", "닭", "닭날개", "닭다리", "닭봉", "당근", "당면", "당면사리",

    "대추", "대파", "데친 쭈꾸미", "돼지 목살", "두부", "들깻순", "떡", "마늘", "만두", "맛술", "매운 건고추",

    "매운 고추", "맥주", "머쉬마루버섯", "멸치다시다", "무", "묵은갓김치", "묵은지", "물", "밤", "밤호박",

    "방울토마토", "배추김치", "버섯", "볶은깨", "비엔나소세지", "사과", "삶은 계란", "삼백초", "새송이버섯",

    "생강", "생강 가루", "생바질", "생밤", "설탕", "소곱창", "소금", "소주", "송이버섯", "순두부", "시래기",

    "식용유", "실파", "쌀뜨물", "쑥갓", "알감자", "애호박", "양배추", "양송이버섯", "양파", "연두부", "와인",

    "요리술", "우동사리", "우유", "월계수", "월계수잎", "은행", "인삼", "전복", "조랭이 떡", "쪽파", "참기름",

    "청고추", "청양고추", "청주", "초벌 묵은지", "총각김치", "치즈", "카레", "콩나물", "토란대", "토마토",

    "통깨", "통후추", "파", "파인애플", "파채", "파프리카", "팽이버섯", "페페론치노", "편생강", "포도씨유",

    "표고버섯", "풋고추", "피망", "피자치즈", "호박", "호박고구마", "호박고지", "홍감자", "홍고추", "홍초",

    "황태", "후추", "후추가루", "흑임자"

]

seasonings = [

    "가지효소", "간장", "강황가루", "건조 파세리", "게간장", "겨자", "고운 고추가루", "고추", "고추가루",

    "고추기름", "고추장", "고추장아찌간장", "국간장", "굴소스", "굵은 고추가루", "굵은소금", "김치 국물",

    "김치국물", "깔라만시원액", "깨", "깨소금", "꽃소금", "꿀", "다시다", "다시마물", "다진 마늘", "다진 생강",

    "다진 파", "대파", "된장", "두반장", "들기름", "레드와인", "레몬즙", "마늘", "마늘가루", "마늘장아찌 간장",

    "마스코바도", "맛간장", "맛소금", "맛술", "매실", "매실 고추장", "매실 액기스", "매실액", "매실원액",

    "매실청", "매운 고추가루", "맥주", "멸치 액젓", "멸치국물", "멸치액젓", "물", "물고추", "물엿", "미림",

    "미원", "밀가루", "배", "배즙", "버터", "복숭아즙", "볶은깨", "사이다", "사탕수수원당", "새우젓", "생강",

    "생강가루", "생강술", "생강즙", "생강청", "설탕", "소고기다시다", "소금", "소주", "술", "스터브소스",

    "식용유", "식초", "쌀뜨물", "쌈장", "알룰로스", "액젓", "양조간장", "양파", "양파액기스", "연두", "오미자청",

    "올리고당", "올리브유", "요리당", "요리술", "우유", "월계수잎", "전분가루", "정종", "조림간장", "조선간장",

    "조청", "진간장", "짜장가루", "참기름", "참깨", "참치액", "참치액젓", "천일염", "청고추", "청양고추", "청주",

    "춘장", "치즈", "치킨스톡", "카놀라유", "카레", "카레가루", "커피가루", "케첩", "콜라", "통깨", "통마늘",

    "통후추", "파", "파인애플쥬스", "파프리카가루", "편마늘", "포도주", "하이볼", "허브솔트", "홍고추", "황설탕",

    "후추", "후추가루", "흑설탕"

]

# ingredients와 seasonings를 합쳐서 중복 없이 새로운 배열 생성

ingre = list(set(ingredients + seasonings))

# 순서 부여하여 딕셔너리로 저장

ingredient_to_index = {ingredient: index for index, ingredient in enumerate(ingre)}

print(ingredient_to_index)

import pandas as pd

# 텍스트 파일 경로

file_path = "./flavor_scores.txt"

def parse_flavor_scores(file_path):

    # 파일 읽기

    with open(file_path, 'r', encoding='utf-8') as file:

        lines = file.readlines()

    # 데이터 추출

    data = []

    for line in lines[1:]:  # 첫 번째 줄은 헤더이므로 건너뜀

        parts = line.strip().split("\t")

        recipe_name = parts[0]

        scores = list(map(float, parts[1:]))  # Spicy, Sweet, Salty, Umami 점수를 float로 변환

        data.append(scores)

    return data

# 레시피 데이터를 2D 배열로 변환

y = parse_flavor_scores(file_path)

# 결과 출력

print(y)

import numpy as np

from tensorflow.keras.losses import Huber

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense, Input, Dropout

from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

# 고정 크기 벡터화

vectorized_recipes = np.zeros((len(recipes), len(ingredient_to_index)))

for i, recipe in enumerate(recipes):

    for ing, amt in zip(recipe["ingredients"], recipe["amounts"]):

        idx = ingredient_to_index[ing]

        vectorized_recipes[i, idx] = amt

# recipes: 입력 데이터, y: 출력 데이터

# 데이터를 훈련 데이터와 검증 데이터로 분리

X_train, X_val, y_train, y_val = train_test_split(

    vectorized_recipes, np.array(y), test_size=0.4, random_state=42

)

# Dense 네트워크 설계

def build_dense_model(input_size):

    model = Sequential()

    model.add(Input(shape=(input_size,)))

    model.add(Dense(256, activation='relu'))  # 첫 번째 은닉층 (ReLU 활성화 함수)

    model.add(Dropout(0.3))  # Dropout 추가하여 과적합 방지

    model.add(Dense(128, activation='relu'))  # 두 번째 은닉층

    model.add(Dropout(0.3)) 

    model.add(Dense(64, activation='relu'))   # 세 번째 은닉층

    model.add(Dense(4, activation='linear'))  # 출력층: 맵/단/짠/감의 점수 예측

    model.compile(optimizer='adam', loss=Huber(), metrics=['mae'])

    return model

dense_model = build_dense_model(len(ingredient_to_index))

dense_model.summary()

# 모델 학습

history = dense_model.fit(

    X_train, y_train, validation_data=(X_val, y_val), epochs=10000, batch_size=32

)

# 학습 결과 시각화

plt.plot(history.history['loss'], label='Training Loss')

plt.plot(history.history['val_loss'], label='Validation Loss')

plt.legend()

plt.xlabel('Epochs')

plt.ylabel('Loss')

plt.title('Training and Validation Loss')

plt.show()

# 테스트 데이터 예측

test_recipes = [

    {'ingredients': ['묵은지', '닭', '양파', '대파', '청고추', '홍고추', '감자', '고추장', '고추가루', '설탕', '간장', '참기름', '후추', '맛술'], 'amounts': [200.0, 1000.0, 160.0, 20.0, 30.0, 30.0, 560.0, 30.0, 30.0, 30.0, 30.0, 15.0, 1.0, 15.0]}

]

test_vectorized = np.zeros((len(test_recipes), len(ingredient_to_index)))

for i, recipe in enumerate(test_recipes):

    for ing, amt in zip(recipe["ingredients"], recipe["amounts"]):

        idx = ingredient_to_index[ing]

        test_vectorized[i, idx] = amt

# 예측

predictions = dense_model.predict(test_vectorized)

print("Predicted Scores (맵, 단, 짠, 감):", np.round(predictions, 2))

from sklearn.metrics import mean_absolute_error, mean_squared_error

import numpy as np

# 테스트 데이터

test_recipes = [

    {'ingredients': ['닭', '감자', '양파', '당근', '고추', '대파', '다진 마늘', '우유', '간장', '고추장', '고추가루', '요리당', '청주', '물', '후추', '참기름', '액젓'], 

     'amounts': [1000, 420, 320, 35, 30, 20, 20, 200, 150, 80, 10, 72, 15, 500, 2, 2, 15]},

    {'ingredients': ['닭', '당면', '대파', '양파', '설탕', '진간장', '굴소스', '미림', '물', '후추가루', '청양고추'], 'amounts': [800.0, 50.0, 100.0, 160.0, 45.0, 90.0, 15.0, 75.0, 200.0, 1.0, 10.0]},

    {'ingredients': ['닭', '감자', '꽈리고추', '대파', '편생강', '월계수잎', '생강술', '고추장', '고추가루', '맛간장', '설탕', '올리고당', '후추가루', '들기름'], 'amounts': [1000.0, 280.0, 150.0, 20.0, 15.0, 5.0, 125.0, 45.0, 30.0, 30.0, 30.0, 15.0, 2.0, 15.0]}

    

]

# 테스트 데이터의 실제 출력값 (예: 사람이 부여한 점수)

y_test = [

    [3.2, 3.8, 3.0, 3.6],

    [4.2, 4.6, 3.0, 5.0],

    [3.8, 3.9, 3.0, 4.8]# 테스트 데이터의 실제 점수

]

# 테스트 데이터를 벡터화

test_vectorized = np.zeros((len(test_recipes), len(ingredient_to_index)))

for i, recipe in enumerate(test_recipes):

    for ing, amt in zip(recipe["ingredients"], recipe["amounts"]):

        if ing in ingredient_to_index:

            idx = ingredient_to_index[ing]

            test_vectorized[i, idx] = amt

# 예측

predictions = dense_model.predict(test_vectorized)

# 예측 결과 출력

print("Predicted Scores (맵, 단, 짠, 감):", np.round(predictions, 2))

# 정확도 평가

mae = mean_absolute_error(y_test, predictions)

rmse = np.sqrt(mean_squared_error(y_test, predictions))

print("Mean Absolute Error (MAE):", np.round(mae, 2))

print("Root Mean Squared Error (RMSE):", np.round(rmse, 2))
