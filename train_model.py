import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import joblib

def train():
    # Sample dataset
    data = {
        "text": [
            "NASA has discovered water on the moon",
            "Breaking: Actor spotted partying with aliens",
            "COVID-19 vaccine proves effective in latest trials",
            "Scientists prove Earth is flat in new study",
            "Government launches new scheme for farmers",
            "Aliens have landed in New York City",
        ],
        "label": ["REAL", "FAKE", "REAL", "FAKE", "REAL", "FAKE"]
    }

    df = pd.DataFrame(data)
    X = df["text"]
    y = df["label"]

    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
    X_vec = vectorizer.fit_transform(X)

    model = PassiveAggressiveClassifier(max_iter=1000)
    model.fit(X_vec, y)

    joblib.dump(model, "saved_model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")

    print("✅ Model trained and saved!")

# 🔥🔥🔥 THIS PART IS CRUCIAL 🔥🔥🔥
if __name__ == "__main__":
    train()
