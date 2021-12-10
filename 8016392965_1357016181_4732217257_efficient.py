import os
import sys
import timeit
import psutil
from inputStringHandler_8016392965_1357016181_4732217257 import createInputStrings
from advancedStringAligner_8016392965_1357016181_4732217257 import alignStringsAdvanced
from consts_8016392965_1357016181_4732217257 import outputFile, delta, alpha, acgt_index
from concurrent.futures import ThreadPoolExecutor
#import resource
stringsMemory = 0
basicTime = 0
advancedTime = 0
basicMemory = 0
advancedMemory = 0

from time import sleep
class MemoryMonitor:
    def __init__(self):
        self.keep_measuring = True
        self.process = psutil.Process(os.getpid())

    def measure_usage(self):
        max_usage = 0
        while self.keep_measuring:
            max_usage = max(
                max_usage,
                #resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
                self.process.memory_info()[0]
            )
            sleep(0.1)

        return max_usage/ 1024

def calcScore(stringA, stringB):
    lent = len(stringA)
    score = 0
    for i in range(lent):
        if stringA[i] == '_' or stringB[i] == '_':
            score += delta
        elif stringA[i] == stringB[i]:
            score += 0
        else:
            score += alpha[acgt_index.get(stringA[i])][acgt_index.get(stringB[i])]
    return score

def advancedProcess():
    # Input file
    inputFile = sys.argv[1]

    # Create the input strings according to definition
    timeStart = timeit.default_timer()
    inputStringA, inputStringB, memory = createInputStrings(os.path.join(os.getcwd(),inputFile))

    # Align the two strings using memory-efficient DP algorithm
    timeAdvancedBefore = timeit.default_timer()
    advancedAlignedA, advancedAlignedB, memoryTakenAdvanced = alignStringsAdvanced(inputStringA, inputStringB)
    timeAdvancedAfter = timeit.default_timer()
    timeTakenAdvanced = timeAdvancedAfter - timeAdvancedBefore
    #print("Advanced DP done")

    #print("Final output")
    with open(os.path.join(os.getcwd(),outputFile), 'w') as output:
        if len(advancedAlignedA) <= 100:
            #print("Aligned string A: "+ advancedAlignedA)
            output.write(advancedAlignedA+"\n")
        else:
            #print("Aligned string A: "+advancedAlignedA[0:50]+" "+advancedAlignedA[-50:])
            output.write(advancedAlignedA[0:50]+" "+advancedAlignedA[-50:]+"\n")

        if len(advancedAlignedB) <= 100:
            #print("Aligned string B: "+advancedAlignedB)
            output.write(advancedAlignedB+"\n")
        else:
            #print("Aligned string B: "+advancedAlignedB[0:50]+" "+advancedAlignedB[-50:])
            output.write(advancedAlignedB[0:50]+" "+advancedAlignedB[-50:]+"\n")
        
        #print("Score: "+str(calcScore(advancedAlignedA, advancedAlignedB)))
        output.write("Optimal Alignment Score: "+str(calcScore(advancedAlignedA, advancedAlignedB))+"\n")

        advancedTime = timeTakenAdvanced
        #print(advancedTime)
        #print("Total time taken: "+str(timeTakenAdvanced)+" (s)")
        output.write("Total time taken: "+str(timeTakenAdvanced)+" (s) \n")

def main():

    with ThreadPoolExecutor() as executor:
        monitor = MemoryMonitor()
        mem_thread = executor.submit(monitor.measure_usage)
        try:
            fn_thread = executor.submit(advancedProcess)
            result = fn_thread.result()
        finally:
            monitor.keep_measuring = False
            max_usage = mem_thread.result()

        advancedMemory = max_usage+stringsMemory
        #print(f"Peak memory usage Advanced: {advancedMemory}")
        with open(os.path.join(os.getcwd(),outputFile), 'a') as output:
            output.write("Total memory used: "+str(advancedMemory)+" (KBs) \n")

if __name__ == "__main__":
    main()