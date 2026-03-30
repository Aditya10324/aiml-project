import subprocess
import sys

def silent_install(packages):
    for pkg in packages:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", pkg],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL)
        
silent_install(['pandas', 'scikit-learn'])

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movies.csv")

df['combined'] = df['title'] + " " + df['genre'] + " " + df['overview']

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined'])

similarity = cosine_similarity(tfidf_matrix)

def recommend(movie_name):
    movie_name = movie_name.lower()

    if movie_name not in df['title'].str.lower().values:
        print("Movie not found in database.")
        return

    idx = df[df['title'].str.lower() == movie_name].index[0]

    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:\n")

    count = 0
    for i in scores[1:]:
        if i[1] > 0.05:
            title = df.iloc[i[0]]['title']
            overview = df.iloc[i[0]]['overview']

            print(f"Movie: {title}")
            print(f"Overview: {overview}")
            print("-" * 50)

            count += 1
        if count == 5:
            break

movie = input("Enter a movie name: ")
recommend(movie)