# borrowed from http://pythoninthepink.blogspot.com/

from exercises.patterns.factory.maze import Maze
from exercises.patterns.factory.direction import Direction
from exercises.patterns.factory.room import Room
from exercises.patterns.factory.door import Door
from exercises.patterns.factory.wall import Wall
from exercises.patterns.factory.player import Player
from exercises.patterns.factory.wizard import Wizard
from exercises.patterns.factory.enchanted_room import EnchantedRoom
from exercises.patterns.factory.enchanted_door import EnchantedDoor
from exercises.patterns.factory.maze_factory import MazeFactory
from exercises.patterns.factory.enchanted_maze_factory import EnchantedMazeFactory

def create_maze():
    """Series of operations which create our Maze."""
    maze = Maze()
    room1 = Room(1)
    room2 = Room(2)
    door = Door(room1, room2)

    maze.add_room(room1)
    maze.add_room(room2)

    room1.set_side(Direction.NORTH, Wall())
    room1.set_side(Direction.EAST, door)
    room1.set_side(Direction.SOUTH, Wall())
    room1.set_side(Direction.WEST, Wall())

    room2.set_side(Direction.NORTH, Wall())
    room2.set_side(Direction.EAST, Wall())
    room2.set_side(Direction.SOUTH, Wall())
    room2.set_side(Direction.WEST, door)

    return maze

def create_enchanted_maze():
    """Series of operations which create our Maze."""
    maze = Maze()
    room1 = EnchantedRoom(1)
    room2 = EnchantedRoom(2)
    door = EnchantedDoor(room1, room2)

    maze.add_room(room1)
    maze.add_room(room2)

    room1.set_side(Direction.NORTH, Wall())
    room1.set_side(Direction.EAST, door)
    room1.set_side(Direction.SOUTH, Wall())
    room1.set_side(Direction.WEST, Wall())

    room2.set_side(Direction.NORTH, Wall())
    room2.set_side(Direction.EAST, Wall())
    room2.set_side(Direction.SOUTH, Wall())
    room2.set_side(Direction.WEST, door)

    return maze

# these are the ones we care the most about!
def create_factory_maze_type_a(factory):
    """Series of operations which create our Maze."""

    maze = factory.make_maze()
    room1 = factory.make_room(1)
    room2 = factory.make_room(2)
    door = factory.make_door(room1, room2)

    maze.add_room(room1)
    maze.add_room(room2)

    room1.set_side(Direction.NORTH, factory.make_wall())
    room1.set_side(Direction.EAST, door)
    room1.set_side(Direction.SOUTH, factory.make_wall())
    room1.set_side(Direction.WEST, factory.make_wall())

    room2.set_side(Direction.NORTH, factory.make_wall())
    room2.set_side(Direction.EAST, factory.make_wall())
    room2.set_side(Direction.SOUTH, factory.make_wall())
    room2.set_side(Direction.WEST, door)

    return maze

def create_factory_maze_type_b(factory):
    """Series of operations which create our Maze."""

    maze = factory.make_maze()
    room1 = factory.make_room(1)
    room2 = factory.make_room(2)
    door = factory.make_door(room1, room2)

    maze.add_room(room1)
    maze.add_room(room2)

    room1.set_side(Direction.NORTH, factory.make_wall())
    room1.set_side(Direction.EAST, factory.make_wall())
    room1.set_side(Direction.SOUTH, door)
    room1.set_side(Direction.WEST, factory.make_wall())

    room2.set_side(Direction.NORTH, door)
    room2.set_side(Direction.EAST, factory.make_wall())
    room2.set_side(Direction.SOUTH, factory.make_wall())
    room2.set_side(Direction.WEST, factory.make_wall())

    return maze

def play(maze, player):
    print("\n--> Player {} enters the maze in room {}".format(player.player_id, player.current_room.room_number))
    room1 = player.current_room
    for side in Direction.ALL:
        print("\t{} SIDE: {}".format(side, room1.get_side(side)))

    door = room1.get_side(Direction.EAST)
    if not door.is_open:
        door.unlock()
        door.enter(player)

    # lol, this line gave me so many headaches - python is different than Java! :)
    room2 = player.current_room
    for side in Direction.ALL:
        print("\t{} SIDE: {}".format(side, room2.get_side(side)))

def play_enchanted(maze, player):
    print("\n---> Wizard {} enters the enchanted maze in room {}".format(player.player_id, player.current_room.room_number))
    room1 = player.current_room
    for side in Direction.ALL:
        print("\t{} SIDE: {}".format(side, room1.get_side(side)))

    door = room1.get_side(Direction.SOUTH)
    player.unlock_with_spell(door)
    door.enter(player)

    room2 = player.current_room
    for side in Direction.ALL:
        print("\t{} SIDE: {}".format(side, room2.get_side(side)))

if __name__ == "__main__":
    maze = create_factory_maze_type_a(MazeFactory)
    enchanted_maze = create_factory_maze_type_b(EnchantedMazeFactory)
    play(maze, Player("Pinky", maze.get_room_by_number(1)))
    play_enchanted(enchanted_maze, Wizard("Harry", enchanted_maze.get_room_by_number(1)))

