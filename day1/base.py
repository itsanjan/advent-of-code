with open('input.txt') as inputfile:
        changes = list(map(int, inputfile.readlines()))

print(changes)

#---P1
current_frequency=0

for change in changes:
        current_frequency += change
print(current_frequency)
#----P2
change=0
observed=set()
current_frequency=0
while True:
    for change in changes:
         current_frequency +=int(change)
         if current_frequency in observed:
             print(current_frequency)
             quit()
         observed.add(current_frequency)

