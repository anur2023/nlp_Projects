import re
import string
import nltk
import emoji
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required NLTK data
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Initialize necessary components
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Define preprocessing functions

def remove_html(text):
    pattern = re.compile('<.*?>')
    return pattern.sub('', text)

def remove_emoji(text):
    return emoji.demojize(text)

def remove_url(text):
    pattern = re.compile(r'https?://\S+|www\.\S+')
    return pattern.sub('', text)

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Fix chat conversion function
chat_dict = {
    "u": "you", "r": "are", "b4": "before", "gr8": "great", "idk": "I don't know"
}

def chat_conversion(text):
    words = text.split()
    new_text = [chat_dict.get(w.lower(), w) for w in words]
    return " ".join(new_text)

def spelling_correct(text):
    text_blob = TextBlob(text)
    return text_blob.correct().string  # Fixed to return corrected text

def remove_stopWords(text):
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return " ".join(filtered_words)

def stem_words(text):
    return " ".join([ps.stem(word) for word in text.split()])

def lemmatization(text):
    words = word_tokenize(text)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words if word not in string.punctuation]
    return " ".join(lemmatized_words)

# Define the pipeline function
def preprocess_text(text, functions):
    for func in functions:
        text = func(text)
    return text