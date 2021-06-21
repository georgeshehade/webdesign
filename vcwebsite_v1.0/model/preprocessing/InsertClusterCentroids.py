import sqlite3

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

centroids = [[-0.02052666, -0.06595708,  0.02392972],
            [ 0.06492347, -0.00064844, -0.02657856],
            [-0.0342036 ,  0.05239211, -0.05075364],
            [-0.1250352 , -0.0201957 ,  0.07142147],
            [-0.05051371,  0.02671735,  0.02023248]]

for centre in centroids:
    sqlquery = f'''INSERT INTO cluster_centroids (cluster1, cluster2, cluster3)
VALUES ({centre[0]}, {centre[1]}, {centre[2]});'''
    cur = conn.cursor()
    cur.execute(sqlquery)
    cur.close()

