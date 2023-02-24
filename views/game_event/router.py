from fastapi import FastAPI, APIRouter, status
from views.game_event import views


def install(app: FastAPI):
    router = APIRouter(tags=["server.events"], prefix="/events")
    router.add_api_route(
        "/",
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        endpoint=views.get_events
    )
    app.include_router(router)