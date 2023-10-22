import bcrypt

def hash_password(password: str):
    salt = bcrypt.gensalt()  # Generate a random salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def verify_password(hashed_password: bytes, input_password: str):
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)