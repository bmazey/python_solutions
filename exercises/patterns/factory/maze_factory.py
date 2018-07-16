# borrowed from http://pythoninthepink.blogspot.com/

from exercises.patterns.factory.maze import Maze
from exercises.patterns.factory.wall import Wall
from exercises.patterns.factory.room import Room
from exercises.patterns.factory.door import Door


class MazeFactory(object):

    """Factory producing basic Maze."""

    @staticmethod
    def make_maze():
        return Maze()

    @staticmethod
    def make_wall():
        return Wall()

    @staticmethod
    def make_room(room_number):
        return Room(room_number)

    @staticmethod
    def make_door(room1, room2):
        return Door(room1, room2)

