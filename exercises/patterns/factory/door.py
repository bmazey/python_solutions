# borrowed from http://pythoninthepink.blogspot.com/

from exercises.patterns.factory.map_site import MapSite


class Door(MapSite):

    """A Door joins two Rooms. It has two states: open and closed."""

    def __init__(self, room1, room2, is_open=False):
        super().__init__()
        self.open = is_open
        self.rooms = {
            room2.room_number: room1,  # from room 2 we can get to room 1
            room1.room_number: room2   # from room 1 we can get to room 2
        }

    def other_side_from(self, room):
        """Return the Room object from the other side of the Door."""
        return self.rooms[room.room_number]

    @property
    def is_open(self):
        """Returns True if the Door is opened; False otherwise."""
        return self.open

    def unlock(self):
        self.open = True
        print("The door is now unlocked!")

    def enter(self, player):
        """Entering the door means going to room on the other side. A player can enter the door only if it's opened."""
        if self.is_open:
            other_room = self.other_side_from(player.current_room)
            other_room.enter(player)
        else:
            super().enter(player)

