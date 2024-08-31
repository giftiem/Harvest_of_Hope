from models.user import User
from database.user import UserStorage
from exceptions.auth_exceptions import InvalidPassword
from tokens.jwt import generateJWT

class AuthServices:
	def __init__(self):
		self.user_storage = UserStorage()
	
	def create_user(self, email: str, password: str, name:str):
		# TODO: hash password
		# TODO: check if user exists by email

		# create user
		return self.user_storage.create_user(email=email, password=password, name=name)



	def get_user(self, email: str, password: str) -> User:
		
		# TODO get user
		uid, found_email, name, found_password = self.user_storage.get_user(email = email)

		# validate user
		if not found_email == password:
			raise InvalidPassword("wrong email or password")
		

		# TODO: generate jwt
		jwtToken = generateJWT(uid=uid, email=email)

		
		# TODO: return user
		return User(email=email, name=name)
