import sys
import os
from datetime import * 
sys.path.append(os.path.join(sys.path[0], '..'))
import script
import logging

def time_passed(deathdate):
    if deathdate:
        today = datetime.today()
        death_date = datetime.strptime(deathdate, "%d %b %Y")
        return (today - death_date).days
    return 'NA'

#Ajit Kandasamy
#recent births
def US35(individuals):
    recent_births = []
    for indi in individuals:
        obj = individuals[indi]
        if time_passed(obj["birthdate"]) < 30:
            recent_births += [indi]
            print(f"RECENT BIRTH: INDIVIDUAL: US35: I{indi}: Individual {obj['name']} was born on {obj['birthdate']}") 
    return recent_births if recent_births != [] else None

#Ajit Kandasamy
# List couples with large age differences  
def US34(individuals, families):
    large_differences = []
    for fam in families:
        if 'WIFE' in families[fam] and 'HUSB' in families[fam]:
            wife_id = families[fam]['WIFE'][1:]
            wife_birth = individuals[wife_id]['birthdate']
            husb_id = families[fam]['HUSB'][1:]
            husb_birth = individuals[husb_id]['birthdate']
            if script.calculate_age(husb_birth)*2 <= script.calculate_age(wife_birth) or script.calculate_age(wife_birth)*2 <= script.calculate_age(husb_birth):
                large_differences += [fam]
                print(f"LARGE AGE DIFFERENCE: FAMILY: US10: {fam}: Both husband and wife have a large age difference")
    return large_differences

# Jesal Gandhi
# Male last names  
def US16(individuals, families):
    for fam in families:
        husb = families[fam]['HUSB']
        temp = individuals[husb[1:]]['name']
        temp2 = temp.split("/")
        lastName = temp2[1]
        for child in families[fam]['CHIL']:
            key = child[1:]
            indiChild = individuals[key]
            temp2 = indiChild['name'].split("/")
            if indiChild['sex'] == 'M' and temp2[1] != lastName:
                print(f"MALE LAST NAMES: FAMILY: US16: {fam}: {indiChild['name']} does not have the same last name as the rest of his family")

# Jesal Gandhi
# List upcoming birthdays  
def US38(individuals):
    today = datetime.now()
    thirty_days = timedelta(days=30)
    for k in individuals:
        birthdate_str = individuals[k]['birthdate']
        name = individuals[k]['name']
        birth = datetime.strptime(birthdate_str, "%d %b %Y")
        birth_month_day = (birth.month, birth.day)
        today_month_day = (today.month, today.day)
        difference = (datetime(today.year, *birth_month_day) - today).days
        if 0 <= difference <= 30:
            print(f"UPCOMING BIRTHDAY: INDIVIDUAL: US38: {k}: {name}'s birthday is on {birthdate_str}")

# Dhihan Ahmed
# Fewer than 15 siblings
def US15(families):
    # iterating over family IDs to check # of children
    for fam_id in sorted(families.keys()):
        fam = families[fam_id]
        children_list = fam['CHIL']
        # print(children_list)
        if len(children_list) >= 15:
            print(f"OVER 15 SIBLINGS: FAMILY: US15: {fam_id} has 15 or more siblings.")

# Dhihan Ahmed
# Correct gender for each role
def US21(individuals, families):
    # iterating over family IDs to check husband/wife IDs
    for fam_id in sorted(families.keys()):
        fam = families[fam_id]

        husb_id = "N/A" if 'HUSB' not in fam else fam['HUSB']
        wife_id = "N/A" if 'WIFE' not in fam else fam['WIFE']

        if husb_id != "N/A" and wife_id != "N/A":
            for indi in individuals:
                # print(indi)
                # print(husb_id)
                # break
                if "I"+indi == husb_id:
                    if individuals[indi]['sex'] != 'M':
                        print(f"CORRECT GENDER FOR EACH ROLE: FAMILY: US21: Husband {husb_id} {individuals[indi]['name']} is not a male.") 
                if "I"+indi == wife_id:
                    if individuals[indi]['sex'] != 'F':
                        print(f"CORRECT GENDER FOR EACH ROLE: FAMILY: US21: Wife {wife_id} {individuals[indi]['name']} is not a female.") 

def sprint3():
    # call your US## here:
    script.parse() # DO NOT DELETE

    US35(script.individuals)
    US34(script.individuals, script.families)
    US38(script.individuals)
    US16(script.individuals, script.families)

    US15(script.families)
    US21(script.individuals, script.families)


sprint3()