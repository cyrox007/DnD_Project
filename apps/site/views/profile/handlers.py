from fastapi import Request

from database import Database
from apps.site.components.users.model import User

async def get_profile(request: Request = None):
    response = await request.json()
    db_session = Database.connect_database()
    user_data = User.get_user(db_session, response["username"])
    return { 
        "status": "ok",
        "username": user_data.username,
        "email": user_data.email,
        "first_name": user_data.first_name,
        "surname": user_data.surname,
        "avatar": user_data.avatar
        }