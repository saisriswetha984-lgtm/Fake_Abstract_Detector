# ------------------------------
# Streamlit Fake vs Real Abstract Detector
# ------------------------------

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Title
st.title("Fake vs Real Abstract Detector")
st.write("Enter any abstract below and find out if it's REAL or FAKE.")

# Load dataset
df = pd.read_csv('data.csv')

# Split into features and labels
X = df['text']
y = df['label']

# Train-test split (we'll just train on all data for the demo)
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english', ngram_range=(1,2))
X_vec = vectorizer.fit_transform(X)
model = LogisticRegression()
model.fit(X_vec, y)

# Text input from user
abstract_input = st.text_area("Enter your abstract here:")

# Predict button
if st.button("Predict"):
    if abstract_input.strip() == "":
        st.warning("Please enter an abstract first!")
    else:
        vec = vectorizer.transform([abstract_input])
        pred = model.predict(vec)[0]
        label = "REAL" if pred == 0 else "FAKE"
        
        # Show colored output
        if label == "REAL":
            st.success(f"Prediction: {label}")
        else:
            st.error(f"Prediction: {label}")
