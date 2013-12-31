'''
Created on Dec 22, 2013

@author: Justin
'''

import mobile
import socket
import inspect
import command.forplayers as player_cmds
import random

class Player(mobile.Mobile):
  
  def __init__(self, server, **kwargs):
    mobile.Mobile.__init__(self)

    self.server = server
    self.name = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    self.connected = True
    self.conn = kwargs.get("conn")
    self.ip = kwargs.get("addr")
    self.cmd_list = self._loadAllCommands()
    
    self.location = self._getLocation()

  def hear(self, msg):

    self.conn.send(msg + "\n")

  def getStringLocation(self):
    
    return str(self.location)

  def _loadAllCommands(self):

    cmds = []
    for _, obj in inspect.getmembers(player_cmds):
      if inspect.isclass(obj) and obj.__doc__:
        cmds.append(obj)
    return cmds

  def _disambiguateCmd(self, typed, doc):
    
    if typed == doc: return True
    if len(typed) > len(doc): return False
    for idx in xrange(len(typed)):
      if typed[idx] != doc[idx]:
        return False
    return True

  def _parseCmd(self, cmd):

    typed_list = cmd.split()
    typed_list[0] = typed_list[0].lower()
    for obj in self.cmd_list:
      for doc in obj.__doc__.split():
        if self._disambiguateCmd(typed_list[0], doc):
          obj().executeCmd(self, typed_list)
          return

  def _getLocation(self):
    
    # Add location data loading here
    return (0,0,0)

  def save(self):
    
    if self.connected:
      self.hear("If there was anything to save, now would be the time...")

  def logout(self):
    
    self.hear("Thanks for playing!")
    self.conn.close()
    self.connected = False

  def _recvCmds(self):
    
    while self.connected:
      try:
        cmd = self.conn.recv(2048).strip()
        if cmd:
          self._parseCmd(cmd)
        else:
          self.hear("You gonna type something?")
      except socket.error, msg:
        print msg
        self.connected = False
        self.save()

  def handleLogin(self):
    
    self._recvCmds()
    
    
