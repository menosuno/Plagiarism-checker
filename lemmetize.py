from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from pprint import pprint
 
lemmatizer = WordNetLemmatizer()



# from nltk.stem import WordNetLemmatizer 
# lemmatizer = WordNetLemmatizer()

# def lemmatize(stem_words1, stem_words2):
#     l_words1 = ' '.join([lemmatizer.lemmatize(w) for w in stem_words1])
#     l_words2 = ' '.join([lemmatizer.lemmatize(w) for w in stem_words2])

#     return l_words1, l_words2

def lemmetize(words):
     a = []
     tokens = word_tokenize(words)
     for token in tokens:
          lemmetized_word = lemmatizer.lemmatize(token)
          a.append(lemmetized_word)
     return a
     
