
from src.basecommand import BaseCommand as bc
from src.world import World

# All classes in this module should be in alphabetical order

class CreateRoom(bc):
  """build"""

  def action(self):

    x,y,z = self.room.coords
  
    if room == None:
      admin.hear("You're nowhere. Something's broke.", color.red)
      return
    if direction in room.exits.keys():
      admin.error("The room already exists, you goof.")
      return
  
    new_room = stuff.Room()
    new_room.coordinates = room.coordinates
    if direction == "north":       y += 1
    elif direction == "south":     y -= 1
    elif direction == "east":      x += 1
    elif direction == "west":      x -= 1
    elif direction == "northeast": y += 1 ; x += 1
    elif direction == "southeast": y -= 1 ; x += 1
    elif direction == "southwest": y -= 1 ; x -= 1
    elif direction == "northwest": y += 1 ; x -= 1
    elif direction == "up":        z += 1
    elif direction == "down":      z -= 1
    new_room.coordinates = "%s %s %s" % (str(x), str(y), str(z))
    if new_room.coordinates in stuff.ROOMS.keys():
        admin.error("You're trying to build over a room that already "
                    "exists. If you would like to proceed, type 'link', "
                    "otherwise press <enter>.")
        link = admin.input()
        if link == None: return
        if link == 'link':
            room.exits[direction] = new_room.coordinates
            existing_room = stuff.ROOMS[new_room.coordinates]
            new_direction = DIRECTION_OPPOSITE[direction]
            existing_room.exits[new_direction] = (room.coordinates)
        else:
            admin.error("Aborting build!")
    else:
        room.exits[direction] = new_room.coordinates
        new_room.exits[DIRECTION_OPPOSITE[direction]] = room.coordinates
        stuff.ROOMS[new_room.coordinates] = new_room
        new_room.name = new_room.coordinates
        new_room.desc = "# No Description #\n# No Description #\n# No Description #"

