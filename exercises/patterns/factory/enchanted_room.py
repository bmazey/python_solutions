from exercises.patterns.factory.room import Room

class EnchantedRoom(Room):

    """An EnchantedRoom casts a spell on the player."""

    def __init__(self, room_number, spell):
        super().__init__(room_number)
        self.spell = spell

