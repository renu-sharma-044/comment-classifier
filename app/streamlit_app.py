import streamlit as st
import sys
import os
import pandas as pd
import joblib
import json
sys.path.append(os.path.abspath("src"))
from preprocess import preprocess

st.set_page_config(page_title="Comment Categorizer", layout="wide")
st.title("📝 Comment Categorization & Reply Assistant Tool")

# Load model
model = joblib.load("models/comment_classifier.joblib")

# Load reply templates
with open("src/templates.json") as f:
    templates = json.load(f)

st.write("Upload a CSV file with a column named **text** to categorize comments.")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if "text" not in df.columns:
        st.error("CSV must contain a 'text' column.")
    else:
        st.success("File uploaded successfully!")

        # Convert all values to string to avoid float errors
        df["text"] = df["text"].astype(str)

        # Preprocess text
        df["clean"] = df["text"].apply(preprocess)

        # Predict categories
        df["predicted_label"] = model.predict(df["clean"])

        # Apply templates
        df["reply_template"] = df["predicted_label"].map(templates)

        # Show preview table
        st.write("### Preview:")
        st.dataframe(df.head(20))

        # Show chart
        st.write("### Category Distribution:")


        st.success("Processing complete!")
