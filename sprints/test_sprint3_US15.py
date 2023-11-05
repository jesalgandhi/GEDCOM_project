import unittest
from datetime import datetime
import sprint3

class TestUS15(unittest.TestCase):
    def test_fewer_than_fiften_siblings(self):
        families = {
            'F1': {'HUSB': 'I1', 'WIFE': 'I3', 'CHIL': ['I2', 'I4']},
        }
        self.assertEqual(sprint3.US15(families), None)

    def test_more_than_fiften_siblings(self):
        families = {
            'F1': {'HUSB': 'I4', 'WIFE': 'I9', 'CHIL': ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10', 'I11', 'I12', 'I13', 'I14', 'I15',]},
        }
        self.assertEqual(sprint3.US15(families), None)

    def test_less_than_fiften_siblings(self):
        families = {
            'F1': {'HUSB': 'I6', 'WIFE': 'I9', 'CHIL': ['I2', 'I4', 'I1', 'I10']},
        }
        self.assertEqual(sprint3.US15(families), None)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
