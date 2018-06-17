from exercises.patterns.builder.car_builder import CarBuilder

class CarBuilderDirector(object):

    @staticmethod
    def constructSuv():
        builder = CarBuilder()
        builder.set_wheels(4)
        builder.set_doors(4)
        builder.set_fuel('Unleaded Gas')
        builder.set_color('Yellow')
        return builder.get_result()

# Let's try it out below ...
car = CarBuilderDirector.constructSuv()
print(car)