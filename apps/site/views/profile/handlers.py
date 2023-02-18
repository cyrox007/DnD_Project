from fastapi import Request

from database import Database
from apps.site.components.users.model import User

async def get_profile(request: Request):
    response = await request.json()
    db_session = Database.connect_database()
    user_data = User.get_user(db_session, response["username"])
    
    db_session.close()
    return { 
        "status": "ok",
        "username": user_data.username,
        "email": user_data.email,
        "first_name": user_data.first_name,
        "surname": user_data.surname,
        "avatar": user_data.avatar
        }

async def update_profile(request: Request):
    response = request.json()
    db_session = Database.connect_database()

    if User.update_profile(db_session, response) == True:
        db_session.close()
        return {
            "status": "ok"
        }
    else:
        db_session.close()
        return {
            "status": "bed"
        }

async def update_password(request: Request):
    response = request.json()
    db_session = Database.connect_database()

    if User.update_user_password(db_session, response) == True:
        db_session.close()
        return { "status": "ok" }
    else:
        db_session.close()
        return { "status": "bed" }