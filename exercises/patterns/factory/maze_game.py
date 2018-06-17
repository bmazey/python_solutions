# borrowed from http://pythoninthepink.blogspot.com/

from exercises.patterns.factory.maze import Maze
from exercises.patterns.factory.direction import Direction
from exercises.patterns.factory.room import Room
from exercises.patterns.factory.door import Door
from exercises.patterns.factory.wall import Wall
from exercises.patterns.factory.player import Player
from exercises.patterns.factory.enchanted_room import EnchantedRoom
from exercises.patterns.factory.enchanted_door import EnchantedDoor

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

    door = room1.get_side(Direction.EAST)
    player.unlock_with_spell(door)
    player = door.enter(player)

    for side in Direction.ALL:
        print("\t{} SIDE: {}".format(side, room1.get_side(side)))

if __name__ == "__main__":
    maze = create_maze()
    enchanted_maze = create_enchanted_maze()
    play(maze, Player("Pinky", maze.get_room_by_number(1)))
    play_enchanted("Harry", enchanted_maze.get_room_by_number(1))

