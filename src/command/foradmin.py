
from src.command.basecommand import BaseCommand as bc
from src.world import World
import src.constants as const

# All classes in this module should be in alphabetical order

class CreateRoom(bc):
  """build"""

  def action(self):

    if self.room == None:
      self.sendMsg("You're nowhere", "players")
      return
    x, y, z = self.player.location

    typed_direction = self.args[0]
    direction = const.DIRECTION_SHORTCUT.get(typed_direction)
    if not direction:
      self.sendMsg("You didn't enter a valid direction", "player")
      return
  

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
    coords = (x, y, z)
    if str(coords) in self.player.server.world.rooms.keys()
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

