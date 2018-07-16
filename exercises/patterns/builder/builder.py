import abc


class Builder:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_wheels(self, value):
        pass

    @abc.abstractmethod
    def set_doors(self, value):
        pass

    @abc.abstractmethod
    def set_fuel(self, value):
        pass

    @abc.abstractmethod
    def set_color(self, value):
        pass

    @abc.abstractmethod
    def get_result(self):
        pass

