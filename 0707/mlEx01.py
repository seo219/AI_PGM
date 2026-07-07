from sklearn.datasets import load_iris # 사이킷런에서 붓꽃 데이터셋 로드
import pandas as pd # 데이터 분석을 위한 pandas 라이브러리 임포트
from sklearn import svm # 사이킷런에서 SVM 모델 임포트
import plotly.express as px

iris = load_iris()
df = pd.DataFrame(iris.data) # 붓꽃 데이터셋의 feature 값을 DataFrame으로 변환
s = svm.SVC(gamma=0.1, C=10) # SVM 모델 생성
s.fit(iris.data, iris.target) # SVM 모델 학습

# 훈련 집합 # svm 분류 모델 SVC 객체 생성하고 
# iris 데이터로 학습 # 101번째와 51번째 샘플을 변형하고 새로운 데이터 생성
new_d = [[6.4, 3.2, 6.0, 2.5], [7.1, 3.1, 4.7, 1.35]]
# 데이터 집합
res = s.predict(new_d) # 새로운 데이터에 대한 예측 수행
print("새로운 2개 샘플의 부류는 ", res) # 예측 결과 출력

# print(iris.data) # 붓꽃 데이터셋의 feature 값 출력
# print(iris.target) # 붓꽃 데이터셋의 label 값 출력
# print(iris.feature_names) # 붓꽃 데이터셋의 feature 이름 출력
# print(iris.target_names) # 붓꽃 데이터셋의 label 이름 출력
# print(iris.DESCR) # 붓꽃 데이터셋의 상세 정보 출력

df = px.data.iris()
# petal_length를 제외하여 3차원 공간 구성
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width', color='species')
fig.show(renderer="browser")