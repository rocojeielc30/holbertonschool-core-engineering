#!/usr/bin/env python3
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute

HOME_HTML = "<h1>WebSocket Echo</h1>"


async def homepage(request):
    return HTMLResponse(HOME_HTML)


async def websocket_endpoint(websocket):
    await websocket.accept()
    async for message in websocket.iter_text():
        await websocket.send_text(message)


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
