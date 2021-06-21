import sqlite3

# create connection to database
conn = sqlite3.connect('VC.db')

question_size = 2
survey_answer_table = """CREATE TABLE survey_answers
                         (comp_name, id, {})""".format(', '.join(["q"+ str(i) for i in range(question_size)]))

cluster_table = """CREATE TABLE cluster_table
                   (comp_name, cluster, value_rating_employee_management)"""

#discuss what info a company leaves behind
website_table= ""

def build(conn):
    c = conn.cursor()
    
    # create survey answer table (comp name, id , questions)
    c.execute(survey_answer_table)
    c.execute(cluster_table)
    # c.execute(website_table)
    conn.commit()
    conn.close()

build(conn)
