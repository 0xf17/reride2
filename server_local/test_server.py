import sys
sys.path.append("..")

from reride import server

#sample server
#modes: server.TESTMODE, server.DATAMODE
server.start(server.TESTMODE)

server.wait()
