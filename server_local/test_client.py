import sys
sys.path.append("..")

from reride import client

#sample frame
frame = [1,2]

#send call
#modes: client.TESTMODE, client.DATAMODE
client.send_data(client.DATAMODE,frame
)
