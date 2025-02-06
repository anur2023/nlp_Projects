from Working_on_project.Text_Preprocessiong import *
from Working_on_project.Text_Pipiline import *



pipeline = [
    remove_html,
    remove_url,
    remove_emoji,
    remove_punctuation,
    chat_conversion,
    spelling_correct,
    remove_stopWords,
    lemmatization
]
text = """
        Hey! Check out my blog at <a href="https://myblog.com">myblog.com</a>. It's about #AI & machine learning! 😂 I’ve been working on an amazing prjct, but it’s hard 2 keep up with deadlines. Btw, u should totally join me, it will b gr8. Also, do u knw about the new research paper??!

"""
processed_text = preprocess_text(text, pipeline)
print("Processed text :- ",processed_text)