from fastapi import APIRouter, status
from apps.site.views.main import handlers


main_router = APIRouter(tags=['Payments'])
main_router.add_api_route(
    '/',
    methods=['GET'],
    status_code=status.HTTP_200_OK,
    endpoint=handlers.site_init
)
main_router.add_api_route(
    "/login",
    methods=["POST"],
    status_code=status.HTTP_200_OK,
    endpoint=handlers.login
)