import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer #통계라이브러리
from scipy.io import mmwrite, mmread # 행렬저장하는 패키지
import pickle

df_reviews = pd.read_csv('./crawling_data/cleaned_reviews.csv')
df_reviews.info()

# 문서의 등장한 단어 역수를 취해서 행렬로 변환 벡터
Tfidf = TfidfVectorizer(sublinear_tf=True)
Tfidf_matrix = Tfidf.fit_transform(df_reviews.reviews)
print(Tfidf_matrix.shape)

# matrix 저장
with open('./models/tfidf.pickle', 'wb') as f:
    pickle.dump(Tfidf, f)

mmwrite('./models/Tfidf_movie_review.mtx', Tfidf_matrix)

