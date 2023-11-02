import unittest
from datetime import datetime
import sprint3


class TestUS34(unittest.TestCase):
    def test_large_age_difference(self):
        individuals = {
            '1': {'name': 'Ajit Kandasamy','birthdate': '12 JUN 2004'},
            '2': {'name': 'Amy Smith', 'birthdate': '23 OCT 2020'},
        }
        families = {
            'F1': {'WIFE': 'I2', 'HUSB': 'I1'}
        }

        self.assertEqual(sprint3.US34(individuals, families), ['F1'])

    def test_no_large_age_difference(self):
        individuals = {
            '1': {'name': 'Ajit Kandasamy','birthdate': '12 JUN 2004'},
            '2': {'name': 'Amy Smith', 'birthdate': '23 OCT 2005'},
        }
        families = {
            'F1': {'WIFE': 'I2', 'HUSB': 'I1'}
        }

        
        self.assertEqual(sprint3.US34(individuals, families), [])



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)