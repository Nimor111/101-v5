import unittest
from user_interface.projection import Projection


class TestProjection(unittest.TestCase):

    def setUp(self):
        self.projection = Projection(1)

    def test_reserve_seat_works_properly_with_non_zero_values(self):
        self.projection.reserve_seat(1, 1)
        self.assertEqual(self.projection.hall[1][1], 'x')

    def test_reserve_seat_with_zero_values(self):
        self.assertRaises(IndexError, self.projection.reserve_seat, 0, 0)

    def test_free_seats_works_properly_on_taken_seat(self):
        self.projection.reserve_seat(1, 1)
        self.assertFalse(self.projection.is_free_seat((1, 1)))


if __name__ == '__main__':
    unittest.main()
