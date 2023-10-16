import unittest
from datetime import datetime
import sprint2
import script

class TestUS42(unittest.TestCase):
    def illegitmate_dates(self):
        individuals = {
            'I1': {'birthdate': '19 JUL 1985', 'deathdate': '32 JAN 2020', 'children': 'I2'},
            'I2': {'birthdate': '92 DEC 1975', 'deathdate': '15 MAR 2015', 'chilren': 'I3, I4'}
        }
        families = {
            'I1': {'birthdate': '30 OCT 1967', 'deathdate': '01 JAN 2020', 'chilren': 'I9, I12'},
            'I2': {'birthdate': '29 FEB 1980', 'deathdate': '15 MAR 2015', 'chilren': 'I1'}
        }

        result = sprint2.US42(script.individuals, script.families)

        # print(log.output)

        self.assertEqual(len(individuals) + len(families), 4)

    def more_illegitimate_dates(self):
        individuals = {
            'I1': {'birthdate': '20 MAY 1975', 'deathdate': '01 JAN 2020', 'children': ''},
            'I2': {'birthdate': '52 AUG 2000', 'deathdate': '15 MAR 2015', 'chilren': ''}
        }
        families = {
            'I1': {'birthdate': '92 JAN 1999', 'deathdate': '01 JAN 2020', 'chilren': ''}
        }

        result = sprint2.US42(script.individuals, script.families)

        # print(log.output)

        self.assertEqual(len(individuals) + len(families), 3)

    def no_illegitimate_dates(self):
        individuals = {
            'I1': {'birthdate': '22 MAY 2013', 'deathdate': '01 JAN 2020', 'children': ''},
            'I2': {'birthdate': '02 FEB 2013', 'deathdate': '30 SEP 2015', 'chilren': 'I3, I4, I9'}
        }
        families = {
            'I1': {'birthdate': '02 JAN 2019', 'deathdate': '01 JAN 2020', 'chilren': 'I2'}, 
            'I1': {'birthdate': '23 JAN 2019', 'deathdate': '01 JAN 2020', 'children': ''}
        }

        result = sprint2.US42(script.individuals, script.families)

        # print(log.output)

        self.assertEqual(len(individuals) + len(families), 4)



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)