from sys import stdout
import matplotlib.pyplot as plt
import subprocess

from numpy.core.fromnumeric import sort

basicCpuTime = []
advancedCpuTime = []
basicMemory = []
advancedMemory = []
m_n = []

for i in range(1, 65):
    print(i)
    lines, err = subprocess.Popen(["mainProgram.py", "TestCases\input"+str(i)+".txt"], stdout = subprocess.PIPE,shell=True).communicate()
    lines = lines.decode("utf-8")
    lines = lines.splitlines()
    basicCpuTime.append(float(lines[0]))
    advancedCpuTime.append(float(lines[1]))
    basicMemory.append(float(lines[2]))
    advancedMemory.append(float(lines[3]))

#basicCpuTime = [0.00013729999999995135, 0.00023570000000000535, 0.00045909999999993456, 0.0008589999999999987, 0.001606699999999961, 0.0031585000000000085, 0.006383400000000039, 0.013383599999999996, 0.0002282999999999591, 0.0003979000000000066, 0.0007793999999999857, 0.001507399999999992, 0.002963300000000002, 0.005914199999999981, 0.011737700000000018, 0.02377990000000002, 0.0003954000000000457, 0.0007424999999999793, 0.001743400000000006, 0.0028074000000000154, 0.005914399999999986, 0.011160699999999968, 0.02210829999999997, 0.04624020000000001, 0.0007337000000000038, 0.0019046999999999814, 0.003196399999999988, 0.00548700000000002, 0.010585199999999961, 0.020749999999999935, 0.04371250000000004, 0.08766499999999999, 0.0015300999999999787, 0.0027511000000000063, 0.005361799999999972, 0.011035699999999982, 0.021550500000000028, 0.04440869999999997, 0.08663840000000006, 0.17957309999999999, 0.002816900000000011, 0.005370399999999997, 0.010433899999999996, 0.02164239999999995, 0.04163220000000001, 0.0852251, 0.17788370000000003, 0.3730406, 0.005797500000000011, 0.011745200000000011, 0.021767699999999945, 0.04453659999999998, 0.08928810000000004, 0.17269330000000005, 0.35322269999999995, 0.7259929, 0.011902099999999971, 0.02349949999999995, 0.04403380000000001, 0.09055409999999997, 0.1825699, 0.3661813, 0.7344643, 1.5333729999999999]
#advancedCpuTime = [0.000889099999999976, 0.001619499999999996, 0.0020220000000000793, 0.0022234999999999894, 0.003436400000000006, 0.008377200000000085, 0.011454999999999993, 0.0222059, 0.0016209000000000362, 0.0020482000000000555, 0.0028537999999999064, 0.005329699999999993, 0.006412300000000037, 0.01116410000000001, 0.02085860000000006, 0.04287849999999993, 0.001533400000000018, 0.002834200000000009, 0.004797399999999952, 0.008838400000000024, 0.012277400000000105, 0.02184240000000004, 0.04683139999999997, 0.08464919999999998, 0.002881300000000031, 0.004114799999999974, 0.012278400000000023, 0.01387320000000003, 0.02390520000000007, 0.04813230000000002, 0.07635010000000009, 0.14768130000000002, 0.004825400000000091, 0.006257599999999974, 0.016058200000000022, 0.023123600000000022, 0.04630310000000004, 0.08562729999999996, 0.14813719999999997, 0.3141246999999999, 0.006462699999999932, 0.011270199999999897, 0.02011430000000003, 0.04068839999999996, 0.0804456, 0.15998849999999998, 0.2979269, 0.582957, 0.010038400000000003, 0.021500899999999934, 0.038582100000000064, 0.07377900000000004, 0.1446942, 0.28430180000000005, 0.5787822000000001, 1.1379765000000002, 0.020095100000000032, 0.04055059999999999, 0.07381629999999995, 0.13801960000000002, 0.29108770000000006, 0.5548905, 1.1064629, 2.2627694]
#basicMemory = [28092.0, 28240.0, 28216.0, 28096.0, 27988.0, 28036.0, 28056.0, 28100.0, 28044.0, 28240.0, 28176.0, 28048.0, 28084.0, 28196.0, 28132.0, 28232.0, 28196.0, 28152.0, 28068.0, 28112.0, 28016.0, 28200.0, 28044.0, 28176.0, 28140.0, 28032.0, 28104.0, 28128.0, 28216.0, 28260.0, 28120.0, 28016.0, 28172.0, 28040.0, 28040.0, 28092.0, 28180.0, 28224.0, 28156.0, 32200.0, 28084.0, 28172.0, 27988.0, 28248.0, 28172.0, 28180.0, 32340.0, 38592.0, 28140.0, 28104.0, 28208.0, 28164.0, 28180.0, 31996.0, 36400.0, 47412.0, 28028.0, 28228.0, 27996.0, 28160.0, 32528.0, 36400.0, 47008.0, 70844.0]
#advancedMemory = [28108.0, 28256.0, 28232.0, 28112.0, 28060.0, 28180.0, 28328.0, 28632.0, 28060.0, 28256.0, 28192.0, 28072.0, 28160.0, 28404.0, 28532.0, 28764.0, 28212.0, 28168.0, 28092.0, 28184.0, 28224.0, 28636.0, 28764.0, 28932.0, 28156.0, 28048.0, 28156.0, 28272.0, 28488.0, 28532.0, 28872.0, 29172.0, 28188.0, 28092.0, 28188.0, 28364.0, 28452.0, 28372.0, 28732.0, 29500.0, 28136.0, 28316.0, 28240.0, 28520.0, 28604.0, 28548.0, 28932.0, 29440.0, 28284.0, 28440.0, 28516.0, 28360.0, 28912.0, 28748.0, 28644.0, 29432.0, 28064.0, 28392.0, 28508.0, 29220.0, 29148.0, 29464.0, 29456.0, 29660.0]
#m_n = [4, 6, 10, 18, 34, 66, 130, 258, 6, 8, 12, 20, 36, 68, 132, 260, 10, 12, 16, 24, 40, 72, 136, 264, 18, 20, 24, 32, 48, 80, 144, 272, 34, 36, 40, 48, 64, 96, 160, 288, 66, 68, 72, 80, 96, 128, 192, 320, 130, 132, 136, 144, 160, 192, 256, 384, 258, 260, 264, 272, 288, 320, 384, 512]

