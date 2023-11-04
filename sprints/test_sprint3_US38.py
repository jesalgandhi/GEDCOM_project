import unittest
from datetime import datetime
import sprint3


class TestUS38(unittest.TestCase):
    def test_upcoming_birthday_within_30_days(self):
        individuals = {
            '1': {'name': 'John', 'birthdate': '10 Nov 2000'},
            '2': {'name': 'Alice', 'birthdate': '15 Dec 1995'},
        }
        today = datetime(2023, 11, 5)  # Current date for testing
        self.assertEqual(sprint3.US38(individuals), None)

    def test_no_upcoming_birthday_within_30_days(self):
        individuals = {
            '1': {'name': 'John', 'birthdate': '10 Nov 2000'},
            '2': {'name': 'Alice', 'birthdate': '15 Dec 1995'},
        }
        today = datetime(2023, 11, 15)  # Current date for testing
        self.assertEqual(sprint3.US38(individuals), None)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)