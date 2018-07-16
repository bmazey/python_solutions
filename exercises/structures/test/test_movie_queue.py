from exercises.structures.src.movie_queue import MovieQueue

mq = MovieQueue()
mq.populate_movie_queue()


def test_first_entry():
    assert mq.queue[0].casefold() == 'Donatello'.casefold()


def test_second_entry():
    assert mq.queue[1].casefold() == 'Raphael'.casefold()


def test_third_entry():
    assert mq.queue[2].casefold() == 'Michelangelo'.casefold()


def test_fourth_entry():
    assert mq.queue[3].casefold() == 'Leonardo'.casefold()