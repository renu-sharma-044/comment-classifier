import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib
from preprocess import preprocess

df = pd.read_csv("data/labeled_comments.csv")
df["clean"] = df["text"].apply(preprocess)

X = df["clean"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,2), max_features=20000)),
    ("clf", LogisticRegression(max_iter=1000))
])

print("Training model...")
model.fit(X_train, y_train)

print("Training complete!")
print("Saving model...")

import os
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/comment_classifier.joblib")

print("Model saved: models/comment_classifier.joblib")
