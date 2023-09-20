'''
Jesal Gandhi
Professor Ens
I pledge my honor that I have abided by the Stevens Honor System.
M2.B3: Assignment: Project 2 - GEDCOM data
'''

supported_tags = [
    'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 
    'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE'
]
exceptional_tags = ['INDI', 'FAM']

# print formatted lines to terminal for each line in .gedcom file
def print_line(level_num, tag_id, valid_val, args):
    concatArgs = ' '.join(args)
    print(f"--> {level_num} {tag_id} {concatArgs}")
    print(f"<-- {level_num}|{tag_id}|{valid_val}|{concatArgs}")

# parse thru each line, then each word, of the file
def parse():
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
        
        # call print_line for each line successfully parsed
        print_line(level, tag, valid, arguments)


def main():
    parse()

main()