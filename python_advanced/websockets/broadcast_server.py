#!/usr/bin/env python3
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

HOST = "127.0.0.1"
PORT = 8765
PREFIX = "B:"


connected_clients = set()


def build_message(message):
    return f"{PREFIX}{message}"


async def send_to_client(client, message):
    try:
        await client.send(message)
    except ConnectionClosed:
        connected_clients.discard(client)


async def broadcast(message):
    active_clients = list(connected_clients)

    send_tasks = []
    for client in active_clients:
        send_tasks.append(send_to_client(client, message))

    await asyncio.gather(*send_tasks)


async def connection_handler(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await broadcast(build_message(message))
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    async with websockets.serve(connection_handler, HOST, PORT):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
