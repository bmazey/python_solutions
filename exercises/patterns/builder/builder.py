from abc import ABCMeta, abstractmethod

class Builder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_wheels(self, value):
        pass

    @abstractmethod
    def set_doors(self, value):
        pass

    @abstractmethod
    def set_fuel(self, value):
        pass

    @abstractmethod
    def set_color(self, value):
        pass

    @abstractmethod
    def get_result(self):
        pass

