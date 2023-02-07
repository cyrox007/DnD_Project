from fastapi import Request


async def authorization(request: Request):
    data = await request.json()

    if data["username"] == "admin" and data["password"] == "123456":
        return { "status": "ok" }
    else:
        return { "status": "bed" }

async def registration(request: Request):
    return { "status": "ok" }