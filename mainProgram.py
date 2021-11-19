import os
import timeit
from inputStringHandler import createInputStrings
from basicStringAligner import alignStrings
from advancedStringAligner import alignStringsAdvanced
from consts import inputFile, outputFile

# Create the input strings according to definition
timeStart = timeit.default_timer()
inputStringA, inputStringB = createInputStrings(os.path.join(os.getcwd(),inputFile))
print("String created")
print("A:"+str(len(inputStringA))+", B:"+str(len(inputStringB)))

# Align the two strings using basic DP algorithm
timeBasicBefore = timeit.default_timer()
basicAlignedA, basicAlignedB, memoryTakenBasic = alignStrings(inputStringA, inputStringB)
timeBasicAfter = timeit.default_timer()
timeTakenBasic = timeBasicAfter - timeBasicBefore
print("Basic DP done")

# Align the two strings using memory-efficient DP algorithm
timeAdvancedBefore = timeit.default_timer()
advancedAlignedA, advancedAlignedB, memoryTakenAdvanced = alignStringsAdvanced(inputStringA, inputStringB)
timeAdvancedAfter = timeit.default_timer()
timeTakenAdvanced = timeAdvancedAfter - timeAdvancedBefore
print("Advanced DP done")

# Write ouptut and details to file
timeTotal = timeAdvancedAfter - timeStart
memoryTotal = memoryTakenBasic + memoryTakenAdvanced

print("Final output")
with open(os.path.join(os.getcwd(),outputFile), 'w') as output:
    if len(basicAlignedA) <= 100:
        print("Aligned string A: "+ basicAlignedA)
        output.write(basicAlignedA+"\n")
    else:
        print("Aligned string A: "+basicAlignedA[0:50]+"*"+basicAlignedA[-50:])
        output.write(basicAlignedA[0:50]+"*"+basicAlignedA[-50:]+"\n")

    if len(basicAlignedB) <= 100:
        print("Aligned string B: "+basicAlignedB)
        output.write(basicAlignedB+"\n")
    else:
        print("Aligned string B: "+basicAlignedB[0:50]+"*"+basicAlignedB[-50:])
        output.write(basicAlignedB[0:50]+"*"+basicAlignedB[-50:]+"\n")

    print("Total time taken: "+str(timeTotal)+" (s)")
    output.write("Total time taken: "+str(timeTotal)+" (s) \n")

    print("Total memory allocated: "+str(memoryTotal/2**20)+" MB")
    output.write("Total memory allocated: "+str(memoryTotal/2**20)+" MB \n")
