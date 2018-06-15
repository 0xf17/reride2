"""
.. module:: server_local/server.old
   : platform:
   : synopsis: tests websocket library and its functions to implement a local ws server

.. moduleauthor:: @grvashu

"""

import asyncio
import websockets
import datetime

server = 'grvmbp.local'

data = []
async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

async def getdata(websocket, path):
    buf = await websocket.recv()

    frame = buf.split()
    data.append(frame)

    for fragment in frame:
        print(fragment, end=' ')
    print('')

    await websocket.send(buf)

start_server = websockets.serve(getdata, server, 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
