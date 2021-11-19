from consts import acgt_index, alpha, delta
import psutil

def alignStrings(stringA, stringB):
    memoryBefore = psutil.virtual_memory()[3]
    alignedStringA = ""
    alignedStringB = ""

    lenA = len(stringA) + 1
    lenB = len(stringB) + 1

    print("Init\n")
    # Constructing dp table and filling it
    dp = []
    for i in range(lenB):
        inner = []
        for j in range(lenA):
            inner.append(0)
        dp.append(inner)

    for i in range(lenB):
        dp[i][0] = i * delta

    for j in range(lenA):
        dp[0][j] = j * delta

    print("Table allocated\n")
    for i in range(1, lenB):
        for j in range(1, lenA):
            cost_x_y = dp[i - 1][j - 1] + alpha[acgt_index.get(stringA[j - 1])][acgt_index.get(stringB[i - 1])]
            cost_x_not = dp[i - 1][j] + delta
            cost_y_not = dp[i][j - 1] + delta
            dp[i][j] = min(cost_x_not, min(cost_y_not, cost_x_y))

    print("Table done\n")
    #print(dp)
    # Top down pass to get the aligned strings
    i = lenB - 1
    j = lenA - 1
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            if dp[i][j] == dp[i - 1][j - 1] + alpha[acgt_index.get(stringA[j - 1])][acgt_index.get(stringB[i - 1])]:
                alignedStringA = stringA[j - 1] + alignedStringA
                alignedStringB = stringB[i - 1] + alignedStringB
                i = i - 1
                j = j - 1
            else:
                if dp[i - 1][j] < dp[i][j - 1]:
                    alignedStringA = "_" + alignedStringA
                    alignedStringB = stringB[i - 1] + alignedStringB
                    i = i - 1
                else:
                    alignedStringA = stringA[j - 1] + alignedStringA
                    alignedStringB = "_" + alignedStringB
                    j = j - 1
        else:
            if i > 0:
                alignedStringA = "_" + alignedStringA
                alignedStringB = stringB[i - 1] + alignedStringB
                i = i - 1
            else:
                alignedStringA = stringA[j - 1] + alignedStringA
                alignedStringB = "_" + alignedStringB
                j = j - 1

    print("Backtracking done\n")
    # print(alignedStringA)
    # print(alignedStringB)
    memoryAfter = psutil.virtual_memory()[3]
    return alignedStringA, alignedStringB, memoryAfter-memoryBefore

# alignStrings('GTGCATCAGCATGC', 'ACGCTGCACAGC') -> 15, mismatch for GA
# alignStrings('CTGCATCAGCATGC', 'ACGCTGCACAGC') -> 16, add gap for CA
