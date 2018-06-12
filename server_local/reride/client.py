import asyncio
import websockets

server = 'ws://grvmbp.local:8767'

async def hello():
    async with websockets.connect(
            server) as websocket:
        message = input("Enter payload: ")

        await websocket.send(message)
        print(f"> {message}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

async def _send_data(frame):
    async with websockets.connect(
        server) as websocket: 
        await websocket.send(str(frame))

def start():
    asyncio.get_event_loop().run_until_complete(hello())

def send_data(frame):
    asyncio.get_event_loop().run_until_complete(_send_data(frame))
