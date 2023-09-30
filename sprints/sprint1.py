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

    # ...

    # call your US## here:
    US03()
    US14()

sprint1()



