from fastapi import FastAPI, APIRouter, status
from apps.site.views.auth import handlers


def install(app: FastAPI):
    router = APIRouter(tags=['server.auth'], prefix="/auth")
    router.add_api_route(
        "/login",
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        endpoint=handlers.authorization
    )
    app.include_router(router)
    