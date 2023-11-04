import unittest
from datetime import datetime
import sprint3


class TestUS16(unittest.TestCase):
    def test_all_males_have_same_last_name(self):
        individuals = {
            '1': {'name': 'John /Smith/', 'sex': 'M'},
            '2': {'name': 'Robert /Smith/', 'sex': 'M'},
            '3': {'name': 'Alice /Smith/', 'sex': 'F'},
            '4': {'name': 'David /Smith/', 'sex': 'M'},
        }
        families = {
            'F1': {'HUSB': 'I1', 'WIFE': 'I3', 'CHIL': ['I2', 'I4']},
        }
        self.assertEqual(sprint3.US16(individuals, families), None)

    def test_some_males_have_different_last_name(self):
        individuals = {
            '1': {'name': 'John /Smith/', 'sex': 'M'},
            '2': {'name': 'Robert /Brown/', 'sex': 'M'},
            '3': {'name': 'Alice /Smith/', 'sex': 'F'},
        }
        families = {
            '1': {'HUSB': 'I1', 'WIFE': 'I3', 'CHIL': ['I2']},
        }
        self.assertEqual(sprint3.US16(individuals, families), None)

    def test_no_males_in_family(self):
        individuals = {
            '1': {'name': 'John /Smith/', 'sex': 'F'},
            '2': {'name': 'Alice /Brown/', 'sex': 'F'},
        }
        families = {
            'F1': {'WIFE': 'I1', 'HUSB': 'I2', 'CHIL': ['I2']},
        }
        self.assertEqual(sprint3.US16(individuals, families), None)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
