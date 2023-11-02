import unittest
from datetime import datetime
import sprint3


class TestUS35(unittest.TestCase):
    def test_recent_births(self):
        individuals = {
            'I1': {'name': 'Ajit Kandasamy','birthdate': '12 JUN 2004'},
            'I2': {'name': 'Jesal Gandhi', 'birthdate': '23 OCT 2023'},
            'I3': {'name': 'Dhihan Ahmed', 'birthdate': '19 SEP 2023'}
        }

        self.assertEqual(sprint3.US35(individuals), ['I2'])

    def test_no_recent_births(self):
        individuals = {
            'I1': {'name': 'Ajit Kandasamy','birthdate': '12 JUN 2004'},
            'I2': {'name': 'Jesal Gandhi', 'birthdate': '23 OCT 2010'},
            'I3': {'name': 'Dhihan Ahmed', 'birthdate': '14 JUL 2005'}
        }
        
        self.assertEqual(sprint3.US35(individuals), None)



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)