# Comment Categorization & Reply Assistant Tool

A machine‑learning powered tool that automatically classifies user comments (from social media, product posts, reviews, etc.) into categories such as Praise, Support, Constructive Criticism, Hate, Spam, Emotional, and Questions. The app also generates recommended reply templates for each category.

This project includes:

* Custom dataset (200+ comments)
* ML model training pipeline (TF‑IDF + Logistic Regression)
* Text preprocessing (cleaning + lemmatization)
* Streamlit web app for uploading CSV files
* Automatic replies
* Category distribution visualization

---

## 🚀 Features

### ✔ Comment Categorization

Automatically detects categories such as:

* Praise
* Support
* Constructive Criticism
* Hate / Abuse
* Threat
* Emotional
* Spam / Irrelevant
* Questions / Suggestions

### ✔ Smart Reply Templates

Each predicted category is mapped to a helpful response template.

### ✔ Streamlit Web App

* Upload CSV file
* Automatic preprocessing
* Category prediction
* Reply generation
* Preview table
* Bar‑chart visualization
* Download categorized CSV

### ✔ Clean Python Code (Modular)

Organized into:

```
src/
app/
data/
models/
venv/
```

---

## 📂 Project Structure

```
comment-classifier/
│
├── app/
│   └── streamlit_app.py
│
├── src/
│   ├── preprocess.py
│   ├── generate_dataset.py
│   ├── train.py
│   ├── inference.py
│   └── templates.json
│
├── data/
│   ├── labeled_comments.csv       (auto-generated)
│   └── categorized_comments.csv   (output)
│
├── models/
│   └── comment_classifier.joblib
│
└── venv/ (virtual environment)
```

---

## 🧠 Tech Stack

* **Python 3.13**
* **scikit‑learn** (ML model)
* **spaCy** (lemmatization)
* **NLTK** (optional)
* **Pandas**
* **Streamlit** (UI)
* **Joblib** (model saving)

---

## ⚙️ Installation

### 1️⃣ Clone or Download the Project

```
cd ~/comment-classifier
```

### 2️⃣ Create Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Requirements

```
pip install pandas scikit-learn nltk spacy joblib matplotlib seaborn streamlit
python -m spacy download en_core_web_sm
```

---

## 🏗 Dataset Creation

The dataset is automatically created using:

```
python src/generate_dataset.py
```

This generates:

```
data/labeled_comments.csv
```

---

## 🧪 Train the Model

Run:

```
python src/train.py
```

This saves the trained model:

```
models/comment_classifier.joblib
```

---

## ▶️ Run the Streamlit App

Start the web UI:

```
streamlit run app/streamlit_app.py
```

The app will open at:

```
http://localhost:8501
```

---

## 📤 How to Use the App

1. Prepare a CSV with a column named **text**.
2. Upload it in the app.
3. The app will:

   * preprocess text
   * categorize each comment
   * generate replies
   * show preview and distribution chart
4. Download the full categorized CSV.

Example CSV format:

```
text
Amazing work
Worst video ever.
I like the idea but execution is weak.
Follow me for free giveaways!!
```

---

## 📊 Sample Output (Preview)

| text                                   | clean                    | predicted_label | reply_template                                                             |
| -------------------------------------- | ------------------------ | --------------- | -------------------------------------------------------------------------- |
| Amazing work                           | amazing work             | praise          | Thank you so much! Your appreciation means a lot to our team.              |
| Worst video ever.                      | bad video                | hate            | We’re sorry you feel this way. Please share more details so we can assist. |
| I like the idea but execution is weak. | like idea execution weak | constructive    | Thanks for the feedback! We will surely work on improving this.            |

---

## 💡 Future Improvements

* BERT/Transformer-based classification
* User authentication
* Custom reply generation using LLMs
* Feedback-based model retraining
* Multi-language support

---

## 🏁 Conclusion

This tool helps companies and creators automatically organize audience feedback, saving time and enabling meaningful engagement.
It is production-ready, easy to extend, and simple to run.

If you want help adding features or deploying online, feel free to ask! 🚀
