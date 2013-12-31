'''
Created on Dec 23, 2013

@author: jusmith
'''

import room


class World:
  
  rooms = {}
  mobs = {}
  players = {}

  # TODO: FRICKIN' URGENT!
  # Get these methods out of here and make World class for holding game data ONLY
  # No in game methods should be in here...

  def newRoom(self, **kwargs):
    
    new_room = room.Room(**kwargs)
    self.rooms[new_room.getStringCoords()] = new_room

  def moveObj(self, loc, obj):
    
    room = self.rooms.get(str(loc))
    old_room = self.rooms.get(str(obj.location))
    if old_room:
      old_room.removeObj(obj)
    if room:
      room.addObj(obj)

  def build(self):
    
    # this will be where the data will be read and loaded
    # when there's a pre-exisitng world
    self.newRoom(name = "Starting Room",
                 description = "This is where you start...",
                 coords = (0, 0, 0))
    
