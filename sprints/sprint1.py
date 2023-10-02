import sys
import os
from datetime import * 
sys.path.append(os.path.join(sys.path[0], '..'))
import script
script.parse() # DO NOT DELETE

# start code; families and individuals should be accessible now; test:
# print(script.families)
# print(script.individuals)


def sprint1():
    # Jesal Gandhi
    # USO3: Birth before death: WORKING
    def US03():
        for k in script.individuals:
            # print(script.individuals[k]['deathdate'])
            deathdate_str = script.individuals[k]['deathdate']
            birthdate_str = script.individuals[k]['birthdate']
            if deathdate_str != 'NA':
                death = datetime.strptime(deathdate_str, "%d %b %Y")
                birth = datetime.strptime(birthdate_str, "%d %b %Y")
                if birth > death:
                    print(f"ERROR: INDIVIDUAL: US03: I{k}: Birthday {birthdate_str} occurs after death date {deathdate_str}")

    # Jesal Gandhi
    # US14: Multiple births <= 5
    def US14():
        # print(script.individuals)
        # print(script.families)
        for k in script.families:
            children = script.families[k]['CHIL']
            if len(children) >= 5:
                for i in range(len(children)):
                    mutliple_births = 1
                    same_date = ""
                    for j in range(i+1, len(children)):
                        same_date = script.individuals[children[i][1:]]['birthdate']
                        if datetime.strptime(script.individuals[children[i][1:]]['birthdate'], "%d %b %Y") == datetime.strptime(script.individuals[children[j][1:]]['birthdate'], "%d %b %Y"):
                            mutliple_births += 1
                    if mutliple_births >= 5:
                        print(f"ERROR: FAMILY: US14: {k}: There are 5 or more individuals born on the same date {same_date} in this family")

    # Dhihan Ahmed
    # US05: Marriage before death: WORKING
    # modified line 272 of sprint1_test.ged to test US05. changed the line from: 
    # {2 DATE 10 MAY 1968} -> {2 DATE 10 MAY 2968}
    def US05():

        for fam_id in sorted(script.families.keys()):
            fam = script.families[fam_id]
            wife_name, husb_name = "Unknown", "Unknown"
            if 'HUSB' in fam:
                husb_name = script.individuals.get(fam['HUSB'][1:]).get("name", "Unknown")
            if 'WIFE' in fam:
                wife_name = script.individuals.get(fam['WIFE'][1:]).get("name", "Unknown")

            husb_id = "N/A" if 'HUSB' not in fam else fam['HUSB']
            wife_id = "N/A" if 'WIFE' not in fam else fam['WIFE']

            marriage_date = "N/A" if 'MARR' not in fam else fam['MARR']

            if marriage_date != 'N/A':
                husb_deathdate = ""
                wife_deathdate = ""
                for id in sorted(script.individuals.keys()):
                    indi = script.individuals[id]
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
    def US02():
        
        for fam_id in sorted(script.families.keys()):
            fam = script.families[fam_id]
            wife_name, husb_name = "Unknown", "Unknown"
            if 'HUSB' in fam:
                husb_name = script.individuals.get(fam['HUSB'][1:]).get("name", "Unknown")
            if 'WIFE' in fam:
                wife_name = script.individuals.get(fam['WIFE'][1:]).get("name", "Unknown")

            husb_id = "N/A" if 'HUSB' not in fam else fam['HUSB']
            wife_id = "N/A" if 'WIFE' not in fam else fam['WIFE']

            marriage_date = "N/A" if 'MARR' not in fam else fam['MARR']

            if marriage_date != 'N/A':
                husb_birthdate = ""
                wife_birthdate = ""
                for id in sorted(script.individuals.keys()):
                    indi = script.individuals[id]
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

    def US23():
        names = {}
        for indi in script.individuals:
            name = script.individuals[indi]["name"]
            birthdate = script.individuals[indi]["birthdate"]
            if name in names and names[name] == birthdate:
                print(f"ERROR: INDIVIDUAL: US23: I{indi}: there already exists a person with name: {name} and birthday: {birthdate}")
            names[name] = birthdate

    def US07():
        for indi in script.individuals:
            name = script.individuals[indi]["name"]
            birthdate = script.individuals[indi]["birthdate"]
            if script.calculate_age(birthdate) >= 150:
                print(f"ERROR: INDIVIDUAL: US07: I{indi}: {name} is 150 years old or older, that is not allowed.")

    # call your US## here:
    US03()
    US14()
    US05()
    US02()
    US23()
    US07()

sprint1()



