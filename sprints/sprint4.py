import sys
import os
from datetime import * 
sys.path.append(os.path.join(sys.path[0], '..'))
import script
import logging

# Ajit Kandasamy
# checks if parents are too old
def US12(families, individuals):
    too_old = []
    for fam in families:
    
        if 'CHIL' not in families[fam] or families[fam]['CHIL'] == []:
            continue

        youngest = min(script.calculate_age(individuals[chil[1:]]['birthdate']) for chil in families[fam]['CHIL'])


        if 'WIFE' in families[fam]:
            wife_id = families[fam]['WIFE'][1:]
            wife_birth = individuals[wife_id]['birthdate']
            wife_age = script.calculate_age(wife_birth)
            if wife_age >= youngest+80:
                too_old += [fam]
                print(f"ERROR: FAMILY: US12: {fam}: at least one of the parents is too old")
                continue
        
        if 'HUSB' in families[fam]:
            husb_id = families[fam]['HUSB'][1:]
            husb_birth = individuals[husb_id]['birthdate']
            husb_age = script.calculate_age(husb_birth)
            if husb_age >= youngest+100:
                too_old += [fam]
                print(f"ERROR: FAMILY: US12: {fam}: at least one of the parents is too old")
    return too_old

def remaining_days_until_anniversary(aniversary_date_str):
    anniversary_date = datetime.strptime(aniversary_date_str, '%d %b %Y')
    today = datetime.now()
    anniversary_date_current_year = datetime(today.year, anniversary_date.month, anniversary_date.day)
    


    if today <= anniversary_date_current_year:
        remaining_days = (anniversary_date_current_year - today).days
    else:
        next_anniversary_date = datetime(today.year + 1, anniversary_date.month, anniversary_date.day)
        remaining_days = (next_anniversary_date - today).days

    return remaining_days

# Ajit Kandasamy
# checks if there are less than 1 words
def US39(families):
    upcoming_aniversaries = []
    for fam in families:
        if 'MARR' in families[fam] and 'DIV' not in families[fam]:
            days_remaining = remaining_days_until_anniversary(families[fam]['MARR'])
            if days_remaining < 30:
                upcoming_aniversaries += [fam]
                print(f"UPCOMING ANIVERSARY: INDIVIDUAL: US39: family {fam} has aniversary coming up in {days_remaining} days")
    return upcoming_aniversaries

def sprint4():
    # call your US## here:
    script.parse() # DO NOT DELETE
    US12(script.families, script.individuals)
    US39(script.families)



sprint4()