import os
import sys
import timeit
import psutil
from concurrent.futures import ThreadPoolExecutor

from inputStringHandler_8016392965_1357016181_4732217257 import createInputStrings
from advancedStringAligner_8016392965_1357016181_4732217257 import alignStringsAdvanced
from consts_8016392965_1357016181_4732217257 import outputFile
from utils_8016392965_1357016181_4732217257 import calcScore, MemoryMonitor

stringsMemory = 0
basicTime = 0
advancedTime = 0
basicMemory = 0
advancedMemory = 0

def advancedProcess():
    # Input file
    inputFile = sys.argv[1]

    timeAdvancedBefore = timeit.default_timer()
    # Create the input strings according to definition
    inputStringA, inputStringB, _ = createInputStrings(os.path.join(os.getcwd(),inputFile))

    # Align the two strings using memory-efficient DP algorithm
    advancedAlignedA, advancedAlignedB, _ = alignStringsAdvanced(inputStringA, inputStringB)
    timeAdvancedAfter = timeit.default_timer()
    timeTakenAdvanced = timeAdvancedAfter - timeAdvancedBefore

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
        output.write(str(calcScore(advancedAlignedA, advancedAlignedB))+"\n")

        #print("Total time taken: "+str(timeTakenAdvanced)+" (s)")
        output.write(str(timeTakenAdvanced)+"\n")

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

        advancedMemory = max_usage
        with open(os.path.join(os.getcwd(),outputFile), 'a') as output:
            output.write(str(advancedMemory)+"\n")

if __name__ == "__main__":
    main()
