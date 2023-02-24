from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from settings import config

def create_app() -> FastAPI:
    from views.main import router as main_router
    from views.auth import router as auth_router
    from views.profile import router as profile_router
    from views.game_event import router as event_router

    app = FastAPI()
    app.mount(
        config.STATICS_URLPATH,
        StaticFiles(directory=config.STATICS_FILEPATH),
        name="static"
    )

    main_router.install(app)
    auth_router.install(app)
    profile_router.install(app)
    event_router.install(app)

    return app

app = create_app()