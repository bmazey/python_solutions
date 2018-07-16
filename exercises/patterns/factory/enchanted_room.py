# borrowed from http://pythoninthepink.blogspot.com/

from exercises.patterns.factory.room import Room


class EnchantedRoom(Room):

    """An EnchantedRoom casts a spell on the player."""

    def __init__(self, room_number, spell):
        super().__init__(room_number)
        self.spell = spell

    def enter(self, player):
        super(EnchantedRoom, self).enter(player)
        print("{} is under the spell {}".format(player.player_id, self.spell))

