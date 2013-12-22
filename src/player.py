'''
Created on Dec 22, 2013

@author: Justin
'''

import mobile

class Player(mobile.Mobile):
  
  def __init__(self, **kwargs):
    mobile.Mobile.__init__(self)

    self.connected = True
    self.conn = kwargs.get("conn")
    self.ip = kwargs.get("addr")

    self.hear("You are connecting from {}".format(self.ip[0]))

  def hear(self, msg):

    self.conn.send(msg + "\n")

  def recvCmds(self):
    
    while self.connected:
      cmd = self.conn.recv(2048)
      if cmd:
        self.hear("You just typed, {}".format(cmd))
