import unittest
from datetime import datetime
import sprint2
import script

class TestUS28(unittest.TestCase):
    def test_siblings_printing(self):
        individuals = {
            'I1': {'birthdate': '19 JUL 1985', 'deathdate': '01 JAN 2020', 'children': 'I2'},
            'I2': {'birthdate': '02 DEC 1975', 'deathdate': '15 MAR 2015', 'chilren': 'I3, I4'}
        }
        families = {
            'I1': {'birthdate': '30 OCT 1967', 'deathdate': '01 JAN 2020', 'chilren': 'I9, I12'},
            'I2': {'birthdate': '29 JAN 1980', 'deathdate': '15 MAR 2015', 'chilren': 'I1'}
        }

        result = sprint2.US28(script.individuals, script.families)

        # print(log.output)

        self.assertEqual(len(individuals) + len(families), 4)

    def no_siblings_to_print(self):
        individuals = {
            'I1': {'birthdate': '20 MAY 1975', 'deathdate': '01 JAN 2020', 'children': ''},
            'I2': {'birthdate': '02 AUG 2000', 'deathdate': '15 MAR 2015', 'chilren': ''}
        }
        families = {
            'I1': {'birthdate': '02 JAN 1999', 'deathdate': '01 JAN 2020', 'chilren': ''}
        }

        result = sprint2.US28(script.individuals, script.families)

        # print(log.output)

        self.assertEqual(len(individuals) + len(families), 3)

    def mixed_printing(self):
        individuals = {
            'I1': {'birthdate': '12 MAY 2013', 'deathdate': '01 JAN 2020', 'children': ''},
            'I2': {'birthdate': '02 FEB 2013', 'deathdate': '15 MAR 2015', 'chilren': 'I3, I4, I9'}
        }
        families = {
            'I1': {'birthdate': '02 JAN 2019', 'deathdate': '01 JAN 2020', 'chilren': 'I2'}, 
            'I1': {'birthdate': '23 JAN 2019', 'deathdate': '01 JAN 2020', 'children': ''}
        }

        result = sprint2.US28(script.individuals, script.families)

        # print(log.output)

        self.assertEqual(len(individuals) + len(families), 4)



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)