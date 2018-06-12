import asyncio
import websockets

server = 'ws://grvmbp.local:8766'

async def hello():
    async with websockets.connect(
            server) as websocket:
        message = input("Enter payload: ")

        await websocket.send(message)
        print(f"> {message}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

def start():
    asyncio.get_event_loop().run_until_complete(hello())
