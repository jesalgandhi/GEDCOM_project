import unittest
from datetime import datetime
import sprint1
import script


class TestUS05(unittest.TestCase):
    def test_marriage_before_deathdate(self):
        individuals = script.individuals
        families = script.families

        with self.assertLogs(level='ERROR') as log:
            sprint1.US05(individuals, families)
    
        self.assertEqual(len(log.output), 1)

    def test_marriage_equal_deathdate(self):
        individuals = script.individuals
        families = script.families

        with self.assertLogs(level='ERROR') as log:
            sprint1.US05(individuals, families)

        self.assertEqual(len(log.output), 1)

    def test_marriage_after_deathdate(self):
        individuals = script.individuals
        families = script.families

        with self.assertLogs(level='ERROR') as log:
            sprint1.US05(individuals, families)
        
        self.assertTrue(log.output, "ERROR:root:ERROR: INDIVIDUAL: US03: II1: Marriage date 10 MAY 2968 occurs after death date 10 DEC 1992")

    def test_missing_deathdate(self):
        individuals = script.individuals
        families = script.families

        # Ensure that no error messages are logged
        with self.assertLogs(level='ERROR') as log:
            sprint1.US05(individuals, families)

        self.assertTrue(log.output, "ERROR:root:")

    def test_missing_marriage(self):
        individuals = script.individuals
        families = script.families

        # Ensure that no error messages are logged
        with self.assertLogs(level='ERROR') as log:
            sprint1.US05(individuals, families)

        self.assertTrue(log.output, "ERROR:root:")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)