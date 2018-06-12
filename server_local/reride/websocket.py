import asyncio
import websockets
import datetime
import random
import time
import sys

TESTPORT  = '8765'

class WebSocketClient:

    def __init__(self, hostname):
        self.server = 'ws://' + hostname

    def test(self):
        server = self.server + ':' + TESTPORT

        async with websockets.connect(server)
        as websocket:
            payload = 'Hello Server'

            await websocket.send(payload)
            print(f"> {payload}")

            greeting = await websocket.recv()
            print(f"< {greeting}")

class WebSocketServer:
    def __init__(self, hostname):
        self.server = 'ws://' + hostname

    def start_test(self):
        start_server = websockets.serve(self.test, self.server, TESTPORT)

    async def test(self):
        server = self.server + ':' + TESTPORT

        async with websockets.connect(
                server) as websocket:
            payload = 'Hello Client'

            greeting = await websocket.recv()
            print(f"> {greeting}")

            await websocket.send(payload)
            print(f"< {payload}")

    def wait(self):
        try:
            asyncio.get_event_loop().run_until_complete(self.start_test)
            asyncio.get_event_loop().run_forever()
        except TypeError:
            print('Type Error')
            sys.exit()
