import unittest
from datetime import datetime
from sprint4 import US27


class TestUS27(unittest.TestCase):
    def test_individuals_with_age_in_years(self):
        individuals = {
            'I1': {'name': 'John /Smith/', 'birthdate': '01 Jan 1990'},
            'I2': {'name': 'Jane /Smith/', 'birthdate': '02 Feb 1985'},
            'I3': {'name': 'Jim /Smith/', 'birthdate': '03 Mar 2000'}
        }
        
        self.assertEqual(US27(individuals), None)

    def test_individuals_with_age_in_months(self):
        individuals = {
            'I1': {'name': 'John /Smith/', 'birthdate': '01 Jan 2022'},
            'I2': {'name': 'Jane /Smith/', 'birthdate': '02 Feb 2023'},
            'I3': {'name': 'Jim /Smith/', 'birthdate': '03 Mar 2023'},
        }
        
        self.assertEqual(US27(individuals), None)

    def test_individuals_with_zero_age(self):
        individuals = {
            'I1': {'name': 'John /Smith/', 'birthdate': '01 Jan 2023'},
            'I2': {'name': 'Jane /Smith/', 'birthdate': '02 Feb 2023'},
            'I3': {'name': 'Jim /Smith/', 'birthdate': '03 Mar 2023'},
        }
        self.assertEqual(US27(individuals), None)




if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
