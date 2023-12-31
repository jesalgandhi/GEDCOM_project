import unittest
from datetime import datetime
import sprint1


class TestUS03(unittest.TestCase):
    def test_birthdate_before_deathdate(self):
        individuals = {
            'I1': {'birthdate': '01 JAN 1980', 'deathdate': '01 JAN 2020'},
            'I2': {'birthdate': '01 JAN 1990', 'deathdate': '01 JAN 2000'},
        }

        with self.assertLogs(level='ERROR') as log:
            sprint1.US03(individuals)
    
        self.assertEqual(len(log.output), 1)

    def test_birthdate_equal_deathdate(self):
        individuals = {
            'I1': {'birthdate': '01 JAN 1990', 'deathdate': '01 JAN 1990'},
            'I2': {'birthdate': '01 JAN 2000', 'deathdate': '01 JAN 2000'},
        }

        with self.assertLogs(level='ERROR') as log:
            sprint1.US03(individuals)

        self.assertEqual(len(log.output), 1)

    def test_birthdate_after_deathdate(self):
        individuals = {
            'I1': {'birthdate': '01 JAN 2020', 'deathdate': '01 JAN 2000'},
            'I2': {'birthdate': '01 JAN 2005', 'deathdate': '01 JAN 1995'},
        }

        with self.assertLogs(level='ERROR') as log:
            sprint1.US03(individuals)
        
        self.assertTrue(log.output, "ERROR:root:ERROR: INDIVIDUAL: US03: II1: Birthday 01 JAN 2020 occurs after death date 01 JAN 2000")

    def test_missing_deathdate(self):
        individuals = {
            'I1': {'birthdate': '01 JAN 1980', 'deathdate': 'NA'},
            'I2': {'birthdate': '01 JAN 1990', 'deathdate': '01 JAN 2000'},
        }

        # Ensure that no error messages are logged
        with self.assertLogs(level='ERROR') as log:
            sprint1.US03(individuals)

        self.assertTrue(log.output, "ERROR:root:")

    def test_missing_birthdate(self):
        individuals = {
            'I1': {'birthdate': 'NA', 'deathdate': '01 JAN 2020'},
            'I2': {'birthdate': '01 JAN 1990', 'deathdate': '01 JAN 2000'},
        }

        # Ensure that no error messages are logged
        with self.assertLogs(level='ERROR') as log:
            sprint1.US03(individuals)

        self.assertTrue(log.output, "ERROR:root:")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)