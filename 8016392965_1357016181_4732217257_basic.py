import os
import sys
import timeit

from inputStringHandler_8016392965_1357016181_4732217257 import createInputStrings
from basicStringAligner_8016392965_1357016181_4732217257 import alignStrings
from consts_8016392965_1357016181_4732217257 import outputFile
from utils_8016392965_1357016181_4732217257 import calcScore, MemoryMonitor
from concurrent.futures import ThreadPoolExecutor

basicTime = 0
advancedTime = 0
basicMemory = 0
advancedMemory = 0

def basicProcess():
    # Input file
    inputFile = sys.argv[1]

    timeBasicBefore = timeit.default_timer()
    # Create the input strings according to definition
    inputStringA, inputStringB, _ = createInputStrings(os.path.join(os.getcwd(),inputFile))

    # Align the two strings using basic DP algorithm
    basicAlignedA, basicAlignedB, _ = alignStrings(inputStringA, inputStringB)
    timeBasicAfter = timeit.default_timer()
    timeTakenBasic = timeBasicAfter - timeBasicBefore

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
        output.write(str(calcScore(basicAlignedA, basicAlignedB))+"\n")

        #print("Total time taken: "+str(timeTakenBasic)+" (s)")
        output.write(str(timeTakenBasic)+"\n")

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
        with open(os.path.join(os.getcwd(),outputFile), 'a') as output:
            output.write(str(basicMemory)+"\n")

if __name__ == "__main__":
    main()
