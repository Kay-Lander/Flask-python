from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, '')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def show():
    return render_template('success.html')

@app.route('/fail')
def wrong():
    return redirect('/')

app.run(debug=True)