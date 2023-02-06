from fastapi import FastAPI
from apps.site.views.main.router import main_router


app = FastAPI()
app.include_router(main_router)