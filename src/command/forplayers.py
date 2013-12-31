'''
Created on Dec 22, 2013

@author: Justin
'''

from basecommand import BaseCommand as bc

# Classes in this module should be in alphabetical order

class Look(bc):
  """look"""
  
  def action(self):
    
    if self.room:
      msg = [self.room.name,
             self.interface_border,
             self.room.description,
             "Exits: {}".format(", ".join(self.room.exits.keys()))]
      self.sendMsg(msg, "player")
    else:
      self.sendMsg("You're nowhere...")


class Quit(bc):
  """quit logout"""
  
  def action(self):
    
    self.player.save()
    self.player.logout()


class Say(bc):
  "say"
  
  def action(self):
    
    player_msg = "You say, {}".format(" ".join(self.args))
    room_msg = "{} says, '{}'".format(self.player.name,
                                    " ".join(self.args))
    self.sendMsg(player_msg, "player")
    self.sendMsg(room_msg, "room")
          

class ShowStats(bc):
  """score stats"""

  def action(self):

    self.isinterface = True
    self.sendMsg("HP: {}".format(self.player.hp["max"]))
