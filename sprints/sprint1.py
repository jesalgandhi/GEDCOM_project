import sys
import os
from datetime import * 
sys.path.append(os.path.join(sys.path[0], '..'))
import script
import logging

# start code; families and individuals should be accessible now; test:
# print(script.families)
# print(script.individuals)


# Jesal Gandhi
# USO3: Birth before death: WORKING
def US03(individuals):
    for k in individuals:
        # print(individuals[k]['deathdate'])
        deathdate_str = individuals[k]['deathdate']
        birthdate_str = individuals[k]['birthdate']
        if deathdate_str != 'NA' and birthdate_str != 'NA':
            death = datetime.strptime(deathdate_str, "%d %b %Y")
            birth = datetime.strptime(birthdate_str, "%d %b %Y")
            error_msg = ""
            if birth > death:
                error_msg = f"ERROR: INDIVIDUAL: US03: I{k}: Birthday {birthdate_str} occurs after death date {deathdate_str}"
                print(error_msg)
                logging.error(error_msg)
                return error_msg
                # print(f"ERROR: INDIVIDUAL: US03: I{k}: Birthday {birthdate_str} occurs after death date {deathdate_str}")
            else:
                logging.error(error_msg)
                return None

# Jesal Gandhi
# US14: Multiple births <= 5
def US14(individuals, families):
    # print(individuals)
    # print(families)
    for k in families:
        children = families[k]['CHIL']
        if len(children) >= 5:
            for i in range(len(children)):
                mutliple_births = 1
                same_date = ""
                for j in range(i+1, len(children)):
                    same_date = individuals[children[i][1:]]['birthdate']
                    if datetime.strptime(individuals[children[i][1:]]['birthdate'], "%d %b %Y") == datetime.strptime(individuals[children[j][1:]]['birthdate'], "%d %b %Y"):
                        mutliple_births += 1
                if mutliple_births >= 5:
                    print(f"ERROR: FAMILY: US14: {k}: There are 5 or more individuals born on the same date {same_date} in this family")


# Dhihan Ahmed
# US05: Marriage before death: WORKING
# modified line 272 of sprint1_test.ged to test US05. changed the line from: 
# {2 DATE 10 MAY 1968} -> {2 DATE 10 MAY 2968}
def US05(individuals, families):

    for fam_id in sorted(families.keys()):
        fam = families[fam_id]
        wife_name, husb_name = "Unknown", "Unknown"
        if 'HUSB' in fam:
            husb_name = individuals.get(fam['HUSB'][1:]).get("name", "Unknown")
        if 'WIFE' in fam:
            wife_name = individuals.get(fam['WIFE'][1:]).get("name", "Unknown")

        husb_id = "N/A" if 'HUSB' not in fam else fam['HUSB']
        wife_id = "N/A" if 'WIFE' not in fam else fam['WIFE']

        marriage_date = "N/A" if 'MARR' not in fam else fam['MARR']

        if marriage_date != 'N/A':
            husb_deathdate = ""
            wife_deathdate = ""
            for id in sorted(individuals.keys()):
                indi = individuals[id]
                if indi['name'] == husb_name:
                    husb_deathdate = indi['deathdate']
                if indi['name'] == wife_name:
                    wife_deathdate = indi['deathdate']

            if husb_deathdate != 'NA':
                marriage = datetime.strptime(marriage_date, "%d %b %Y")
                death = datetime.strptime(husb_deathdate, "%d %b %Y")
                if marriage > death:
                    print(f"ERROR: INDIVIDUAL: US05: {husb_id}: Marriage date {marriage_date} occurs after death date {husb_deathdate}")

            if wife_deathdate != 'NA':
                marriage = datetime.strptime(marriage_date, "%d %b %Y")
                death = datetime.strptime(wife_deathdate, "%d %b %Y")
                if marriage > death:
                    print(f"ERROR: INDIVIDUAL: US05: {wife_id}: Marriage date {marriage_date} occurs after death date {wife_deathdate}")


# Dhihan Ahmed
# US02: Birth before marriage: WORKING
# modified line 299 of sprint1_test.ged to test US02. changed the line from: 
# {2 DATE 1 JUL 1993} -> {2 DATE 1 JUL 1893}
def US02(individuals, families):
    for fam_id in sorted(families.keys()):
        fam = families[fam_id]
        wife_name, husb_name = "Unknown", "Unknown"
        if 'HUSB' in fam:
            husb_name = individuals.get(fam['HUSB'][1:]).get("name", "Unknown")
        if 'WIFE' in fam:
            wife_name = individuals.get(fam['WIFE'][1:]).get("name", "Unknown")

        husb_id = "N/A" if 'HUSB' not in fam else fam['HUSB']
        wife_id = "N/A" if 'WIFE' not in fam else fam['WIFE']

        marriage_date = "N/A" if 'MARR' not in fam else fam['MARR']

        if marriage_date != 'N/A':
            husb_birthdate = ""
            wife_birthdate = ""
            for id in sorted(individuals.keys()):
                indi = individuals[id]
                if indi['name'] == husb_name:
                    husb_birthdate = indi['birthdate']
                if indi['name'] == wife_name:
                    wife_birthdate = indi['birthdate']

            marriage = datetime.strptime(marriage_date, "%d %b %Y")
            husb_birth = datetime.strptime(husb_birthdate, "%d %b %Y")
            wife_birth = datetime.strptime(wife_birthdate, "%d %b %Y")

            if husb_birth > marriage:
                print(f"ERROR: INDIVIDUAL: US02: {husb_id}: Birth date {husb_birthdate} occurs after marriage date {marriage_date}")

            if wife_birth > marriage:
                print(f"ERROR: INDIVIDUAL: US02: {wife_id}: Birth date {wife_birthdate} occurs after marriage date {marriage_date}")


# Ajit Kandasamy
# US23: Unique name and birth date: WORKING
def US23(individuals):
    names = {}
    for indi in individuals:
        name = individuals[indi]["name"]
        birthdate = individuals[indi]["birthdate"]
        if name in names and names[name] == birthdate:
            print(f"ERROR: INDIVIDUAL: US23: I{indi}: there already exists a person with name: {name} and birthday: {birthdate}")
        names[name] = birthdate


# Ajit Kandasamy
# US07: Less then 150 years old: WORKING
def US07(individuals):
    for indi in individuals:
        name = individuals[indi]["name"]
        birthdate = individuals[indi]["birthdate"]
        if script.calculate_age(birthdate) >= 150:
            print(f"ERROR: INDIVIDUAL: US07: I{indi}: {name} is 150 years old or older, that is not allowed.")


def sprint1():
    # call your US## here:
    script.parse() # DO NOT DELETE
    US03(script.individuals)
    US14(script.individuals, script.families)
    US05(script.individuals, script.families)
    US02(script.individuals, script.families)
    US23(script.individuals)
    US07(script.individuals)


sprint1()
