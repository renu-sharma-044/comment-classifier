import pandas as pd
import joblib
from preprocess import preprocess

model = joblib.load("models/comment_classifier.joblib")

df = pd.read_csv("data/unlabeled_comments.csv")
df["clean"] = df["text"].apply(preprocess)
df["predicted_label"] = model.predict(df["clean"])

df.to_csv("data/categorized_comments.csv", index=False)

print("Done! Output saved to data/categorized_comments.csv")

