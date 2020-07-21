from flask import Flask,render_template,redirect,request
from flask_mysqldb import MySQL
from cryptography.fernet import Fernet
import hashlib 
import json
#key for encryption
key = b'eRcQXxwSRi8lzzupwCPeD8iGo2t3e33l3usITnj3WNY='
app=Flask(__name__)
#intializing mysql database
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="workindia"
mysql=MySQL(app)
#To get the user data for registration
@app.route('/app/user',methods=['POST'])
def dbms():
	user=request.json
	username=user['username']
	password=user['password']
	cur=mysql.connection.cursor()
	#insert the username and password
	#password is inserted after converting into md5 hash for security purposes
	cur.execute("INSERT INTO users (username,password) VALUES (%s,%s)",(username,hashlib.md5(password.encode()).hexdigest()))
	mysql.connection.commit()
	cur.close()
	res={"status":"account created"}
	return json.dumps(res)
@app.route('/app/user/auth',methods=['POST'])
def auth():
	user=request.json
	username=user['username']
	password=user['password']
	cur=mysql.connection.cursor()
	#search for username and password from the users table
	users=cur.execute("SELECT * FROM users WHERE username=%s AND password=%s",(username,hashlib.md5(password.encode()).hexdigest()))
	userdetails=cur.fetchall()
	if users>0:
		print(userdetails)
		res={"status":"Success",
		"userid":userdetails[0][2]}
	else:
		res={"status":"Failure"}
	return json.dumps(res)
@app.route('/app/sites',methods=['POST'])
def save():
	u_id=request.args
	u_id=u_id.get('user')
	print(u_id)
	print(key)
	#intizalize the cipher key
	cipher_suite = Fernet(key)
	note=request.json
	print(note)
	#encrypt the data to store in database
	encoded_text = cipher_suite.encrypt(note['note'].encode())
	print(encoded_text)
	cur=mysql.connection.cursor()
	#search for user in users table 
	#if user is registered then save his notes
	#if user is not registered return as failure
	users=cur.execute("SELECT * FROM users WHERE id=%s",(u_id))
	if users>0:
		cur.execute("INSERT INTO notes (user_id,Notes) VALUES (%s,%s)",(u_id,encoded_text))
		mysql.connection.commit()
		cur.close()
		res={"status":"success"}
	else:
		res={"status":"Failure"}
	return json.dumps(res)
@app.route('/app/sites/list/',methods=['GET'])
def list():
	u_id=request.args
	u_id=u_id.get('user')
	print(u_id)
	print(key)
	cipher_suite = Fernet(key)
	note=request.json
	print(note)
	cur=mysql.connection.cursor()
	users=cur.execute("SELECT * FROM users WHERE id=%s",(u_id))
	#search for user in users table 
	#if user is registered return his saved notes
	#if user is not registered return as failure
	if users>0:
		notes=cur.execute("SELECT * FROM notes WHERE user_id=%s",(u_id))
		no=cur.fetchall()
		print(no)
	# decoded_text = cipher_suite.decrypt(encoded_text)
		a=[]
		# e=bytes(no[0][1].encode())
		# print(cipher_suite.decrypt(e))
		for i in no:
			print(i)
			a.append(cipher_suite.decrypt(bytes(i[1].encode())).decode("utf-8"))
		res=a
	else:
		res={"status":"Failure"}
	return json.dumps(res)
if __name__=="__main__":
	app.run(debug=True)