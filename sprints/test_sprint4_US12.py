import unittest
from datetime import * 

class TestUS12(unittest.TestCase):

    # # calculate age of individual 
    def calculate_age(birthdate):
        if birthdate:
            today = datetime.today()
            birth_date = datetime.strptime(birthdate, "%d %b %Y")
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            return age
        return 'NA'

    def US12(families, individuals):
        too_old = []
        for fam in families:
        
            if 'CHIL' not in families[fam] or families[fam]['CHIL'] == []:
                continue

            youngest = min(TestUS12.calculate_age(individuals[chil[1:]]['birthdate']) for chil in families[fam]['CHIL'])

            if 'WIFE' in families[fam]:
                wife_id = families[fam]['WIFE'][1:]
                wife_birth = individuals[wife_id]['birthdate']
                wife_age = TestUS12.calculate_age(wife_birth)
                if wife_age >= youngest+80:
                    too_old += [fam]
                    print(f"ERROR: FAMILY: US12: {fam}: at least one of the parents is too old")
                    continue
            
            if 'HUSB' in families[fam]:
                husb_id = families[fam]['HUSB'][1:]
                husb_birth = individuals[husb_id]['birthdate']
                husb_age = TestUS12.calculate_age(husb_birth)
                if husb_age >= youngest+100:
                    too_old += [fam]
                    print(f"ERROR: FAMILY: US12: {fam}: at least one of the parents is too old")
        return too_old

    def test_parents_not_too_old(self):
        individuals = {
            '1': {'birthdate': '01 JAN 1980', 'deathdate': None},
            '2': {'birthdate': '01 JAN 1985', 'deathdate': None},
            '3': {'birthdate': '01 JAN 2010', 'deathdate': None},
            '4': {'birthdate': '01 JAN 2015', 'deathdate': None}
        }
        families = {
            'F1': {'HUSB': 'I1', 'WIFE': 'I2', 'CHIL': ['I3', 'I4']}
        }

        result = TestUS12.US12(families, individuals)

        self.assertEqual(result, [])

    def test_mother_too_old(self):
        individuals = {
            '1': {'birthdate': '01 JAN 1930', 'deathdate': None},
            '2': {'birthdate': '01 JAN 1980', 'deathdate': None},
            '3': {'birthdate': '01 JAN 2010', 'deathdate': None},
            '4': {'birthdate': '01 JAN 2015', 'deathdate': None}
        }
        families = {
            'F1': {'WIFE': 'I1', 'HUSB': 'I2', 'CHIL': ['I3', 'I4']}
        }

        result = TestUS12.US12(families, individuals)

        self.assertEqual(result, ['F1'])

    def test_father_too_old(self):
        individuals = {
            '1': {'birthdate': '01 JAN 1850', 'deathdate': None},
            '2': {'birthdate': '01 JAN 1980', 'deathdate': None},
            '3': {'birthdate': '01 JAN 2010', 'deathdate': None},
            '4': {'birthdate': '01 JAN 2015', 'deathdate': None}
        }
        families = {
            'F1': {'HUSB': 'I1', 'WIFE': 'I2', 'CHIL': ['I3', 'I4']}
        }

        result = TestUS12.US12(families, individuals)

        self.assertEqual(result, ['F1'])

    def test_both_parents_too_old(self):
        individuals = {
            '1': {'birthdate': '01 JAN 1840', 'deathdate': None},
            '2': {'birthdate': '01 JAN 1850', 'deathdate': None},
            '3': {'birthdate': '01 JAN 2010', 'deathdate': None},
            '4': {'birthdate': '01 JAN 2015', 'deathdate': None}
        }
        families = {
            'F1': {'WIFE': 'I1', 'HUSB': 'I2', 'CHIL': ['I3', 'I4']}
        }

        result = TestUS12.US12(families, individuals)

        self.assertEqual(result, ['F1'])

if __name__ == '__main__':
    unittest.main()
