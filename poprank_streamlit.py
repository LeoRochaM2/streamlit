import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


df_links = pd.read_csv(r'C:\Users\leoos\Desktop\visualStudio\.vscode\recommended_systems\links.csv')

df_movies = pd.read_csv(r'C:\Users\leoos\Desktop\visualStudio\.vscode\recommended_systems\movies.csv')

df_ratings = pd.read_csv(r'C:\Users\leoos\Desktop\visualStudio\.vscode\recommended_systems\ratings.csv')

df_tags = pd.read_csv(r'C:\Users\leoos\Desktop\visualStudio\.vscode\recommended_systems\tags.csv')

def best_movies(df_ratings, n):
    
    new_rat = df_ratings.groupby('movieId')['rating'].sum().sort_values(ascending=False)
    
    best_ranking = pd.merge(new_rat, df_movies, how="left", on=["movieId"])
    
    return best_ranking.head(n)

best_ranking = best_movies(df_ratings, 10)

best_ranking