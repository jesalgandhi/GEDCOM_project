import unittest
from datetime import datetime
import sprint2


class TestUS36(unittest.TestCase):
    def test_recent_deaths(self):
        individuals = {
            'I1': {'name': 'Ajit Kandasamy','deathdate': '12 JUN 2004'},
            'I2': {'name': 'Jesal Gandhi', 'deathdate': '23 OCT 2020'},
            'I3': {'name': 'Dhihan Ahmed', 'deathdate': '19 SEP 2023'}
        }

        self.assertEqual(sprint2.US36(individuals), ['I3'])

    def test_no_recent_deaths(self):
        individuals = {
            'I1': {'name': 'Ajit Kandasamy','deathdate': '12 JUN 2004'},
            'I2': {'name': 'Jesal Gandhi', 'deathdate': '23 OCT 2010'},
            'I3': {'name': 'Dhihan Ahmed', 'deathdate': '14 JUL 2005'}
        }
        
        self.assertEqual(sprint2.US36(individuals), None)



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)