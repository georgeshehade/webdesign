from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import json


# we read values from wordlist and we strip \n from it
with open('Value-Connection/source/vcwebsite_v1.1/vcwebsite/data/wordlist.txt', 'r') as f:
    values = f.readlines()

values = [x.rstrip('\n') for x in values]

tokenized_values = [word_tokenize(i) for i in values]
vectorized_words = Word2Vec(tokenized_values, min_count=1, vector_size=3, window=5)
word_dict = {}
for i in values:
    word_dict[i] = vectorized_words.wv.get_vector(i)

word_dict = {x: y.tolist() for x, y in word_dict.items()}

with open('Value-Connection/source/vcwebsite_v1.1/vcwebsite/data/vectorized_words.json', 'w') as f:
    json.dump(word_dict, f)
