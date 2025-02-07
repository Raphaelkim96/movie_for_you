import pandas as pd

df = pd.read_csv('./crawling_data/movie_400_20250204_combine.csv')
df.dropna(inplace=True)
df.info()
print(df.head())

# df_temp = pd.read_csv()
# df_temp = pd.read_csv(data_paths[0])
print(df.head())

titles = []
reviews = []
old_title = ''
for i in range(len(df)):

    title = df.iloc[i, 0]
    if title != old_title:
        title = title.replace('"','')
        titles.append(title)
        old_title = title
        df_movie = df[(df.Title == title)]
        review = ' '.join(df_movie.Review)
        reviews.append(review)


#print(titles[:5])
print(len(titles))
#print(reviews[1])

df = pd.DataFrame({'titles':titles, 'reviews':reviews})
df.info()
print(df)



df.to_csv('./crawling_data/reviews_kinolights_1.csv', index=False)