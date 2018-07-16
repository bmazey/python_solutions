# borrowed from http://pythoninthepink.blogspot.com/

from exercises.patterns.factory.map_site import MapSite
from exercises.patterns.factory.direction import Direction


class Room(MapSite):

    """Represent a Room with four sides"""

    def __init__(self, room_number):
        super().__init__()
        self.sides = {
            Direction.NORTH: None,
            Direction.SOUTH: None,
            Direction.EAST: None,
            Direction.WEST: None
        }
        self.room_number = room_number

    def get_side(self, direction):
        """Returns a MapSite object for given Direction"""
        return self.sides[direction]

    def set_side(self, direction, map_site_object):
        """Set a MapSite object for given Direction"""
        self.sides[direction] = map_site_object

    def enter(self, player):
        """Entering a room changes player's location."""
        print("--> {} enters room: {}".format(player.player_id, self.room_number))
        player.current_room = self

