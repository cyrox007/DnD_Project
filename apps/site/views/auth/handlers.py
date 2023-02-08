from fastapi import Request

""" from apps.site.components.users.decorators import get_session """
from database import Database
from apps.site.components.users.model import User


async def authorization(request: Request = None):
    db_session = Database.connect_database()
    data = await request.json()
    """ return { "data": data } """
    user_data = User.get_user(db_session, data["username"])
    if user_data is not None and data["password"] == user_data.password:
        return { "status": "ok" }
    else:
        return { "status": "bed" }


async def registration(request: Request):
    db_session = Database.connect_database()
    data = await request.json()
    if User.insert_new_user(db_session, data) is not None:
        return { "status": "ok" }
    else:
        return { "status": "bed" }