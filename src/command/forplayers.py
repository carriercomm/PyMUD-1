'''
Created on Dec 22, 2013

@author: Justin
'''

from basecommand import BaseCommand as bc

# Classes in this module should be in alphabetical order


class ShowStats(bc):
  """score stats"""

  def action(self):

    self.playerHear("=" * 80)
    self.playerHear("HP: {}".format(self.player.hp["max"]))
    self.playerHear("=" * 80)

