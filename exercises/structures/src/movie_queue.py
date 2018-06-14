class MovieQueue:
    """MovieQueue class."""
    def __init__(self):
        self.queue = list()

    def populate_movie_queue(self):
        """populates a new MovieQueue"""
        self.queue.insert(0, 'Donatello')
        self.queue.insert(1, 'Raphael')
        self.queue.insert(2, 'Michelangelo')
        self.queue.insert(3, 'Leonardo')