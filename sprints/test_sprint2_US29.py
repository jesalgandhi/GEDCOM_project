import unittest
from datetime import datetime
import sprint2

class TestUS29(unittest.TestCase):
    def test_deathdate_present(self):
        individuals = {
            'I1': {'deathdate': '01 JAN 2020', 'name': 'A.B.'},
            'I2': {'deathdate': '15 MAR 2015', 'name': 'C.D.'},
        }

        with self.assertLogs(level='ERROR') as log:
            sprint2.US29(individuals)

        print(log.output)

        self.assertEqual(len(log.output), 2)
        # self.assertTrue(all(f"DEATH: INDIVIDUAL: US29: I{i}: Individual died on" in log.output[log_line] for i, log_line in enumerate(range(len(log.output))))

    def test_deathdate_missing(self):
        individuals = {
            'I1': {'deathdate': 'NA', 'name': 'E.F.'},
            'I2': {'deathdate': '01 JAN 2000', 'name': 'G.H.'},
        }

        with self.assertLogs(level='ERROR') as log:
            sprint2.US29(individuals)

        self.assertEqual(log.output[0], 'ERROR:root:DEATH: INDIVIDUAL: US29: II2: Individual G.H. died on 01 JAN 2000')

    def test_multiple_individuals_with_deathdate(self):
        individuals = {
            'I1': {'deathdate': '01 JAN 2020', 'name': 'I.J.'},
            'I2': {'deathdate': '15 MAR 2015', 'name': 'K.L.'},
            'I3': {'deathdate': 'NA', 'name': 'M.N.'},
            'I4': {'deathdate': '30 JUN 2012', 'name': 'O.P.'},
        }

        with self.assertLogs(level='ERROR') as log:
            sprint2.US29(individuals)

        self.assertEqual(len(log.output), 3)
        # self.assertTrue(all(f"DEATH: INDIVIDUAL: US29: I{i + 1}: Individual died on" in log.output[log_line] for i, log_line in enumerate(range(len(log.output))))

    def test_no_individuals(self):
        individuals = {}

        with self.assertLogs(level='ERROR') as log:
            sprint2.US29(individuals)

        self.assertEqual(log.output[0], "ERROR:root:")

    def test_mixed_deathdate(self):
        individuals = {
            'I1': {'deathdate': '01 JAN 2020', 'name': 'Q.R.'},
            'I2': {'deathdate': 'NA', 'name': 'S.T.'},
            'I3': {'deathdate': '15 MAR 2015', 'name': 'U.V.'},
        }

        with self.assertLogs(level='ERROR') as log:
            sprint2.US29(individuals)

        self.assertEqual(log.output[0], 'ERROR:root:DEATH: INDIVIDUAL: US29: II1: Individual Q.R. died on 01 JAN 2020')

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)