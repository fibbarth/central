#imports
from flask import Flask, request, render_template, g
import MySQLdb
import pprint

#application
app = Flask(__name__)
app.config.from_object('application.settings')

db = MySQLdb.connect(host='localhost', user="root",passwd="", db="central")
cur = db.cursor() 
cur.execute("SELECT * FROM User")
rows = cur.fetchall()

for row in rows:
    print row[1]

import application.views
