import re

# Removing HTML Tags

def remove_html(text):
    pattern = re.compile('<.*?>') 
    return pattern.sub('', text)

Combined_text = """(<div
  <h2>Breaking News: AI is Everywhere!</h2>
  <p>Did you know that <b>AI</b> is now helping in <i>text processing</i>, <u>image recognition</u>, and even <span style="color: red;">self-driving cars</span>?</p>
  <p>Many companies use <a href=>OpenAI</a> for their AI solutions.</p>
  <ul>
    <li>Chatbots are becoming smarter!</li>
    <li>Speech recognition is improving.</li>
    <li>Data science is in high demand.</li>
  </ul>
  <p>Random text: $%^&*()_+ 12345 😊🚀 NLP is fun!</p>
)</div>
"""

Clean_text = remove_html(Combined_text)
# print("Cleaned text -: ",Clean_text)

# Remove URL's
def remove_url(text):
    pattern = re.compile(r'https?://\S+|www\.\S+')
    return pattern.sub('', text)

mixed_text = """
        Visit https://example.com for AI tools. Check http://randomsite.org for updates. Search anything on https://google.com and explore new trends online!
"""
cleaned_text = remove_url(mixed_text)
# print(cleaned_text)

# Removing Punctuation

import string, time
def remove_punctuation(text):
    exclude = string.punctuation 
    return text.translate(str.maketrans('', '', exclude))

mixed_text = """
            Wow! Can you believe it? AI, data science, and NLP—are evolving fast. Visit example.com now; don’t wait... The future is here: exciting, unpredictable, & innovative!
"""
cleaned_text = remove_punctuation(mixed_text)
# print("Cleaned text ",cleaned_text)

# Chat word treatment
chat_words = "my nskd odldnn gdewe ldspdd whwie sdp sd w ped "
def chat_conversion(text):
    new_text = []
    for w in text.split():
        if w.upper() in chat_words:
            new_text.append(chat_words(w.upper()))
        else:
            new_text.append(w)
    return " ".join(new_text)


# Spelling correction

from textblob import TextBlob


def spelling_correct(text):
    textBlb = TextBlob(text)
    correct_para = textBlb.correct().string
    print(correct_para)

incorrect_text = """
    Yesterday I gone to the market for buy some fruits and vegetables. The shopkeeper tell me that fresh apples is available, but I doesn't like the color of them. Then I seen a man who was sellinng mangoes, but it was too much costly. After that, I go to another shop where they have discount on bananas. I buyed some and come back to home happily. My mother say me that I should have also bring some tomatoes, but I forget
"""

# Removing stop words
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
list_of_words = stopwords.words('english')

def remove_stopWords(text):
    new_text = []
    for word in text.split():
        if word in list_of_words:
            new_text.append('') 
        else:
            new_text.append(word)
    return " ".join(new_text)


# Stemming
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer() 

def stem_words(text):
    return " ".join([ps.stem(word) for word in text.split()])



import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

def lemmatization(text):
    word_net_lemmatizer = WordNetLemmatizer()
    punctuations = "?:!.,;"
    
    # Tokenize text
    sentance_words = word_tokenize(text)
    
    # Remove punctuations
    sentance_words = [word for word in sentance_words if word not in punctuations]
    
    # Apply lemmatization
    lemmatized_words = [word_net_lemmatizer.lemmatize(word) for word in sentance_words]
    
    return " ".join(lemmatized_words)

# Example usage:
text = "The cats are running quickly! They were playing happily."
lemmatized_text = lemmatization(text)
print(lemmatized_text)  # Output: "The cat are running quickly They were playing happily"
