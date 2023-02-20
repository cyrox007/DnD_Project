from fastapi import FastAPI, APIRouter, status
from views.profile import views


def install(app: FastAPI):
    router = APIRouter(tags=["server.profile"], prefix="/profile")
    router.add_api_route(
        "/",
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        endpoint=views.get_profile
    )
    router.add_api_route(
        "/setting",
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        endpoint=views.update_profile
    )
    router.add_api_route(
        "/update_password",
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        endpoint=views.update_password
    )
    router.add_api_route(
        "/update_avatar",
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        endpoint=views.update_avatar
    )
    app.include_router(router)