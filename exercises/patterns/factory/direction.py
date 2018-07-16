# borrowed from http://pythoninthepink.blogspot.com/


class Direction(object):

    """Simple structure representing 4 directions.
    Might as well be an enum with ints - I've' put strs here for simplicity.
    """

    NORTH, SOUTH, EAST, WEST = ('NORTH', 'SOUTH', 'EAST', 'WEST')
    ALL = {NORTH, SOUTH, EAST, WEST}

