class ParkingSlot(object):
    """
    Parking Slot class to keep data for a parking slot

    Attributes:
        slot_no (int): Slot Number.
        car (Instance): Car Object.
        is_available (Boolean): tells the availability of slot .
    """

    def __init__(self, slot_no=None, is_available=None):
        self.car = None
        self.slot_no = slot_no
        self.is_available = is_available

    def park_car_in_slot(self, car_obj):
        self.car = car_obj
        self.is_available = False

    def remove_car_from_slot(self):
        self.car = None
        self.is_available = True
