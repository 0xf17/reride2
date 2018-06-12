import asyncio
import websockets

server = 'grvmbp.local'
testport  = '8766'

async def hello(websocket, path):
    message = await websocket.recv()
    print(f"< {message}")

    greeting = f"Hello Client!"

    await websocket.send(greeting)
    print(f"> {greeting}")

def start():
    global start_server
    start_server = websockets.serve(hello, server, testport)

def wait():
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
