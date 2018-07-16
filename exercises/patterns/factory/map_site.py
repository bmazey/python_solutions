# borrowed from http://pythoninthepink.blogspot.com/


class MapSite(object):

    """Abstract for Maze elements"""

    def enter(self, player):
        """Entering this abstract site can't be good..."""
        print(player.player_id, "says: Ouch!")

