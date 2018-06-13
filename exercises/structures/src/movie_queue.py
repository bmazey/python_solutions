class MovieQueue:
    def __init__(self):
        self.queue = list()

    def populate_movie_queue(self):
        self.queue.insert(0, 'Donatello')
        self.queue.insert(1, 'Raphael')
        self.queue.insert(2, 'Michelangelo')
        self.queue.insert(3, 'Leonardo')