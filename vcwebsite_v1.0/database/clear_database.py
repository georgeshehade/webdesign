import sqlite3
conn = sqlite3.connect("VC.db")

delete = "DELETE FROM {}"

def remove(conn):
    c = conn.cursor()
    c.execute(delete.format("survey_answers"))
    c.execute(delete.format("cluster_table"))
    conn.commit()
    conn.close()
    # c.execute(delete.format("website_table"))

remove(conn)