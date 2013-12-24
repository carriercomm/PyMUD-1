'''
Created on Dec 22, 2013

@author: Justin
'''

class NonStringArgumentException(Exception): pass

class BaseCommand:

  def __init__(self):

    self.player = None
    self.target = None
    self.args = None
    self.msg = {"self": [],
                "target": [],
                "room": []}
    self.isinterface = False
    self.interface_border = "=" * 80

  def playerHear(self, msg):

    if isinstance(msg, basestring):
      self.msg["self"].append(msg)
    else: raise NonStringArgumentException

  def targetHear(self, msg):

    if isinstance(msg, basestring):
      self.msg["target"].append(msg)
    else: raise NonStringArgumentException

  def roomHear(self, msg):

    if isinstance(msg, basestring):
      self.msg["room"].append(msg)
    else: raise NonStringArgumentException

  def buildString(self):
    pass

  def action(self):
    pass

  def _final(self):

    if self.isinterface:
      self.msg["self"].insert(0, self.interface_border)
      self.msg["self"].append(self.interface_border)
    if self.player:
      self.player.hear("\n".join(self.msg["self"]))
    if self.target:
      self.target.hear("\n".join(self.msg["target"]))

  def executeCmd(self, player, args = None):

    self.player = player
    self.cmd_entered = args[0]
    self.args = args[1:]

    self.action()
    self.buildString()
    self._final()
