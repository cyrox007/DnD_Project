from fastapi import FastAPI, APIRouter, status
from apps.site.views.profile import handlers


def install(app: FastAPI):
    router = APIRouter(tags=["server.profile"], prefix="/profile")
    router.add_api_route(
        "/index",
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        endpoint=handlers.get_profile
    )