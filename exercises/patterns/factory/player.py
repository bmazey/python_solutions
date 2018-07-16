# borrowed from http://pythoninthepink.blogspot.com/


class Player(object):

    """Represents position of a certain player."""

    def __init__(self, player_id, start_room):

        self.player_id = player_id
        self.current_room = start_room
