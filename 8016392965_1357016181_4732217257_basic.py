import os
import sys
import timeit
import psutil
from inputStringHandler_8016392965_1357016181_4732217257 import createInputStrings
from basicStringAligner_8016392965_1357016181_4732217257 import alignStrings
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

def basicProcess():
    # Input file
    inputFile = sys.argv[1]

    # Create the input strings according to definition
    timeStart = timeit.default_timer()
    inputStringA, inputStringB, stringsMemory = createInputStrings(os.path.join(os.getcwd(),inputFile))

    # Align the two strings using basic DP algorithm
    timeBasicBefore = timeit.default_timer()
    basicAlignedA, basicAlignedB, memoryTakenBasic = alignStrings(inputStringA, inputStringB)
    timeBasicAfter = timeit.default_timer()
    timeTakenBasic = timeBasicAfter - timeBasicBefore
    #print("Basic DP done")

    #print("Final output")
    with open(os.path.join(os.getcwd(),outputFile), 'w') as output:
        if len(basicAlignedA) <= 100:
            #print("Aligned string A: "+ basicAlignedA)
            output.write(basicAlignedA+"\n")
        else:
            #print("Aligned string A: "+basicAlignedA[0:50]+" "+basicAlignedA[-50:])
            output.write(basicAlignedA[0:50]+" "+basicAlignedA[-50:]+"\n")

        if len(basicAlignedB) <= 100:
            #print("Aligned string B: "+basicAlignedB)
            output.write(basicAlignedB+"\n")
        else:
            #print("Aligned string B: "+basicAlignedB[0:50]+" "+basicAlignedB[-50:])
            output.write(basicAlignedB[0:50]+" "+basicAlignedB[-50:]+"\n")

        #print("Score: "+str(calcScore(basicAlignedA, basicAlignedB)))
        output.write("Optimal Alignment Score: "+str(calcScore(basicAlignedA, basicAlignedB))+"\n")
        
        basicTime = timeTakenBasic
        #print(basicTime)
        #print("Total time taken: "+str(timeTakenBasic)+" (s)")
        output.write("Total time taken: "+str(timeTakenBasic)+" (s) \n")

def main():
    with ThreadPoolExecutor() as executor:
        monitor = MemoryMonitor()
        mem_thread = executor.submit(monitor.measure_usage)
        try:
            fn_thread = executor.submit(basicProcess)
            result = fn_thread.result()
        finally:
            monitor.keep_measuring = False
            max_usage = mem_thread.result()

        basicMemory = max_usage+stringsMemory
        #print(f"Peak memory usage Basic : {basicMemory}")
        with open(os.path.join(os.getcwd(),outputFile), 'a') as output:
            output.write("Total memory used: "+str(basicMemory)+" (KBs) \n")

if __name__ == "__main__":
    main()