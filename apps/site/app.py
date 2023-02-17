from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from apps.site.settings import config

def create_app() -> FastAPI:
    from apps.site.views.main import router as main_router
    from apps.site.views.auth import router as auth_router
    from apps.site.views.profile import router as profile_router

    app = FastAPI()
    app.mount(
        config.STATICS_URLPATH,
        StaticFiles(directory=config.STATICS_FILEPATH),
        name="static"
    )

    main_router.install(app)
    auth_router.install(app)
    profile_router.install(app)

    return app

app = create_app()