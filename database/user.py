import sqlite3

class UserStorage:
	def __init__(self):
		self.conn = sqlite3.connect("haverst_hope")
		cursor = self.conn.cursor()
		# Create table
		cursor.execute('''CREATE TABLE IF NOT EXISTS Users
             (uid integer primary key authincrement, email text, name text)''')
		cursor.close()

		self.conn.commit()

	'''
		create new user
		params:
			- email
			- password
			- name
	'''

	def create_user(self, email: str, password: str, name: str) -> str:
		# create new user

		try:
			cursor = self.conn.cursor()

			# insert user data into database
			cursor.execute("INSERT INTO Users (email, name, password) VALUES ({}, {}, {})".format(email, name,  password))
			
			self.conn.commit()
			# return on success
			return "user created successfully"
		except:

			# return on  failure
			return "user already created"

	'''
		create new user
		params:
			- email
		return:
			- email
			- name
			- password
	'''
	def	get_user(self, email):
		try:
			cursor  = self.conn.cursor()
			result = cursor.execute("SELECT uid email, name, password FROM Users WHERE email = {}".format(email))
			if result.arraysize == 0:
				return None
			
			row = result.fetchone()

			return row

			
		except:
			print("failed to fetch user")
			return None