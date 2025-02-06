# nlp_Projects

# 📝 NLP Text Processing Web App (Django)  

This project is a **Django-based web application** that takes user input, processes it using **Natural Language Processing (NLP)** techniques, and returns the cleaned and transformed text. The goal is to demonstrate **text preprocessing** techniques used in various NLP tasks.  

---

## 🚀 Features  
✔ Remove HTML tags  
✔ Remove URLs  
✔ Remove Emojis  
✔ Remove Punctuation  
✔ Convert Chat Abbreviations (e.g., "u" → "you", "r" → "are")  
✔ Correct Spelling Errors  
✔ Remove Stop Words  
✔ Perform Lemmatization  

---

## 📌 Technologies Used  
- **Django** (Python Web Framework)  
- **NLTK** (Natural Language Toolkit)  
- **spaCy** (for Lemmatization)  
- **BeautifulSoup4** (for HTML removal)  
- **emoji** (for emoji removal)  
- **TextBlob** (for spell correction)  

---
Project Structure

nlp_project/
│── nlp_app/
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   ├── static/
│   ├── views.py
│   ├── urls.py
│   ├── nlp_utils.py  # NLP functions
│── nlp_project/
│── manage.py
│── requirements.txt
│── README.md

 NLP Pipeline
The text processing pipeline applies the following functions in order:
✅ 1. Remove HTML (using BeautifulSoup)
✅ 2. Remove URLs (using regex)
✅ 3. Remove Emojis (using emoji library)
✅ 4. Remove Punctuation (using regex)
✅ 5. Convert Chat Language (e.g., "u" → "you", "r" → "are")
✅ 6. Spell Correction (using TextBlob)
✅ 7. Remove Stop Words (using NLTK)
✅ 8. Lemmatization (using spaCy)

