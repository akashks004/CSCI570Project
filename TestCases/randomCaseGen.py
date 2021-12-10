import numpy as np
import random
chars = ['A', 'T', 'G', 'C']

count = 1

temp = ""

for k in range(100):
    # random size for strings A and B
    strsize = random.randrange(2,5)

    strA = ""
    strB = ""
    # create random strA and strB
    for i in range(strsize):
        c1 = random.choice(chars)
        strA += c1
        c2 = random.choice(chars)
        strB += c2

    # random i value string A
    i_rand = random.randrange(3, 11)
    # make sure j is very close to i, or else spikes will arise in plot
    jMin = max(1, i_rand - 2)
    jMax = min(11, i_rand + 2)
    j_rand = random.randrange(jMin, jMax)

    # create random i and j indexes
    i_idx = []
    currentStrAMax = strsize
    for i in range(i_rand):
        ix = random.randrange(1, currentStrAMax)
        i_idx.append(ix)
        currentStrAMax += strsize

    j_idx = []
    currentStrBMax = strsize
    for j in range(j_rand):
        jx = random.randrange(1, currentStrBMax)
        j_idx.append(jx)
        currentStrBMax += strsize

    filename = "rinput"+str(count)+".txt"
    count += 1
    with open(filename, "w") as output:
        output.write(strA+ "\n")
        for idx in i_idx:
            output.write(str(idx)+"\n")
        output.write(strB+ "\n")
        for idx in j_idx:
            output.write(str(idx)+"\n")

