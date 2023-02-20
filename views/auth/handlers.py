import random
import string
from fastapi import Request

""" from apps.site.components.users.decorators import get_session """
from database import Database
from components.users.model import User


async def authorization(request: Request = None):
    db_session = Database.connect_database()
    data = await request.json()
    user_data = User.get_user(db_session, data["username"])
    if user_data is not None and data["password"] == user_data.password:
        return { 
            "status": "ok",
            "user_token": ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
            "username": user_data.username 
            }
    else:
        return { "status": "bed" }


async def registration(request: Request):
    db_session = Database.connect_database()
    data = await request.json()
    if User.get_user(db_session, data["username"]) is not None:
        return { "status": "bed" }

    if User.insert_new_user(db_session, data) == True:
        return { "status": "ok" }
    else:
        return { "status": "bed" }
