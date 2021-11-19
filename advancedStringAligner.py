import psutil

def alignStringsAdvanced(stringA, stringB):
    memoryBefore = psutil.virtual_memory()[3]
    alignedStringA = ""
    alignedStringB = ""

    memoryAfter = psutil.virtual_memory()[3]
    return alignedStringA, alignedStringB, (memoryAfter-memoryBefore)
