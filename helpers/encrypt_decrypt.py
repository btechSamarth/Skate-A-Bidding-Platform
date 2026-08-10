
import bcrypt

def encrypt_password(password):
    encrypted_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return encrypted_password.decode()


def decrypt_password(password , hashed_pw):
    return bcrypt.checkpw(password.encode() , hashed_pw.encode())
