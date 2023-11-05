import unittest
from datetime import datetime
import sprint3

class TestUS21(unittest.TestCase):
    def test_corrent_gender_roles(self):
        individuals = {
            '1': {'name': 'John /Smith/', 'sex': 'M'},
            '2': {'name': 'Robert /Smith/', 'sex': 'M'},
            '3': {'name': 'Alice /Smith/', 'sex': 'F'},
            '4': {'name': 'David /Smith/', 'sex': 'M'},
        }
        families = {
            'F1': {'HUSB': 'I1', 'WIFE': 'I3'}
        }
        self.assertEqual(sprint3.US21(individuals, families), None)

    def test_incorrent_gender_roles(self):
        individuals = {
            '1': {'name': 'Georgia /Town/', 'sex': 'F'},
            '2': {'name': 'Ken /Carson/', 'sex': 'F'},
            '3': {'name': 'Rick /Owens/', 'sex': 'M'},
            '4': {'name': 'Patrick /Smith/', 'sex': 'F'},
        }
        families = {
            'F1': {'HUSB': 'I4', 'WIFE': 'I2'}
        }
        self.assertEqual(sprint3.US21(individuals, families), None)
    
    def test_more_incorrent_gender_roles(self):
        individuals = {
            '1': {'name': 'Deeder /John/', 'sex': 'M'},
            '2': {'name': 'Fabio /Tominic/', 'sex': 'M'},
            '3': {'name': 'Bryan /Shehan/', 'sex': 'F'},
            '4': {'name': 'Kelsey /Kylie/', 'sex': 'M'},
        }
        families = {
            'F1': {'HUSB': 'I10', 'WIFE': 'I1'}
        }
        self.assertEqual(sprint3.US21(individuals, families), None)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
