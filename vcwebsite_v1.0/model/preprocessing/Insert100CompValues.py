import random 
import sqlite3
import nltk
import numpy as np
import gensim
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize

random.seed(5)

#sql database connection 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)

    return conn

conn = create_connection("../value_connection.db")

# ######################################

x = ["Accepting", "Ambitious", "Authentic",
  "Brave", "Caring", "Challenging", "Cheerful",
  "Collaborative", "Communicator", "Creative", "Curious",
  "Decisive", "Dedicated", "Detailed", "Determined",
  "Enthusiastic", "Flexible", "Friendly", "Funny",
  "Hard-working", "Helpful", "Honest", "Integrity",
  "Kind", "Leader", "Logical", "Loyal",
  "Motivated", "Nurturing", "Open-minded", "Optimistic",
  "Persistent", "Practical", "Problem-solver", "Resilient",
  "Responsible", "Self-controlled", "Strong", "Supportive",
  "Team-player", "Trustworthy", "Versatile", "Well-organised"]
tokenized_values = [word_tokenize(i) for i in x]
vectorized_words = Word2Vec(tokenized_values, min_count=1, size=3, window=5)

def create_datapoint(comp_values):

  datapoint = []
  for value in comp_values:
    datapoint.append(list(vectorized_words[value]))

  return np.mean(datapoint, axis = 0)

def Insert100CompVal():
    for i in range(100):
        # random choice can take 1 value multiple times, with random sample select 1 value
        # sample_data = [random.sample(x), random.choice(x), random.choice(x)]
        sample_data = random.sample(x, 3)
        preprocessed_data = create_datapoint(sample_data)
        print(preprocessed_data)
        sqlquery = f''' INSERT INTO company_values(company_name, value1, value2, value3, TEXT)
                    VALUES(random, {preprocessed_data[0]}, {preprocessed_data[1]}, {preprocessed_data[2]})'''
        cur = conn.cursor()
        cur.execute(sqlquery)
        conn.commit()

Insert100CompVal()
