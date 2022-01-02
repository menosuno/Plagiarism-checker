from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from pprint import pprint
 
lemmatizer = WordNetLemmatizer()
text = "I have gone to the meet someone for the most important meeting of my life. I feel my best feelings right now."

def lemmetize_print(words):
     a = []
     tokens = word_tokenize(words)
     for token in tokens:
          lemmetized_word = lemmatizer.lemmatize(token)
          a.append(lemmetized_word)
     print(a)

lemmetize_print("hello worlds")