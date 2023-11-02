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

def sprint3():
    # call your US## here:
    script.parse() # DO NOT DELETE

    # TODO:
    # both US work, you just cant run both at the same time because an illegitimate date is needed in sprint2_test.ged for US42 to
    # show up, but simutaneously an illegitimate date throws a wrench in US28 causing the output to error out and not function
    
    # to test out each US code on your own:
    # - make sure there are NO illegitimate dates in sprint2_test.ged when running US28
    # - make sure there ARE illegitimate dates in sprint2_test.ged when running US42
    US35(script.individuals)
    US34(script.individuals, script.families)


sprint3()