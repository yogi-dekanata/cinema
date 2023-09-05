from controller.cinema_controller import CinemaController
from unittest import TestCase

class TestCinemaController(TestCase):
    def setUp(self):
        self.controller = CinemaController()
        self.controller.initialize_seats("A", 5)

    def test_initialize_seats(self):
        self.assertEqual(len(self.controller.seats), 5)
        self.assertEqual(self.controller.seats[0].code, "A1")

    def test_book_seat(self):
        self.controller.book_seat("A1")
        self.assertEqual(self.controller.seats[0].is_sold, True)

    def test_cancel_seat(self):
        self.controller.book_seat("A1")
        self.controller.cancel_seat("A1")
        self.assertEqual(self.controller.seats[0].is_sold, False)

