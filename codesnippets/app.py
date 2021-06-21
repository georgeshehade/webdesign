
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

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////C:/Users/GeorgeShehade/OneDrive - The Do Good Only Company BV/Documenten/Value-connection'

#db = SQLAlchemy(app)
conn = sqlite3.connect('Value_connection.db')
print ("Opened database successfully");

#craete cursor
cursor = conn.cursor()

# create first table company_values
comand1 = """ CREATE TABLE IF NOT EXISTS
company_values(company_id INTEGER not null  PRIMARY KEY, company_name TEXT , value1 TEXT, value2 TEXT, value3, TEXT)"""
cursor.execute(comand1)
print ("Table created successfully")
co_name = input('Company :')
val_1 = input('Value1:')
val_2 = input('Value2:')
val_3 = input('Value3:')
cursor.execute("""INSERT INTO company_values(company_name, value1, value2, value3) VALUES (?,?,?,?)""", (co_name, val_1,val_2,val_3))
conn.commit()
print(' Data entered successfully.')
conn.close()
if (conn):
	conn.close()
	print('\n sqlite connection closed.')

# set route
@app.route('/')
def index():
	return render_template("index.html")

#@app.route('/values')
#def values():
#	return render_template('.html')


# Create more pages
@app.route('/About')
def about():
	return render_template("about.html")




