import jwt

JWT_SECRET = 'anu'
JWT_ALGORITHM = 'UTF-8'

token_data = {
    'user_id':1337,
    'name':'Fakhrul Alamuddin Al Zulfi'
}

token = jwt.encode(token_data, JWT_SECRET)
print(token.decode('UTF-8'))