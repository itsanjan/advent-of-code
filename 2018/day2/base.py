with open('input.txt') as inputfile:
        boxIDs = list(map(str, inputfile.readlines()))
OutputList=[]
i2=0
i3=0
v2IsNotSet=False
v3IsNotSet=False
for id in boxIDs:
##	for letterIndex in id:
##                i=0
##                for matchCursor in id:
##                        if letterIndex == matchCursor:
##                                i+=1
##                if i>1:
##                        print(id,i)
##                        OutputList.append(i)

        for letterIndex in id:
                for matchCursor in id:
                        print("id",id)
                        print("mtchcrsr",matchCursor)
                        for currentLetter in list(set(id)):
                                i2=0
                                if (id.count(currentLetter) == 2) and ~(v2IsNotSet):
                                        i2 +=1
                                        print(currentLetter,i2)
                                        v2IsNotSet=True
                                if (id.count(currentLetter) == 3) and ~(v3IsNotSet):
                                        i3 +=1
                                        v3IsNotSet=True
                print(id,i2,i3)
                quit()
print(i2,i3,i2*i3)                        
