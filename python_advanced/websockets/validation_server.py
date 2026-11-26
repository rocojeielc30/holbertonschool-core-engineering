#!/usr/bin/env python3 
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

HOST = "127.0.0.1"
PORT = 8765
ERROR = "ERR: EMPTY"


def is_empty(message):
    return len(message.strip()) == 0


def build_response(message):
    if is_empty(message):
        return ERROR
    return f"OK: {message}"


async def connection_handler(websocket):
    try:
        async for message in websocket:
            response = build_response(message)
            await websocket.send(response)
    except ConnectionClosed:
        pass


async def main():
    async with websockets.serve(connection_handler, HOST, PORT):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())