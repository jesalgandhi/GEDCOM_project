'''
Jesal Gandhi, Dhihan Ahmed, Ajit Kandasamy
Professor Ens
I pledge my honor that I have abided by the Stevens Honor System.
M2.B3: Assignment: Project 2 - GEDCOM data
'''
import collections
from datetime import * 

supported_tags = [
    'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 
    'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE'
]

exceptional_tags = ['INDI', 'FAM']

individuals = {}  # Dictionary to store information about individuals
families = {}    # Dictionary to store information about families

current_individual = None  # Variable to keep track of the current individual being processed
current_family = None       # Variable to keep track of the current family being processed

# add an individual to the individuals dictionary
def add_individual(indi_id):
    individuals[indi_id] = {'name': 'NA', 'sex': None, 'birthdate': None, 'alive': True, 'deathdate': 'NA', 'child': 'NA', 'spouse': 'NA'}


# update individual information
def update_individual(indi_id, tag, value):
    indi = individuals[indi_id]    
    if tag == 'NAME':
        indi['name'] = value
    elif tag == 'SEX':
        indi['sex'] = value
    elif tag == 'DATE':
        indi['birthdate'] = value
    elif tag == 'DEAT':
        indi['alive'] = False
        indi['deathdate'] = value
    elif tag == 'FAMC':
        indi['child'] = value
    elif tag == 'FAMS':
        indi['spouse'] = value

# # calculate age of individual 
def calculate_age(birthdate):
    if birthdate:
        today = datetime.today()
        birth_date = datetime.strptime(birthdate, "%d %b %Y")
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
    return 'NA'

# print information about individuals
def print_individuals():
    sortedDict = collections.OrderedDict(sorted(individuals.items(), key=lambda x: int(x[0])))
    print("Individuals:")
    print(f"{'ID':<5}{'Name':<25}{'Gender':<10}{'Birthday':<15}{'Age':<6}{'Alive':<6}{'Death':<6}{'Child':<6}{'Spouse':<6}")
    for indi_id in sortedDict:
        indi = individuals[indi_id]
        age = calculate_age(indi['birthdate'])
        print(f"I{indi_id:<5}{indi['name']:<25}{indi['sex']:<10}{indi['birthdate']:<15}{age:<6}{indi['alive']}{' ' * 4}{indi['deathdate']:<6}{indi['child']:<6}{indi['spouse']:<6}")


# print information about families
def print_families():
    print("Families:")
    for fam_id in sorted(families.keys()):
        fam = families[fam_id]
        husband_name = individuals.get(fam['husband_id'], {}).get('name', 'Unknown')
        wife_name = individuals.get(fam['wife_id'], {}).get('name', 'Unknown')
        print(f"ID: {fam_id}, Husband: {husband_name}, Wife: {wife_name}")

# OLD VERSION:
# print formatted lines to terminal for each line in .gedcom file
# def print_line(level_num, tag_id, valid_val, args):
#     concatArgs = ' '.join(args)
#     print(f"--> {level_num} {tag_id} {concatArgs}")
#     print(f"<-- {level_num}|{tag_id}|{valid_val}|{concatArgs}")

# parse thru each line, then each word, of the file
def parse():
    # These variables are used to populate the individual/family collections
    current_individual = None  # Initialize current_individual
    current_family = None       # Initialize current_family
    
    # populate gedContent as a list of all lines from file
    gedContent = None
    with open("test_file.ged", "r") as ged:
        gedContent = [line.strip() for line in ged]

    # loop through arguments for each line
    for line in gedContent:
        # split the line into individual attributes
        attributes = line.split(" ")
        lenAttributes = len(attributes)

        # create variables for each attribute
        level = attributes[0]
        tag = None
        arguments = None
        valid = None

        # poplate variables created above, accounting for exceptional cases
        if lenAttributes >= 3 and attributes[2] in exceptional_tags:
            tag, arguments, valid = attributes[2], [attributes[1]], "Y"
        else:
            tag = attributes[1]
            valid = "Y" if tag in supported_tags else "N"
            if lenAttributes >= 3:
                arguments = attributes[2:]
            else:
                arguments = ""

        
        
        # Process individual and family information
        if tag == 'INDI':
            current_individual = arguments[0].replace("@", "").replace("I", "")
            add_individual(current_individual)
        elif tag == 'FAM':
            current_family = arguments[0]
        elif tag in ['NAME', 'SEX', 'DATE', 'DEAT', 'FAMC', 'FAMS']:
            if current_individual:
                update_individual(current_individual, tag, (" ".join(arguments)).replace("@", ""))

        
        # OLD VERSION:
        # call print_line for each line successfully parsed
        # print_line(level, tag, valid, arguments)


def main():
    parse()
    print_individuals()
    print_families()

main()