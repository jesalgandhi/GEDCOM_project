import unittest
from datetime import datetime
import sprint2


class TestUS10(unittest.TestCase):

    # # calculate age of individual 
    def calculate_age(birthdate):
        if birthdate:
            today = datetime.today()
            birth_date = datetime.strptime(birthdate, "%d %b %Y")
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            return age
        return 'NA'

    #US10 illegal marriages
    def US10(individuals, families):
        illegal_marriages = []
        for fam in families:
            if 'WIFE' in families[fam]:
                wife_id = families[fam]['WIFE'][1:]
                wife_birth = individuals[wife_id]['birthdate']
                if TestUS10.calculate_age(wife_birth) < 14:
                    illegal_marriages += [fam]
            if 'HUSB' in families[fam]:
                husb_id = families[fam]['HUSB'][1:]
                husb_birth = individuals[husb_id]['birthdate']
                if TestUS10.calculate_age(husb_birth) < 14:
                    illegal_marriages += [fam]
        return illegal_marriages

    def test_illegal_marriages(self):

        individuals = {
            '1': {'id': '1', 'name': 'John Doe', 'birthdate': '01 JAN 1980'},
            '2': {'id': '2', 'name': 'Jane Doe', 'birthdate': '05 FEB 2020'},
        }

        families = {
            'F1': {'id': 'F1', 'HUSB': 'I1', 'WIFE': 'I2'}
        }

        self.assertEqual(TestUS10.US10(individuals, families), ['F1'])

    def test_legal_marriages(self):
        individuals = {
            '1': {'id': '1', 'name': 'John Doe', 'birthdate': '01 JAN 1980'},
            '2': {'id': '2', 'name': 'Jane Doe', 'birthdate': '05 FEB 1982'},
        }

        families = {
            'F1': {'id': 'F1', 'HUSB': 'I1', 'WIFE': 'I2'}
        }
        
        self.assertEqual(TestUS10.US10(individuals, families), [])

    


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)