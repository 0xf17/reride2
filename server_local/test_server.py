import reride.websocket as ws

server = ws.WebSocketServer('grvmbp.local')
server.start_test()
server.wait()
