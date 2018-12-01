with open('input.txt') as inputfile:
        changes = list(map(int, inputfile.readlines()))

print(changes)

#---P1
current_frequency=0

for change in changes:
        current_frequency += change
print(current_frequency)
#----P2


