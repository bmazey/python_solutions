# borrowed from http://pythoninthepink.blogspot.com/


class Maze(object):

    """Maze contains Rooms"""

    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        """Add a Room"""
        self.rooms[room.room_number] = room

    def get_room_by_number(self, room_number):
        """Get Room by its number"""
        return self.rooms[room_number]

