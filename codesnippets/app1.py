# import sqlite3
import sqlite3
# import flask
from flask import Flask, render_template, request
# import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# import date time
from datetime import datetime
# import automap_base
from sqlalchemy.ext.automap import automap_base

# create app
app = Flask(__name__)

# Here I create a DB and a connection
def create_connection(db_file):
    connection = None;
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn

# This is were I call the function for my db
create_connection("Value_connection.db") 

# This is were I create the tables I want in the database 
def create_table(conn, company_values):

    sql = """ INSERT INTO company_values(company_name, value1, value2, value3)
              VALUES(?,?,?,?) """ 

    c = conn.cursor()
    c.execute(sql,company_values)
    return cur.lastrowid    

# here I insert the created tables
def main():
    database = r"Value_connection.db"

    sql_create_company_table = """ CREATE TABLE IF NOT EXISTS guests (
                                        company_id integer not null PRIMARY KEY,
                                        company_name text NOT NULL,
                                        value1 text NOT NULL,
                                        value2 text NOT NULL,
                                        value3 date NOT NULL

                                    ); """

    conn = create_connection(database)

    if conn is not None:
        # make company_values table
        create_table(conn, sql_create_company_table)

    else:
        print("Error! cannot create the database connection.")

@app.route('/')
@app.route('/register')
def register():
    return render_template('register.html')

# sending input form form to db
@app.route('/values', methods=['POST'])
def values():

    if request.method == 'POST':
        c = conn.cursor()
        co_name = request.form.get('Companyname')
        val_1 = request.form.get('Value1')
        val_2 = request.form.get('Value2')
        val_3 = request.form.get('Value3')

        try:
            sql = ("INSERT INTO databasename.tablename (columnName,columnName,columnName,columnName Ci) VALUES (%s, %s, %s, %s)")
            c.execute(sql,(co_name, val_1, val_2, val_3 ))
            connection.commit() 
            #or "conn.commit()" (one of the two)
            return redirect('/')
        except:
            return 'something went wrong'