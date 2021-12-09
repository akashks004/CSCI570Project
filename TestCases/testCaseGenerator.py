baseStringA = "ACTG"
baseStringB = "TACG"

indexesA = [3, 6, 1, 1, 4, 6, 7, 3]
indexesB = [1, 2, 9, 2, 4, 6, 1, 3]

count = 1

temp = ""

for k in range(len(indexesA)):
    temp = baseStringA + "\n"
    for z in range(k+1):
        temp += str(indexesA[z]) + "\n"
    for i in range(len(indexesB)):
        filename = "input"+str(count)+".txt"
        count = count + 1
        with open(filename, "w") as output:
            output.write(temp + baseStringB + "\n")
            for j in range(i+1):
                output.write(str(indexesB[j])+"\n")
        