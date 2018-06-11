import asyncio
import websockets
import datetime
import random
import time
server = 'ws://grvmbp.local:8765'

index = 0
async def hello():
    '''
    test function
    '''
    async with websockets.connect(
            'grvmbp.local:8765') as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

async def read_sensor():
    '''
    read sensor data
    '''
    current_time = datetime.datetime.now()
    frame = []
    frame.append(current_time)
    # frame.append(fsr1)
    # frame.append(fsr2)
    senddata(str(frame))

async def dummydata(size=2):
    global index
    async with websockets.connect(server) as websocket:
        # current_time = datetime.datetime.now()
        frame = []
        frame.append(index)
        frame.append(int(random.uniform(0,1023)))
        frame.append(int(random.uniform(0,1023)))

        await websocket.send(str(frame))
        print(f"> {frame}")

        ack = await websocket.recv()
        if ack == 'ACK':
            print("Received ACK from server")

        index = index + 1

for i in range(100):
    time.sleep(.500)
    asyncio.get_event_loop().run_until_complete(dummydata())
