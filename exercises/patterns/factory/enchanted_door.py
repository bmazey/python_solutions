# borrowed from http://pythoninthepink.blogspot.com/

from exercises.patterns.factory.door import Door


class EnchantedDoor(Door):

    """An EnchantedDoor can't be opened manually, a wizard has to cast a spell to open it."""

    def __init__(self, room1, room2):
        super().__init__(room1, room2)

    def enter(self, player):
        super().enter(player)
        if not self.is_open:
            print("You need to cast a spell first ...")

    def unlock(self, with_spell=False):
        """Unlocking without a spell doesn't work."""

        if not with_spell:
            print("You need to cast a spell first ...")
        else:
            print(with_spell)
            super().unlock()
