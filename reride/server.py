import asyncio
import websockets

server = 'grvmbp.local'
testport  = '8765'
dataport = '8766'


TESTMODE = 0
DATAMODE = 1

async def echo_test(websocket, path):
    '''
    This function echoes client message over websocket connection.
    DO NOT CALL THIS FUNCTION. This function will be called back automatically.
    '''
    message = await websocket.recv()
    print(f"< {message}")

    greeting = f"Hello Client!"

    '''
    send message back to the Client
    '''

    await websocket.send(greeting)
    print(f"> {greeting}")

async def receive_data(websocket, path):
    frame = await websocket.recv()
    print(f"< {frame}")

def start(mode = TESTMODE):
    global start_server
    if mode == TESTMODE:
        start_server = websockets.serve(echo_test, server, testport)
    elif mode == DATAMODE:
        start_server = websockets.serve(receive_data, server, dataport)

def wait():
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
