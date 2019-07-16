from parking_slot import ParkingSlot
import sys


class Parking(object):
    """
    Parking class used for all the parking operations.

    Attributes:
        _parking_slots (dict): Contain all parking slots.
        _slot_count (int): Count of parking slots.
    """

    def __init__(self):
        self._parking_slots = dict()
        self._slot_count = 0

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
            print("Created a parking lot with %s slots" % self._slot_count)
        return
