import unittest
from datetime import * 
import sprint4

class TestUS30(unittest.TestCase):
    def test_living_married_people(self):
        individuals = {
            '1': {'spouse': 'Jesal Yandhi', 'deathdate': None},
            '2': {'spouse': 'Dhihan Ahmed', 'deathdate': None},
            '3': {'spouse': 'Ajit Kandasamy', 'deathdate': None},
            '4': {'spouse': 'Harshil Bianci', 'deathdate': None}
        }
        result = []

        self.assertEqual(sprint4.US30(individuals), None)

    def test_no_living_married_people(self):
        individuals = {
            '1': {'spouse': 'Jesal Yandhi', 'deathdate': '06 10 2005'},
            '2': {'spouse': 'Dhihan Ahmed', 'deathdate': '06 10 2025'},
            '3': {'spouse': 'Ajit Kandasamy', 'deathdate': '04 23 2015'},
            '4': {'spouse': 'Harshil Bianci', 'deathdate': '06 10 2005'}
        }
        result = []

        self.assertEqual(sprint4.US30(individuals), None)

    def test_yes_living_married_people(self):
        individuals = {
            '1': {'spouse': 'Jesal Yandhi', 'deathdate': None},
            '2': {'spouse': 'Dhihan Ahmed', 'deathdate': '06 10 2025'},
            '3': {'spouse': 'Ajit Kandasamy', 'deathdate': None},
            '4': {'spouse': 'Harshil Bianci', 'deathdate': '06 10 2005'}
        }
        result = []

        self.assertEqual(sprint4.US30(individuals), None)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
