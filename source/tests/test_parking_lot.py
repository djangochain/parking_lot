import unittest

from parking import Parking

class TestParkingLot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parking = Parking()
        cls.allocated_slot = 1
        cls.allocated_color = "White"
        cls.allocated_registration_no = "KA-12-FF-2017"

    def test_a_create_parking_lot(self):
        parking_slots = '6'
        self.parking.create_parking_lot(parking_slots)
        self.assertEqual(len(self.parking._parking_slots), int(parking_slots), msg="Wrong parking lot created")

    def test_b_park(self):
        self.parking.park(self.allocated_registration_no, self.allocated_color)
        self.assertFalse(self.parking._parking_slots[self.allocated_slot].is_available, "Park failed.")
        for i in self.parking._parking_slots.values():
            if not i.is_available and i.car:
                self.assertEqual(i.car.registration_no, self.allocated_registration_no, "Park failed")
                self.assertEqual(i.car.colour, self.allocated_color, "Park failed")

    def test_c_registration_numbers_for_cars_with_colour(self):
        self.parking.registration_numbers_for_cars_with_colour(self.allocated_color)
        self.assertTrue(self.parking._parking_slots[self.allocated_slot].car.colour == self.allocated_color,
                        "registration Numbers Failed")

    def test_d_slot_numbers_for_cars_with_colour(self):
        self.parking.slot_numbers_for_cars_with_colour(self.allocated_color)
        self.assertTrue(self.parking._parking_slots[self.allocated_slot].slot_no == self.allocated_slot,
                        "Slot Numbers With Color Failed")

    def test_f_slot_number_for_registration_number(self):
        self.parking.slot_number_for_registration_number(self.allocated_registration_no)
        self.assertTrue(self.parking._parking_slots[self.allocated_slot].slot_no == self.allocated_slot,
                        "Slot Numbers For Registration Number Failed")

    def test_g_leave(self):
        self.parking.leave(self.allocated_slot)
        self.assertTrue(self.parking._parking_slots[self.allocated_slot].is_available, "Leave failed.")

    @classmethod
    def tearDownClass(cls):
        del cls.parking


if __name__ == '__main__':
    unittest.main()
