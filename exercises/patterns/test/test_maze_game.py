from exercises.patterns.factory.maze_factory import MazeFactory
from exercises.patterns.factory.enchanted_maze_factory import EnchantedMazeFactory
from exercises.patterns.factory.player import Player
from exercises.patterns.factory.wizard import Wizard
from exercises.patterns.factory.direction import Direction
from exercises.patterns.factory.maze_game import create_factory_maze_type_a, create_factory_maze_type_b

maze = create_factory_maze_type_a(MazeFactory)
enchanted_maze = create_factory_maze_type_b(EnchantedMazeFactory)

pinky = Player("Pinky", maze.get_room_by_number(1))
harry = Wizard("Harry", enchanted_maze.get_room_by_number(1))


def test_play_maze():
    play(maze, pinky)


def test_play_enchanted_maze():
    play_enchanted(enchanted_maze, harry)


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

