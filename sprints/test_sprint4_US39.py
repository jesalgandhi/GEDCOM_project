import unittest
from datetime import datetime, timedelta

class TestUS39(unittest.TestCase):

    # Calculate age of individual
    def calculate_age(birthdate):
        if birthdate:
            today = datetime.today()
            birth_date = datetime.strptime(birthdate, "%d %b %Y")
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            return age
        return 'NA'

    def remaining_days_until_anniversary(anniversary_date_str):
        anniversary_date = datetime.strptime(anniversary_date_str, '%d %b %Y')
        today = datetime.now()
        anniversary_date_current_year = datetime(today.year, anniversary_date.month, anniversary_date.day)

        if today <= anniversary_date_current_year:
            remaining_days = (anniversary_date_current_year - today).days
        else:
            next_anniversary_date = datetime(today.year + 1, anniversary_date.month, anniversary_date.day)
            remaining_days = (next_anniversary_date - today).days

        return remaining_days

    def US39(families):
        upcoming_anniversaries = []
        for fam in families:
            if 'MARR' in families[fam] and 'DIV' not in families[fam]:
                days_remaining = TestUS39.remaining_days_until_anniversary(families[fam]['MARR'])
                if days_remaining < 30:
                    upcoming_anniversaries.append(fam)
                    print(f"UPCOMING ANNIVERSARY: INDIVIDUAL: US39: family {fam} has an anniversary coming up in {days_remaining} days")
        return upcoming_anniversaries

    def test_no_upcoming_anniversaries(self):
        families = {
            'F1': {'MARR': '01 JAN 2023'}
        }

        result = TestUS39.US39(families)

        self.assertEqual(result, [])

    def test_upcoming_anniversary_within_30_days(self):
        today = datetime.now()
        anniversary_date = today + timedelta(days=15)
        anniversary_date_str = anniversary_date.strftime('%d %b %Y')

        families = {
            'F1': {'MARR': anniversary_date_str}
        }

        result = TestUS39.US39(families)

        self.assertEqual(result, ['F1'])

    def test_upcoming_anniversary_more_than_30_days(self):
        today = datetime.now()
        anniversary_date = today + timedelta(days=40)
        anniversary_date_str = anniversary_date.strftime('%d %b %Y')

        families = {
            'F1': {'MARR': anniversary_date_str}
        }

        result = TestUS39.US39(families)

        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
