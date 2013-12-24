'''
Created on Dec 22, 2013

@author: Justin
'''

from basecommand import BaseCommand as bc
from src.world import World

# Classes in this module should be in alphabetical order

class Look(bc):
  """look"""
  
  def action(self):
    
    room = World.rooms.get(str(self.player.location))
    if room:
      self.playerHear(room.name)
      self.playerHear(self.interface_border)
      self.playerHear(room.description)


class ShowStats(bc):
  """score stats"""

  def action(self):

    self.isinterface = True
    self.playerHear("HP: {}".format(self.player.hp["max"]))
