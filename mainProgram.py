import os
from inputStringHandler import createInputStrings
from basicStringAligner import alignStrings
from advancedStringAligner import alignStringsAdvanced

# Input file
inputFile = "input.txt"

# Output file
outputFile = "output.txt"

# Create the input strings according to definition
inputStringA, inputStringB = createInputStrings(os.path.join(os.getcwd(),inputFile))

# Align the two strings using basic DP algorithm
timeTakenBasic = 0
memoryTakenBasic = 0
basicAlignedA, basicAlignedB = alignStrings(inputStringA, inputStringB)

# Align the two strings using memory-efficient DP algorithm
timeTakenAdvanced = 0
memoryTakenAdvanced = 0
advancedAlignedA, advancedAlignedB = alignStringsAdvanced(inputStringA, inputStringB)

# Write ouptut and details to file
timeTotal = timeTakenBasic + timeTakenAdvanced
memoryTotal = memoryTakenBasic + memoryTakenAdvanced

with open(os.path.join(os.getcwd(),outputFile), 'w') as output:
    output.write(basicAlignedA[0:50]+"*"+basicAlignedA[-50:]+"\n")
    output.write(basicAlignedB[0:50]+"*"+basicAlignedB[-50:]+"\n")
    output.write("Total time taken: "+str(timeTotal)+" (s) \n")
    output.write("Total memory allocated: "+str(memoryTotal)+" MB \n")
