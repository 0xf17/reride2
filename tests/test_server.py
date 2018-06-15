"""
.. module:: test/test_server
   : platform:
   : synopsis: test and enlists all the functions of the reride/server library

.. moduleauthor:: @grvashu, @anchitsh96

"""

import sys
sys.path.append("..")

from reride import server

server.start()
server.wait()
