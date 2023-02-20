import uuid
import hashlib
 
def hash_password(password):
    # uuid используется для генерации случайного числа
    """ salt = uuid.uuid4().hex """
    return hashlib.sha256(password.encode()).hexdigest()
    
def check_password(hashed_password, user_password):
    """ password, salt = hashed_password.split(':') """
    return hashed_password == hashlib.sha256(user_password.encode()).hexdigest()