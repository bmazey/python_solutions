# borrowed from http://pythoninthepink.blogspot.com/

from exercises.patterns.factory.player import Player


class Wizard(Player):

    """A Wizard can cast spells."""

    def unlock_with_spell(self, door):
        door.unlock(with_spell="Alohomora!")

