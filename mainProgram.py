import os
import timeit
from inputStringHandler import createInputStrings
from basicStringAligner import alignStrings
from advancedStringAligner import alignStringsAdvanced
from consts import inputFile, outputFile
# Create the input strings according to definition
timeStart = timeit.default_timer()
inputStringA, inputStringB = createInputStrings(os.path.join(os.getcwd(),inputFile))

# Align the two strings using basic DP algorithm
timeBasicBefore = timeit.default_timer()
basicAlignedA, basicAlignedB, memoryTakenBasic = alignStrings(inputStringA, inputStringB)
timeBasicAfter = timeit.default_timer()
timeTakenBasic = timeBasicAfter - timeBasicBefore

# Align the two strings using memory-efficient DP algorithm
timeAdvancedBefore = timeit.default_timer()
memoryTakenAdvanced = 0
advancedAlignedA, advancedAlignedB = alignStringsAdvanced(inputStringA, inputStringB)
timeAdvancedAfter = timeit.default_timer()
timeTakenAdvanced = timeAdvancedAfter - timeAdvancedBefore

# Write ouptut and details to file
timeTotal = timeAdvancedAfter - timeStart
memoryTotal = memoryTakenBasic + memoryTakenAdvanced

if(len(basicAlignedA)>100):
    basicAlignedA = basicAlignedA[0:50]+"*"+basicAlignedA[-50:]
    basicAlignedB = basicAlignedB[0:50]+"*"+basicAlignedB[-50:]

with open(os.path.join(os.getcwd(),outputFile), 'w') as output:
    output.write(basicAlignedA+"\n")
    output.write(basicAlignedB+"\n")
    output.write("Total time taken: "+str(timeTotal)+" (s) \n")
    output.write("Total memory allocated: "+str(memoryTotal/2**20)+" MB \n")
