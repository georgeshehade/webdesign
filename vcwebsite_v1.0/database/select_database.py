import sqlite3
conn = sqlite3.connect('VC.db')

select = "SELECT * FROM {}"

def select_all(conn):
    c = conn.cursor()
    c.execute(select.format("survey_answers"))
    print(c.fetchall())
    c.execute(select.format("cluster_table"))
    print(c.fetchall())
    conn.commit()
    conn.close()

select_all(conn)
