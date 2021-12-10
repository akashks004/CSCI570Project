import psutil
import os
from time import sleep

from consts_8016392965_1357016181_4732217257 import delta, alpha, acgt_index

class MemoryMonitor:
    def __init__(self):
        self.keep_measuring = True
        self.process = psutil.Process(os.getpid())

    def measure_usage(self):
        max_usage = 0
        while self.keep_measuring:
            max_usage = max(
                max_usage,
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
