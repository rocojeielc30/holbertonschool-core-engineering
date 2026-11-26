#!/usr/bin/python3
import asyncio
import websockets

HOST = "localhost"
PORT = 8765
async def connection_handler(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with websockets.serve(connection_handler, HOST, PORT):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
