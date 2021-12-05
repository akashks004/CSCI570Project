import os
import sys
import timeit
import psutil
from inputStringHandler import createInputStrings
from basicStringAligner import alignStrings
from advancedStringAligner import alignStringsAdvanced
from consts import outputFile1, outputFile2, delta, alpha, acgt_index
from concurrent.futures import ThreadPoolExecutor
#import resource
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

        return max_usage/ 1024 ** 2

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
    inputStringA, inputStringB, memory = createInputStrings(os.path.join(os.getcwd(),inputFile))

    #inputStringA = "AGTACGCA"
    #inputStringB = "TATGC"
    print("String created")
    print("A:"+str(len(inputStringA))+", B:"+str(len(inputStringB)))

    # Align the two strings using basic DP algorithm
    timeBasicBefore = timeit.default_timer()
    basicAlignedA, basicAlignedB, memoryTakenBasic = alignStrings(inputStringA, inputStringB)
    timeBasicAfter = timeit.default_timer()
    timeTakenBasic = timeBasicAfter - timeBasicBefore
    print("Basic DP done")

    print("Score: "+str(calcScore(basicAlignedA, basicAlignedB)))

    print("Final output")
    with open(os.path.join(os.getcwd(),outputFile1), 'w') as output:
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

        print("Total time taken: "+str(timeTakenBasic)+" (s)")
        output.write("Total time taken: "+str(timeTakenBasic)+" (s) \n")

def advancedProcess():
    # Input file
    inputFile = sys.argv[1]

    # Create the input strings according to definition
    timeStart = timeit.default_timer()
    inputStringA, inputStringB, memory = createInputStrings(os.path.join(os.getcwd(),inputFile))

    #inputStringA = "AGTACGCA"
    #inputStringB = "TATGC"
    print("String created")
    print("A:"+str(len(inputStringA))+", B:"+str(len(inputStringB)))

    # Align the two strings using memory-efficient DP algorithm
    timeAdvancedBefore = timeit.default_timer()
    advancedAlignedA, advancedAlignedB, memoryTakenAdvanced = alignStringsAdvanced(inputStringA, inputStringB)
    timeAdvancedAfter = timeit.default_timer()
    timeTakenAdvanced = timeAdvancedAfter - timeAdvancedBefore
    print("Advanced DP done")

    print("Score: "+str(calcScore(advancedAlignedA, advancedAlignedB)))

    print("Final output")
    with open(os.path.join(os.getcwd(),outputFile2), 'w') as output:
        if len(advancedAlignedA) <= 100:
            print("Aligned string A: "+ advancedAlignedA)
            output.write(advancedAlignedA+"\n")
        else:
            print("Aligned string A: "+advancedAlignedA[0:50]+"*"+advancedAlignedA[-50:])
            output.write(advancedAlignedA[0:50]+"*"+advancedAlignedA[-50:]+"\n")

        if len(advancedAlignedB) <= 100:
            print("Aligned string B: "+advancedAlignedB)
            output.write(advancedAlignedB+"\n")
        else:
            print("Aligned string B: "+advancedAlignedB[0:50]+"*"+advancedAlignedB[-50:])
            output.write(advancedAlignedB[0:50]+"*"+advancedAlignedB[-50:]+"\n")

        print("Total time taken: "+str(timeTakenAdvanced)+" (s)")
        output.write("Total time taken: "+str(timeTakenAdvanced)+" (s) \n")

def mainProcess():
    # Input file
    inputFile = sys.argv[1]

    # Create the input strings according to definition
    timeStart = timeit.default_timer()
    inputStringA, inputStringB, memory = createInputStrings(os.path.join(os.getcwd(),inputFile))

    #inputStringA = "AGTACGCA"
    #inputStringB = "TATGC"
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

    print(advancedAlignedA)
    print(advancedAlignedB)

    print("Final output")
    with open(os.path.join(os.getcwd(),outputFile1), 'w') as output:
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


with ThreadPoolExecutor() as executor:
    monitor = MemoryMonitor()
    mem_thread = executor.submit(monitor.measure_usage)
    try:
        fn_thread = executor.submit(basicProcess)
        result = fn_thread.result()
    finally:
        monitor.keep_measuring = False
        max_usage = mem_thread.result()

    print(f"Peak memory usage Basic : {max_usage}")

with ThreadPoolExecutor() as executor:
    monitor = MemoryMonitor()
    mem_thread = executor.submit(monitor.measure_usage)
    try:
        fn_thread = executor.submit(advancedProcess)
        result = fn_thread.result()
    finally:
        monitor.keep_measuring = False
        max_usage = mem_thread.result()

    print(f"Peak memory usage Advanced: {max_usage}")
