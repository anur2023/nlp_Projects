import re
import emoji
import nltk
import spacy
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')

# Load Spacy model for lemmatization
nlp = spacy.load("en_core_web_sm")

def remove_html(text):
    return BeautifulSoup(text, "html.parser").get_text()

def remove_url(text):
    return re.sub(r"http\S+|www\S+|https\S+", "", text)

def remove_emoji(text):
    return emoji.replace_emoji(text, replace="")

def remove_punctuation(text):
    return re.sub(r"[^\w\s]", "", text)

def chat_conversion(text):
    # Example: Convert "u r awesome" → "you are awesome"
    conversions = {"u": "you", "r": "are", "b4": "before"}
    return " ".join([conversions.get(word, word) for word in text.split()])

def spelling_correct(text):
    return str(TextBlob(text).correct())

def remove_stopWords(text):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    return " ".join([word for word in words if word.lower() not in stop_words])

def lemmatization(text):
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc])

# Pipeline function
def process_text(text):
    pipeline = [
        remove_html,
        remove_url,
        remove_emoji,
        remove_punctuation,
        chat_conversion,
        spelling_correct,
        remove_stopWords,
        lemmatization,
    ]
    for function in pipeline:
        text = function(text)
    return text
