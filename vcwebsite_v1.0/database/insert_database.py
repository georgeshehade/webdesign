import sqlite3


conn = sqlite3.connect('VC.db')

insert_data = """INSERT INTO survey_answers
                 VALUES ('D2O', 1234, 4, 3);"""  

# print(insert_data.format('DGO', '1234', 1, 3))
def insert(conn):
    c = conn.cursor()
    c.execute(insert_data)
    conn.commit()
    conn.close()

insert(conn)