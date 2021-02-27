import os
from os import environ
from flask import Flask,render_template,url_for,flash,redirect,request,session
from flask_session.__init__ import Session
from flask_mysqldb import MySQL,MySQLdb
import MySQLdb.cursors
from flask import jsonify,json


app = Flask(__name__)
app.secret_key = 'your secret key'








app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'demo'

mysql = MySQL(app) 

@app.route("/",methods=['GET', 'POST'])
@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
	msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
		username = request.form['username']
		password = request.form['password']
        # Check if account exists using MySQL
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM account WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
		account = cursor.fetchone()
        # If account exists in accounts table in out database
		if account:
            # Create session data, we can access this data in other routes
			session['loggedin'] = True
			session['id'] = account['id']
			session['username'] = account['username']
            # Redirect to home page
			return redirect(url_for('home'))
		else:
            # Account doesnt exist or username/password incorrect
			msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
	return render_template('index.html', msg=msg)






@app.route("/home", methods=['GET', 'POST'])
def home():	
	
	
	return render_template('home.html')



	



@app.route("/logout",methods=['GET', 'POST'])  
def logout():  
	session.clear()
	return render_template('index.html') 























