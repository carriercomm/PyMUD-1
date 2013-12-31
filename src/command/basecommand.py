'''
Created on Dec 22, 2013

@author: Justin
'''

from src.world import World


class NonStringOrListArgumentException(Exception): pass

class BaseCommand:

  def __init__(self):

    self.player = None
    self.target = None
    self.room = None
    self.args = None
    self.msg = {"player": ["\n"],
                "target": ["\n"],
                "room": ["\n"]}
    self.isinterface = False
    self.interface_border = "=" * 80

  def sendMsg(self, msg, hearers):

    if isinstance(msg, basestring):
      self.msg[hearers].append(msg)
    elif type([]) == type(msg):
      for i in msg:
        self.msg[hearers].append(i)
    else: raise NonStringOrListArgumentException

  def buildString(self):
    pass

  def action(self):
    pass

  def _final(self):

    if self.isinterface:
      self.msg["player"].insert(1, self.interface_border)
      self.msg["player"].append(self.interface_border)
    if self.player and len(self.msg["player"]) > 1:
      self.player.hear("\n".join(self.msg["player"]) + "\n")
    if self.target and len(self.msg["target"]) > 1:
      self.target.hear("\n".join(self.msg["target"]) + "\n")
    if self.room and len(self.msg["room"]) > 1:
      for i in self.room.contents:
        if i != self.player and i != self.target:
          if hasattr(i, "hear"):
            i.hear("\n".join(self.msg["room"]) + "\n")

  def executeCmd(self, player, args = None):

    self.player = player
    self.room = World.rooms.get(player.getStringLocation())
    self.cmd_entered = args[0]
    self.args = args[1:]

    self.buildString()
    self.action()
    self._final()
