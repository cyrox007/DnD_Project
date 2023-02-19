from fastapi import Request

from database import Database
from components.users.model import User
from components.image.handler import image_verification, decode_image, avatar_processing
from components.image.tasks import user_image_processing

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
    response = await request.json()
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
    response = await request.json()
    db_session = Database.connect_database()

    if User.update_user_password(db_session, response) == True:
        db_session.close()
        return { "status": "ok" }
    else:
        db_session.close()
        return { "status": "bed" }


async def update_avatar(request: Request):
    response = await request.json()
    db_session = Database.connect_database()
    
    filepath = decode_image(response["file"])
    avatar_path: dict = image_verification(filepath.split('.')[-2]) # генерируем пути для сохранения

    avatar_processing(filepath, avatar_path["for_save"])
    
    if User.avatar_update(db_session, response["user"], avatar_path["for_db"]) == True:
        db_session.close()
        return { 
            "status": "ok",
            "avatar": avatar_path["for_db"] 
            }
    else:
        db_session.close()
        return { "status": "bed" }