# 🧠 Fake vs Real Abstract Detector

A machine learning-based web application that classifies research abstracts as **REAL** or **FAKE** using Natural Language Processing (NLP) techniques.

---

## 🚀 Live Demo

https://fakeabstractdetector-efu2w4fe9nkz3vnpk3fo7n.streamlit.app/

---

## 📌 Features

* 📝 Classifies research abstracts as REAL or FAKE
* 🤖 Uses Machine Learning (Logistic Regression)
* 🧠 NLP-based text processing with TF-IDF
* ⚡ Fast and interactive UI built with Streamlit
* 🎨 Color-coded output for better user experience
* 📊 Works on custom labeled dataset

---

## 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit
* TF-IDF Vectorizer (NLP)

---

## 📊 How It Works

1. Dataset containing abstracts is collected and labeled  
2. Text data is cleaned and preprocessed  
3. TF-IDF Vectorizer converts text into numerical features  
4. Logistic Regression model is trained on the dataset  
5. User input is vectorized and passed to the trained model  
6. The model predicts whether the abstract is REAL or FAKE  
7. Result is displayed with visual feedback  

---
## 📂 Project Structure
Fake_Abstract_Detector/
│
├── app.py
├── data.csv
├── requirements.txt
└── README.md

---

## ⚙️ Installation & Setup

1. Clone the repository
2. Navigate to the project folder
3. cd fake-abstract-detector
4. Install dependencies
pip install -r requirements.txt
5. Run the app
streamlit run app.py


---

## 🧪 Dataset

* Custom dataset of research abstracts
* Labels:
  * `0` → REAL
  * `1` → FAKE

---

## 📸 Sample Output




---

## 🎯 Future Improvements

* Use advanced models like **LSTM / BERT**
* Improve dataset size and diversity  
* Add prediction confidence score  
* Deploy with cloud scalability  
* Add support for multiple domains  

---

## 💡 Acknowledgements

* Scikit-learn for machine learning tools  
* Streamlit for building the web interface  

---

## 📬 Contact

Feel free to connect for feedback, suggestions, or collaboration!


## 📂 Project Structure
