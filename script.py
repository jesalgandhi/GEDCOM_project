'''
Jesal Gandhi, Dhihan Ahmed, Ajit Kandasamy
Professor Ensx
I pledge my honor that I have abided by the Stevens Honor System.
M2.B3: Assignment: Project 2 - GEDCOM data
'''
import collections
from datetime import * 
from prettytable import PrettyTable
import sys
import subprocess


individuals_table = PrettyTable()
individuals_table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]

families_table = PrettyTable()
families_table.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]

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
        if indi['birthdate'] != None:
            indi['deathdate'] = value
        else:
            indi['birthdate'] = value
    elif tag == 'DEAT':
        indi['alive'] = False
        # indi['deathdate'] = value
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
    # print("Individuals:")
    # print(f"{'ID':<5}{'Name':<25}{'Gender':<10}{'Birthday':<15}{'Age':<6}{'Alive':<6}{'Death':<6}{'Child':<6}{'Spouse':<6}")
    for indi_id in sortedDict:
        indi = individuals[indi_id]
        age = calculate_age(indi['birthdate'])
        # if indi['birthdate'] == None:
            # indi['birthdate'] = 'error'
        # print(f"I{indi_id:<5}{indi['name']:<25}{indi['sex']:<10}{indi['birthdate']:<15}{age:<6}{indi['alive']}{' ' * 4}{indi['deathdate']:<6}{indi['child']:<6}{indi['spouse']:<6}")
        individuals_table.add_row(["I"+indi_id, indi['name'], indi['sex'], indi['birthdate'], age, indi['alive'], indi['deathdate'], indi['child'], indi['spouse']])

    print("Individuals:")
    print(individuals_table)

# print information about families
def print_families():
    # print("Families:")
    # print(f"{'ID':<5}{'Married':<15}{'Divorced':<15}{'Husband ID':<13}{'Husband Name':<30}{'Wife ID':<13}{'Wife Name':<30}{'Children':<15}")
    for fam_id in sorted(families.keys()):
        fam = families[fam_id]
        wife_name, husb_name = "Unknown", "Unknown"
        if 'HUSB' in fam:
            husb_name = individuals.get(fam['HUSB'][1:]).get("name", "Unknown")
        if 'WIFE' in fam:
            wife_name = individuals.get(fam['WIFE'][1:]).get("name", "Unknown")
        husb_id = "N/A" if 'HUSB' not in fam else fam['HUSB']
        wife_id = "N/A" if 'WIFE' not in fam else fam['WIFE']
        marr_date = "N/A" if 'MARR' not in fam else fam['MARR']
        div_date = "N/A" if 'DIV' not in fam else fam['DIV']
        # print(f"{fam_id:<5}{marr_date:<15}{div_date:<15}{husb_id:<13}{husb_name:<30}{wife_id:<13}{wife_name:<30}{', '.join(fam['CHIL']):<15}")
        children = ', '.join(fam['CHIL'])
        if len(children):
            families_table.add_row([fam_id, marr_date, div_date, husb_id, husb_name, wife_id, wife_name, children])
        else:
            families_table.add_row([fam_id, marr_date, div_date, husb_id, husb_name, wife_id, wife_name, "NA"])
    print("Families:")
    print(families_table)



# parse thru each line, then each word, of the file
def parse():
    # These variables are used to populate the individual/family collections
    current_individual = None  # Initialize current_individual
    current_family = {'CHIL': []}       # Initialize current_family
    
    # populate gedContent as a list of all lines from file
    gedContent = None

    # make sure a gedcome file is inputted
    if len(sys.argv) != 2 or sys.argv[1][-3:] != "ged":
        raise Exception("Sorry, can only input gedcom file as command line input")

    file = sys.argv[1]
    with open(file, "r") as ged:
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
            if 'FAM' in current_family:
                families[current_family['FAM']] = current_family
                current_family = {'CHIL': []}
            current_family[tag] = arguments[0].replace("@", "")
        elif tag in ['HUSB', 'WIFE']:
            current_family[tag] = arguments[0].replace("@", "")
        elif tag in ['MARR', 'DIV']:
            current_family[tag] = "empty"
        elif tag == 'DATE':
            if 'MARR' in current_family and current_family['MARR'] == "empty":
                current_family['MARR'] = (" ".join(arguments))
            elif 'DIV' in current_family and current_family['DIV'] == "empty":
                current_family['DIV'] = (" ".join(arguments))
            # checking if indi_id is None or not. if it is NONE, it means it is unitialized and we ignore it.
            else:
                if current_individual:
                    update_individual(current_individual, tag, (" ".join(arguments)).replace("@", ""))
        elif tag == 'CHIL':
            current_family[tag].append(arguments[0].replace("@", ""))
        elif tag in ['NAME', 'SEX', 'DEAT', 'FAMC', 'FAMS']:
            if current_individual:
                update_individual(current_individual, tag, (" ".join(arguments)).replace("@", ""))
        
    if "FAM" in current_family:
        families[current_family['FAM']] = current_family

        
        # OLD VERSION:
        # call print_line for each line successfully parsed
        # print_line(level, tag, valid, arguments)



def main():
    parse()

    print_individuals()

    # print(families.keys()) # checking the keys to ensure they got added to the dictionary
    # print(families.items()) # checking the items to ensure they got added to the dictionary
    
    print_families()
    


if __name__ == "__main__":
    main()
    subprocess.run(["python", "./sprints/sprint1.py", sys.argv[1]])