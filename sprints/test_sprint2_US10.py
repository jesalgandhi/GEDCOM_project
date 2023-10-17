import unittest
from datetime import datetime
import sprint2


class TestUS10(unittest.TestCase):
    def test_illegal_marriages(self):
        individuals = {
            'I1': {'id': 'I1', 'name': 'John Doe', 'birthdate': '01 JAN 1980'},
            'I2': {'id': 'I2', 'name': 'Jane Doe', 'birthdate': '05 FEB 2020'},
        }

        families = {
            'F1': {'id': 'F1', 'husb_id': 'I1', 'wife_id': 'I2'}
        }

        self.assertEqual(sprint2.US10(individuals, families), ['F1'])

    def test_legal_marriages(self):
        individuals = {
            'I1': {'id': 'I1', 'name': 'John Doe', 'birthdate': '01 JAN 1980'},
            'I2': {'id': 'I2', 'name': 'Jane Doe', 'birthdate': '05 FEB 1982'},
        }

        families = {
            'F1': {'id': 'F1', 'husb_id': 'I1', 'wife_id': 'I2'}
        }
        
        self.assertEqual(sprint2.US10(individuals, families), [])



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)