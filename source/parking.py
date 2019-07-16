from parking_slot import ParkingSlot
from car_detail import Car
import sys


class Parking(object):
    """
    Parking class used for all the parking operations.

    Attributes:
        _parking_slots (dict): Contain all parking slots.
        _slot_count (int): Count of parking slots.
        _available_slots (list): Available slots for parking.
    """

    def __init__(self):
        self._parking_slots = dict()
        self._slot_count = 0
        self._available_slots = []

    def create_parking_lot(self, slot_count):
        """
           Method to create a parking lot.

           Parameters:
               slot_count (string): Slot Number in the parking
           Returns:
               None
        """
        self._slot_count = int(slot_count)

        if self._parking_slots:
            print("Parking Lot is already created")
            return

        if self._slot_count <= 0:
            print("The parking slot count should be a positive integer greater than zero")
            return

        else:
            for i in range(1, self._slot_count + 1):
                parking_slot_obj = ParkingSlot(i, True)
                self._parking_slots[i] = parking_slot_obj
                self._available_slots.append(parking_slot_obj)
            print("Created a parking lot with %s slots" % self._slot_count)
        return

    def park(self, registration_no, colour):
        """
           Method to park a car (Note: car registration no should be unique )

           Parameters:
               registration_no (string): Registration No of car to be parked.
               colour (string) : Color of the car to be parked.

           Returns:
               None
        """
        if not self.__is_parking_lot_created:
            return

        if self._available_slots:
            self._available_slots[0].park_car_in_slot(Car.create(registration_no, colour))
            print("Allocated slot number: %s" % self._available_slots[0].slot_no)
            self.__set_available_slots()
        else:
            print("Sorry, parking lot is full")

    def leave(self, slot_no):
        """
           Method to empty a slot for a given slot no.

           Parameters:
               slot_no (string): Slot Number of the parking spot

           Returns:
               None
        """
        slot_no = int(slot_no)
        if not self.__is_parking_lot_created:
            return

        if slot_no not in range(1, self._slot_count + 1):
            print("Sorry, this slot number does not exist in parking lot.")

        if slot_no in self._parking_slots:
            parking_slot = self._parking_slots[slot_no]
            if not parking_slot.is_available and parking_slot.car:
                parking_slot.remove_car_from_slot()
                print("Slot number %s is free" % slot_no)
                self.__set_available_slots()
            else:
                print("No car is present at slot number %s" % slot_no)

    def status(self):
        """
           Method to print the status of the parking.

           Parameters:

           Returns:
               String : The tabular version of the parking status with parked cars.
        """
        if not self.__is_parking_lot_created:
            return

        print("Slot No.\tRegistration No\tColour")
        for parking_slot in self._parking_slots.values():
            if not parking_slot.is_available:
                print("%s\t%s\t%s" % (parking_slot.slot_no, parking_slot.car.registration_no, parking_slot.car.colour))

    def __set_available_slots(self):
        """
            Method to set the list of available slots in parking.

            Parameters:

            Returns:
                None
        """
        available_slots = filter(lambda x: x.is_available, self._parking_slots.values())
        self._available_slots = sorted(available_slots, key=lambda x: x.slot_no)

    @property
    def __is_parking_lot_created(self):
        """
            Method to check whether the parking lot is created or not.

            Parameters:

            Returns:
                Boolean : True if parking lot created else False.
        """
        if not self._parking_slots:
            print("Parking Lot is not created yet")
            return False
        return True

    def __is_car_available_in_parking(self, registration_no):
        """
            Method to check if the car with a registration_no present in parking or not.

            Parameters:
                registration_no (string) : The registration no of the car.

            Returns:
                Boolean : True if car is already presnet in the parking.
        """
        return True if list(filter(lambda x: x.car and x.car.registration_no == registration_no,
                                   self._parking_slots.values())) else False
