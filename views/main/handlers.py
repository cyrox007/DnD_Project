from fastapi.responses import HTMLResponse
from fastapi import Request

from utils.j2 import render_template


async def main_page_dev(request: Request):
    return HTMLResponse(render_template(
        "main_page/index.html",
        {"request":request}
        ), 200)
