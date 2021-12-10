# Output file
outputFile1 = "output1.txt"
outputFile2 = "output2.txt"
outputFile = "output.txt"

# Mismatch cost table - alpha
acgt_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
alpha = [[0, 110, 48, 94],
         [110, 0, 118, 48],
         [48, 118, 0, 110],
         [94, 48, 110, 0]]

# Gap penalty - delta
delta = 30
