import exercises.patterns.builder.car_builder_director as director


def test_construct_suv():
    car = director.CarBuilderDirector.construct_suv()
    assert car.wheels == 4
    assert car.doors == 4
    assert car.fuel.casefold() == 'unleaded gas'.casefold()
    assert car.color.casefold() == 'yellow'.casefold()


def test_construct_sports_car():
    car = director.CarBuilderDirector.construct_sports_car()
    assert car.wheels == 4
    assert car.doors == 2
    assert car.fuel.casefold() == 'premium gas'.casefold()
    assert car.color.casefold() == 'red'.casefold()


def test_construct_eighteen_wheeler():
    car = director.CarBuilderDirector.construct_eighteen_wheeler()
    assert car.wheels == 18
    assert car.doors == 2
    assert car.fuel.casefold() == 'diesel'.casefold()
    assert car.color.casefold() == 'blue'.casefold()


def test_construct_tesla():
    car = director.CarBuilderDirector.construct_tesla()
    assert car.wheels == 4
    assert car.doors == 4
    assert car.fuel.casefold() == 'electricity'.casefold()
    assert car.color.casefold() == 'black'.casefold()
