import random
import string
from fastapi import Request

""" from components.users.decorators import get_session """
from database import Database
from components.users.model import User, UserVerification


async def authorization(request: Request = None):
    db_session = Database.connect_database()
    data = await request.json()
    user_data = User.get_user(db_session, data["username"])
    if user_data is not None and data["password"] == user_data.password and user_data.user_role > 100:
        db_session.close()
        return {
            "status": "ok",
            "user_token": ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
            "username": user_data.username
        }
    else:
        db_session.close()
        return {"status": "bed"}


async def registration(request: Request):
    db_session = Database.connect_database()
    data = await request.json()
    if User.get_user(db_session, data["username"]) is not None:
        db_session.close()
        return {"status": "bed"}

    if User.insert_new_user(db_session, data) == True and \
        UserVerification.create_verification_code(db_session, data) == True:
        db_session.close()
        return {"status": "ok"}
    else:
        db_session.close()
        return {"status": "bed"}