#X-axis points
for i in range(1,9):
    for j in range(1,9):
        m_n.append((2**i)+(2**j))

#print(m_n)

dict1 = dict(zip(m_n, basicCpuTime))
dict2 = dict(zip(m_n, advancedCpuTime))
dict3 = dict(zip(m_n, basicMemory))
dict4 = dict(zip(m_n, advancedMemory))
smn = sorted(dict1)
smoothBasicTime = []
smoothAdvancedTime = []
smoothBasicMemory = []
smoothAdvancedMemory = []
for i in smn:
    smoothBasicTime.append(dict1[i])
    smoothAdvancedTime.append(dict2[i])
    smoothBasicMemory.append(dict3[i])
    smoothAdvancedMemory.append(dict4[i])

plt.plot(smn, smoothBasicTime, color = 'tab:blue')
plt.plot(smn, smoothAdvancedTime, color = 'tab:orange')
plt.xlabel("m + n")
plt.ylabel("CPU Time")
plt.legend(['Basic', 'Advanced'])
plt.title("CPU Time vs problem size")
plt.savefig('CPUvsPsize.png')

plt.plot(smn, smoothBasicMemory, color = 'tab:blue')
plt.plot(smn, smoothAdvancedMemory, color = 'tab:orange')
plt.xlabel("m + n")
plt.ylabel("Memory")
plt.legend(['Basic', 'Advanced'])
plt.title("Memory vs problem size")
plt.savefig('MemoryvsPsize.png')