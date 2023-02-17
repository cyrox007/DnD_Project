from fastapi import Request

from database import Database
from apps.site.components.users.model import User

async def get_profile(request: Request = None):
    response = await request.json()
    db_session = Database.connect_database()
    user_data = User.get_user(db_session, response["username"])
    return { 
        "status": "ok",
        "user": user_data
        }