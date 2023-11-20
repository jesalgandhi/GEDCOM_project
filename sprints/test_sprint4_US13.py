import unittest
from datetime import datetime
import sprint4


class TestUS13(unittest.TestCase):
    def test_birthdate_difference_within_range(self):
        individuals = {
            '1': {'name': 'John /Smith/', 'birthdate': '01 Jan 1990'},
            '2': {'name': 'Jane /Smith/', 'birthdate': '02 Feb 1990'},
            '3': {'name': 'Jim /Smith/', 'birthdate': '03 Mar 1990'},
        }
        families = {
            'F1': {'HUSB': 'I1', 'WIFE': 'I2', 'CHIL': ['I3', 'I1']},
        }
        self.assertIsNone(sprint4.US13(families, individuals))

    def test_birthdate_difference_outside_range(self):
        individuals = {
            '1': {'name': 'John /Smith/', 'birthdate': '01 Jan 1990'},
            '2': {'name': 'Jane /Smith/', 'birthdate': '01 Feb 1990'},
            '3': {'name': 'Jim /Smith/', 'birthdate': '03 Mar 1990'},
        }
        families = {
            'F1': {'HUSB': 'I1', 'WIFE': 'I2', 'CHIL': ['I3', 'I2']},
        }
        self.assertEqual(sprint4.US13(families, individuals), None)

    def test_single_child_family(self):
        individuals = {
            '1': {'name': 'John /Smith/', 'birthdate': '01 Jan 1990'},
        }
        families = {
            'F1': {'HUSB': 'I1', 'WIFE': 'I2', 'CHIL': []},
        }
        self.assertIsNone(sprint4.US13(families, individuals))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
