class Car(object):
    """
    Car class to have all info of car needed.

    Attributes:
        __registration_no (string): Registration number of the car.
        __colour (string): Colour of the car.
    """

    def __init__(self):
        self.__registration_no = None
        self.__colour = None

    @property
    def registration_no(self):
        return self.__registration_no

    @registration_no.setter
    def registration_no(self, value):
        self.__registration_no = value

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, value):
        self.__colour = value

    @classmethod
    def create(cls, registration_no, colour):
        car_obj = cls()
        car_obj.registration_no = registration_no
        car_obj.colour = colour
        return car_obj
