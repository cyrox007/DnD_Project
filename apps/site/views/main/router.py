from fastapi import FastAPI, APIRouter, status
from apps.site.views.main import handlers


def install(app: FastAPI):
    router = APIRouter()
    router.add_api_route(
        '/',
        methods=['GET'],
        status_code=status.HTTP_200_OK,
        endpoint=handlers.main_page_dev
    )
    app.include_router(router)
