from fastapi import Request

from apps.site.components.users.decorators import get_session
from apps.site.components.users.model import User


@get_session
async def authorization(request: Request, db_session = None):
    data = await request.json()
    user_data = User.get_user(db_session, data["username"])
    if user_data.username is not None and data["password"] == user_data.password:
        return { "status": "ok" }
    else:
        return { "status": "bed" }

@get_session
async def registration(request: Request, db_session = None):
    data = await request.json()
    if User.insert_new_user(db_session, data) is not None:
        return { "status": "ok" }
    else:
        return { "status": "bed" }