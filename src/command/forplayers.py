'''
Created on Dec 22, 2013

@author: Justin
'''

from basecommand import BaseCommand as bc
from world import World

# Classes in this module should be in alphabetical order

class Look(bc):
  """look"""
  
  def buildString(self):
    
    room = World.rooms.get(str(self.player.location))
    if room
  
  def action(self):


class ShowStats(bc):
  """score stats"""

  def action(self):

    self.playerHear("=" * 80)
    self.playerHear("HP: {}".format(self.player.hp["max"]))
    self.playerHear("=" * 80)