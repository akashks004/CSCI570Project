import os

#Variables
baseStringA = ""
baseStringB = ""
indexesA = []
indexesB = []

#open the input file in read mode
with open(os.getcwd()+'\input.txt', 'r') as f:
    for item in f:
        item = item.rstrip() #removing the \n at end of each line
        if(item.isdigit()):
            if(baseStringB == ""):
                indexesA.append(int(item))
            else:
                indexesB.append(int(item))
        else:
            if(baseStringA == ""):
                baseStringA = item
            else:
                baseStringB = item

baseStringALength = len(baseStringA)
baseStringBLength = len(baseStringB)

for i in indexesA:
    baseStringA = baseStringA[:i+1] + baseStringA + baseStringA[i+1:]

for i in indexesB:
    baseStringB = baseStringB[:i+1] + baseStringB + baseStringB[i+1:]

#Checking if the length of the first and the second string to be 2^j*str1.length and 2^k*str2.length.
assert len(baseStringA) == ((2**(len(indexesA)))*baseStringALength)
assert len(baseStringB) == ((2**(len(indexesB)))*baseStringBLength)

#closing the input file
f.close()
print(baseStringA)
print(indexesA)
print(baseStringB)
print(indexesB)

        