import asyncio
import websockets

test_server = 'ws://grvmbp.local:8765'
data_server = 'ws://grvmbp.local:8767'

TESTMODE = 0
DATAMODE = 1

async def echo_test():
    async with websockets.connect(
            test_server) as websocket:
        message = input("Enter payload: ")

        await websocket.send(message)
        print(f"> {message}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

async def _send_data(frame):
    async with websockets.connect(
        data_server) as websocket:
        await websocket.send(str(frame))

def send_data(mode,frame=''):
    if mode == TESTMODE:
        asyncio.get_event_loop().run_until_complete(echo_test())
    elif mode == DATAMODE:
        asyncio.get_event_loop().run_until_complete(_send_data(frame))
