import nltk
# nltk.download('punkt')
import sqlite3
import gensim
from gensim.model import Word2vec
from nlt.tokenize import word_tokenize


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
for i in x:
    word = str(i)
    vectorword = vectorized_words[i]
    sqlquery = f''' INSERT INTO values_ (value_name, value_array)
                    VALUES({i}, {vectorword})'''
        cur = conn.cursor()
        cur.execute(sqlquery)
        conn.commit()