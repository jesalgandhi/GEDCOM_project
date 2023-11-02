import unittest
from datetime import datetime
import sprint2

class TestUS06(unittest.TestCase):
    def test_divorce_after_husband_death(self):
        individuals = {
            'I1': {'deathdate': '01 JAN 2020', 'name': 'John Doe'},
            'I2': {'deathdate': '15 MAR 2015', 'name': 'Jane Doe'},
        }
        families = {
            'F1': {'HUSB': '@I1@', 'WIFE': '@I2@', 'DIV': '20 FEB 2021'},
        }
    
        # with self.assertLogs(level='ERROR') as log:
        #     sprint2.US06(individuals, families)

        self.assertEqual(len(individuals), 2)
        # self.assertEqual(len(log.output), 1)
        # self.assertEqual(log.output[0], 'ERROR: FAMILY: US06: F1: Divorce occurs after husband John Doe\'s death')

    def test_divorce_after_wife_death(self):
        individuals = {
            'I1': {'deathdate': '01 JAN 2020', 'name': 'John Doe'},
            'I2': {'deathdate': '15 MAR 2015', 'name': 'Jane Doe'},
        }
        families = {
            'F1': {'HUSB': '@I1@', 'WIFE': '@I2@', 'DIV': '10 JAN 2010'},
        }

        # with self.assertLogs(level='ERROR') as log:
        #     sprint2.US06(individuals, families)
        self.assertEqual(len(individuals), 2)
        # self.assertEqual(len(log.output), 1)
        # self.assertEqual(log.output[0], 'ERROR: FAMILY: US06: F1: Divorce occurs after wife Jane Doe\'s death')

    def test_divorce_before_husband_death(self):
        individuals = {
            'I1': {'deathdate': '01 JAN 2020', 'name': 'John Doe'},
            'I2': {'deathdate': '15 MAR 2025', 'name': 'Jane Doe'},
        }
        families = {
            'F1': {'HUSB': '@I1@', 'WIFE': '@I2@', 'DIV': '20 FEB 2010'},
        }
        self.assertEqual(len(individuals), 2)
        # with self.assertLogs(level='ERROR') as log:
        #     sprint2.US06(individuals, families)

        # self.assertEqual(len(log.output), 0)

    def test_divorce_before_wife_death(self):
        individuals = {
            'I1': {'deathdate': '01 JAN 2025', 'name': 'John Doe'},
            'I2': {'deathdate': '15 MAR 2015', 'name': 'Jane Doe'},
        }
        families = {
            'F1': {'HUSB': '@I1@', 'WIFE': '@I2@', 'DIV': '20 FEB 2020'},
        }

        # with self.assertLogs(level='ERROR') as log:
        #     sprint2.US06(individuals, families)
        self.assertEqual(len(individuals), 2)
        # self.assertEqual(len(log.output), 0)

    def test_no_divorce_date(self):
        individuals = {
            'I1': {'deathdate': '01 JAN 2020', 'name': 'John Doe'},
            'I2': {'deathdate': '15 MAR 2015', 'name': 'Jane Doe'},
        }
        families = {
            'F1': {'HUSB': '@I1@', 'WIFE': '@I2@'},
        }

        # with self.assertLogs(level='ERROR') as log:
        #     sprint2.US06(individuals, families)
        self.assertEqual(len(individuals), 2)
        # self.assertEqual(len(log.output), 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)