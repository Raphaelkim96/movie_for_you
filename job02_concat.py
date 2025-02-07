import pandas as pd
import glob


#data_paths = glob.glob('./crawling_data/movie_reviews_500_movies/*')
data_paths = glob.glob('./crawling_data/movie_400_20250204_combine.csv')
print(data_paths)

df = pd.DataFrame()

# 여러파일 하나로 concat
for path in data_paths:
    df_temp = pd.read_csv(path)
    # df_temp = pd.read_csv(data_paths[0])
    print(df_temp.head())

    titles = []
    reviews = []
    old_title = ''
    for i in range(len(df_temp)):

        title = df_temp.iloc[i, 0]
        if title != old_title:
            title = title.replace('"', '')
            titles.append(title)
            old_title = title
            df_movie = df_temp[(df_temp.Title == title)]
            review = ' '.join(df_movie.Review)
            reviews.append(review)


    #print(titles[:5])
    print(len(titles))
    #print(reviews[1])

    df_batch = pd.DataFrame({'titles':titles, 'reviews':reviews})
    # df_batch.info()
    print(df_batch)
    df = pd.concat([df, df_batch], ignore_index=True)

df.info()
df.to_csv('./crawling_data/reviews_kinolights.csv', index=False)