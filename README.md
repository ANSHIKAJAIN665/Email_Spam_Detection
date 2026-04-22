# 🚀 Email Spam Classifier

🔗 **Live Demo:** https://emailspamdetection-qkpl9gg6nw3rqy2nxxwct9.streamlit.app/

---

## 📌 Overview

This is a Machine Learning-based Email Spam Classifier built using **Streamlit**.
It uses Natural Language Processing (NLP) techniques to preprocess text and classify messages as **Spam** or **Not Spam** in real time.

---

## ✨ Features

* 📩 Real-time spam detection
* 🧠 NLP preprocessing (tokenization, stopword removal, stemming)
* ⚡ Fast prediction using trained ML model
* 🌐 Interactive web interface with Streamlit

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn
* NLTK
* Machine Learning
* Natural Language Processing (NLP)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/email-spam-classifier.git
cd email-spam-classifier
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Download NLTK data

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### 4️⃣ Run the app

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
EMAIL_SPAM/
│── app.py
│── model.pkl
│── vectorizer.pkl
│── requirements.txt
│── README.md
```

---

## 🧪 How It Works

1. User inputs a message
2. Text is preprocessed using NLP techniques
3. TF-IDF vectorization is applied
4. Trained model predicts Spam or Not Spam

---

## 📈 Future Improvements

* Improve model accuracy
* Add more advanced NLP models (like BERT)
* Deploy with Docker
* Add user authentication

---

## 👩‍💻 Author

**Anshika Jain**

---
