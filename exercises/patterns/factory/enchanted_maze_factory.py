# borrowed from http://pythoninthepink.blogspot.com/

from random import choice

from exercises.patterns.factory.maze_factory import MazeFactory
from exercises.patterns.factory.enchanted_room import EnchantedRoom
from exercises.patterns.factory.enchanted_door import EnchantedDoor


class EnchantedMazeFactory(MazeFactory):

    """Factory producting Enchanted Maze."""

    SPELLS = ("Wingardium Leviosa", "Confundus", "Expelliarmus")

    @classmethod
    def make_room(cls, room_number):
        spell = choice(cls.SPELLS)
        return EnchantedRoom(room_number, spell)

    @staticmethod
    def make_door(room1, room2):
        return EnchantedDoor(room1, room2)

