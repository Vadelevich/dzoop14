class Vehicle:

    def __init__(self, position):  # position: кортеж (10, 20)
        self.position = position

    def travel(self, destination):
        route = self.calculate_route(source=self.position, to=destination)
        self.move_along(route)

    @staticmethod
    def calculate_route(source, to):
        return 0  # to be realized

    def move_along(self, route):
        print("moving")


class Mixin:
    def turn_on_radio(self):
        return print(f'Playing {self}')

class Car(Vehicle):
    def __init__(self,position):
        super().__init__(position)
    def turn_on_radio(self,fm):
        Mixin.turn_on_radio(fm)

class Airplane(Vehicle):
    pass


car = Car((10, 20))
car.turn_on_radio('Moscow FM')
# Playing Moscow FM