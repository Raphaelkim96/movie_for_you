import pandas as pd
from konlpy.tag import Okt
import re

df = pd.read_csv('./crawling_data/reviews_kinolights_1.csv')
df.info()

df_stopwords = pd.read_csv('./crawling_data/stopwords.csv')
stopwords = list(df_stopwords['stopword'])


okt = Okt()
print(df.titles[0])
print(df.reviews[0])
cleaned_sentences = []
for review in df.reviews:
    #review = df.reviews[0]
    review = re.sub('[^가-힣]', ' ', review)
    #print(review)

    tokened_review = okt.pos(review , stem=True) #stem= True ㅣ 변형말고 웒형으로
    #print(tokened_review)
    # 의미있는 명사,동사,형용사만 사용하고 나머지 버림
    df_token = pd.DataFrame(tokened_review,columns=['word', 'class'])
    df_token = df_token[(df_token['class'] == 'Noun') |
                        (df_token['class'] == 'Verb') |
                        (df_token['class'] == 'Adjective')]
    #print(df_token)

    # 불용어 제거, 1개짜리 단어 제거
    words = []
    for word in df_token.word:
        if 1 < len(word):
            if word not in stopwords:
                words.append(word)
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)

df.reviews = cleaned_sentences
df.dropna(inplace=True)
df.info()
df.to_csv('./crawling_data/cleaned_reviews.csv', index=False)
