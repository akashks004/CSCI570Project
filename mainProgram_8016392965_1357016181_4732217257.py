import os
import sys
import timeit
from concurrent.futures import ThreadPoolExecutor

from inputStringHandler_8016392965_1357016181_4732217257 import createInputStrings
from basicStringAligner_8016392965_1357016181_4732217257 import alignStrings
from advancedStringAligner_8016392965_1357016181_4732217257 import alignStringsAdvanced
from consts_8016392965_1357016181_4732217257 import outputFile1, outputFile2
from utils_8016392965_1357016181_4732217257 import calcScore, MemoryMonitor

def basicProcess():
    # Input file
    inputFile = sys.argv[1]
    mnsize = 0

    timeBasicBefore = timeit.default_timer()
    # Create the input strings according to definition
    inputStringA, inputStringB, _ = createInputStrings(os.path.join(os.getcwd(),inputFile))
    mnsize = len(inputStringA) + len(inputStringB)

    # Align the two strings using basic DP algorithm
    basicAlignedA, basicAlignedB, _ = alignStrings(inputStringA, inputStringB)
    timeBasicAfter = timeit.default_timer()
    timeTakenBasic = timeBasicAfter - timeBasicBefore

    with open(os.path.join(os.getcwd(),outputFile1), 'w') as output:
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

        #print("Total time taken: "+str(timeTakenBasic)+" (s)")
        output.write("Total time taken: "+str(timeTakenBasic)+" (s) \n")
    print(mnsize)
    print(timeTakenBasic)

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

    with open(os.path.join(os.getcwd(),outputFile2), 'w') as output:
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

        #print("Total time taken: "+str(timeTakenAdvanced)+" (s)")
        output.write("Total time taken: "+str(timeTakenAdvanced)+" (s) \n")
    print(timeTakenAdvanced)

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

        basicMemory = max_usage
        #print(f"Peak memory usage Basic : {basicMemory}")
        with open(os.path.join(os.getcwd(),outputFile1), 'a') as output:
            output.write("Total memory used: "+str(basicMemory)+" (KBs) \n")

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
        #print(f"Peak memory usage Advanced: {advancedMemory}")
        with open(os.path.join(os.getcwd(),outputFile2), 'a') as output:
            output.write("Total memory used: "+str(advancedMemory)+" (KBs) \n")

    print(basicMemory / 1024)
    print(advancedMemory / 1024)

if __name__ == "__main__":
    main()
