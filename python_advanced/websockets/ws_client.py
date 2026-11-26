#!/usr/bin/env python3
import asyncio
import websockets

SERVER = "ws://localhost:8765"
MESSAGE = "Hello WebSocket"


async def connect_send(uri: str, text: str) -> str:
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        return response


async def main():
    response = await connect_send(SERVER, MESSAGE)
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
