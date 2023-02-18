from fastapi import FastAPI, APIRouter, status
from apps.site.views.profile import handlers


def install(app: FastAPI):
    router = APIRouter(tags=["server.profile"], prefix="/profile")
    router.add_api_route(
        "/",
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        endpoint=handlers.get_profile
    )
    router.add_api_route(
        "/setting",
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        endpoint=handlers.update_profile
    )
    router.add_api_route(
        "/update_password",
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        endpoint=handlers.update_password
    )
    app.include_router(router)