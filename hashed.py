import bcrypt

# Replace 'admin_password' with your desired password
hashed_password = bcrypt.hashpw('admin_password'.encode(), bcrypt.gensalt())
print(hashed_password.decode())
