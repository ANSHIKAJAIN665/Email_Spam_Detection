import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# ---------------- NLTK FIX ---------------- #
def download_nltk():
    try:
        nltk.data.find('tokenizers/punkt')
    except:
        nltk.download('punkt')

    try:
        nltk.data.find('tokenizers/punkt_tab')
    except:
        nltk.download('punkt_tab')

    try:
        nltk.data.find('corpora/stopwords')
    except:
        nltk.download('stopwords')

download_nltk()
# ------------------------------------------ #

ps = PorterStemmer()

def transform_text(message):
    message = message.lower()
    message = nltk.word_tokenize(message)

    y = []
    for i in message:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# UI
st.title("📧 Email Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button("Predict"):
    if input_sms.strip() == "":
        st.warning("Please enter a message")
    else:
        transformed_sms = transform_text(input_sms)
        vector_input = tfidf.transform([transformed_sms])
        result = model.predict(vector_input)[0]

        if result == 1:
            st.error("Spam")
        else:
            st.success("Not Spam")