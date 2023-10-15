import sys
import os
from datetime import * 
sys.path.append(os.path.join(sys.path[0], '..'))
import script

# Dhihan Ahmed
# helper function used for US42: checks if date is legitmate or not
def date_checker(date_str):
    try:
        datetime.strptime(date_str, "%d %b %Y")
        return True
    except ValueError:
        return False

# Dhihan Ahmed
# US28: List siblings in families by decreasing age, i.e. oldest siblings first: WORKING
def US28(individuals, families):
    print("US28 - List siblings in families by decreasing age (i.e. oldest siblings first) BELOW:")
    # iterating through families
    for fam_id in sorted(families.keys()):
        fam = families[fam_id]

        children = ' '.join(fam['CHIL']) # getting the children and storing it into children string

        # it this family has no children
        if (len(children) == 0):
            print(f"{fam_id} has no children.")
            continue

        children = children.replace("I", "") # getting rid of the I in the children IDs in families
        children = children.split() # putting the ID's in the string into an array

        ages_dict = {} # dictionary to store individual IDs as keys and their respective age as the value
        age = 0 # age variable

        # iteraing over children array
        for indi_id in children:
            # iterating over script individuals IDs
            for indi in individuals:
                # if children ID and individual ID match
                if indi == indi_id:
                    # get the age
                    age = script.calculate_age(individuals[indi]['birthdate'])
                    # store the ID and respective age into dictionary
                    ages_dict[indi_id] = age
                    # print(f"ID: {indi}, Age: {age}")
        
        sorted_items = sorted(ages_dict.items(), key=lambda item: item[1], reverse=True) # sorting the items (age) in descending order
        sorted_values = [(key, value) for key, value in sorted_items] # creating an array where each element is a tuple of the respective ID and sorted age 
        
        # printing the info
        print(f"{fam_id}'s children listed in decreasing age order: ", end="")
        for (key, value) in sorted_values:
            print(f"| I{key}, Age: {value} | ", end="")
        print("")

# Dhihan Ahmed
# US42: All dates should be legitimate dates for the months specified: WORKING
def US42(individuals, families):
    # iterating over individual IDs to check birthdays and deathdates
    for indi in individuals:
        birthdate_str = individuals[indi]['birthdate'] # getting birthdate
        if birthdate_str != "NA":
            # checking if birthdate is legitimate
            if not date_checker(birthdate_str):
                print(f"ERROR: INDIVIDUAL: US42: I{indi}: Birthday {birthdate_str} is not a legitimate date.")

        deathdate_str = individuals[indi]['deathdate'] # getting deathdate
        # checking if deathdate is legitimate
        if deathdate_str != "NA":
            if not date_checker(deathdate_str):
                print(f"ERROR: INDIVIDUAL: US42: I{indi}: Death date {deathdate_str} is not a legitimate date.")

    # iterating over family IDs to check marriage dates
    for fam_id in sorted(families.keys()):
        fam = families[fam_id]
        marr_date = "N/A" if 'MARR' not in fam else fam['MARR'] # getting marriage date

        if marr_date != "N/A":
            # checking if marriage date is legitimate
            if not date_checker(marr_date):
                print(f"ERROR: FAMILY: US42: {fam_id}: Marriage date {marr_date} is not a legitimate date.")

def sprint2():
    # call your US## here:
    script.parse() # DO NOT DELETE

    # TODO:
    # both US work, you just cant run both at the same time because an illegitimate date is needed in sprint2_test.ged for US42 to
    # show up, but simutaneously an illegitimate date throws a wrench in US28 causing the output to error out and not function
    
    # to test out each US code on your own:
    # - make sure there are NO illegitimate dates in sprint2_test.ged when running US28
    # - make sure there ARE illegitimate dates in sprint2_test.ged when running US42
    US28(script.individuals, script.families)
    US42(script.individuals, script.families)



sprint2()


                

