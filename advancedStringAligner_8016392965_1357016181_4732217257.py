import psutil
from consts_8016392965_1357016181_4732217257 import acgt_index,alpha, delta
from basicStringAligner_8016392965_1357016181_4732217257 import alignStrings
import numpy as np

def reverse_string(a_string):
    return a_string[::-1]

def NWScore(stringX, stringY):
    memoryBefore = psutil.virtual_memory()[3]
    lenX = len(stringX)+1
    lenY = len(stringY)+1

    dp = []
    for i in range(2):
        inner = []
        for j in range(lenY):
            inner.append(0)
        dp.append(inner)

    for j in range(1, lenY):
        dp[0][j] = dp[0][j-1] + delta

    for i in range(1, lenX):
        dp[1][0] = dp[0][0] + delta
        for j in range(1, lenY):
            scoreDiff = dp[0][j-1] + alpha[acgt_index.get(stringX[i-1])][acgt_index.get(stringY[j-1])]
            scoreDel = dp[0][j] + delta
            scoreIns = dp[1][j-1] + delta
            dp[1][j] = min(scoreDiff, scoreDel, scoreIns)
        dp[0][:] = dp[1][:]

    LastLine = [0] * (lenY)
    for j in range(0,lenY):
        LastLine[j] = dp[1][j]
    memory = psutil.virtual_memory()[3] - memoryBefore
    return LastLine, memory

def Recursive(level, stringX, stringY):
    memoryBefore = psutil.virtual_memory()[3]
    memoryAfterx = 0
    memory1 = 0
    memory2 = 0
    Z = ""
    W = ""
    if len(stringX) == 0:
        for i in range(len(stringY)):
            Z = Z + '_'
            W = W + stringY[i]
    elif len(stringY) == 0:
        for i in range(len(stringX)):
            Z = Z + stringX[i]
            W = W + '_'
    elif len(stringX) == 1 or len(stringY) == 1:
        Z, W, _ = alignStrings(stringX, stringY)
    else:
        xmid = int(len(stringX) / 2)

        Xleft = stringX[:xmid]
        Xright = stringX[xmid:]
        ScoreL, memory1 = NWScore(Xleft, stringY)
        ScoreR, memory2 = NWScore(reverse_string(Xright), reverse_string(stringY))
        ScoreR = reverse_string(ScoreR)
        FScore = [x+y for x,y in zip(ScoreL, ScoreR)]
        ymid = np.argmin(FScore)
        Yleft = stringY[:ymid]
        Yright = stringY[ymid:]

        Zleft, Wleft,memoryAfterLeft = Recursive(level+1, Xleft, Yleft)
        Zright, Wright, memoryAfterRight = Recursive(level+1, Xright, Yright)
        memoryAfterx = memoryAfterLeft + memoryAfterRight

        Z = Zleft + Zright
        W = Wleft + Wright
    memoryAfter = psutil.virtual_memory()[3] - memoryBefore
    return Z, W, memoryAfterx+memory1+memory2+memoryAfter

def alignStringsAdvanced(stringA, stringB):
    alignedStringA = ""
    alignedStringB = ""

    alignedStringA, alignedStringB, memory_used = Recursive(0, stringA, stringB)

    return alignedStringA, alignedStringB, memory_used
