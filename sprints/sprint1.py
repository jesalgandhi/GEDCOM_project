import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))
import script
script.parse() # DO NOT DELETE

# start code; families and individuals should be accessible now; test:
print(script.families)
print(script.individuals)

for k in script.individuals:
    print(script.individuals[k])

# Jesal Gandhi Sprint1
# USO3: Birth before death
def US03():
    pass

# US14: Multiple births <= 5
def US14():
    pass

