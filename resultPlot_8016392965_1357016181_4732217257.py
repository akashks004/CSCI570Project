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
    lines, err = subprocess.Popen(["python", "mainProgram_8016392965_1357016181_4732217257.py", "TestCases\input"+str(i)+".txt"], stdout = subprocess.PIPE,shell=True).communicate()
    lines = lines.decode("utf-8")
    lines = lines.splitlines()
    print(lines)
    m_n.append(int(lines[0]))
    basicCpuTime.append(float(lines[1]))
    advancedCpuTime.append(float(lines[2]))
    basicMemory.append(float(lines[3]))
    advancedMemory.append(float(lines[4]))

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

plt.figure(1)
plt.plot(smn, smoothBasicTime, color = 'tab:blue')
plt.plot(smn, smoothAdvancedTime, color = 'tab:orange')
plt.xlabel("m + n")
plt.ylabel("CPU Time (s)")
plt.legend(['Basic', 'Advanced'])
plt.title("CPU Time vs problem size")
#plt.show()
plt.savefig('CPUPlot.png')

plt.figure(2)
plt.plot(smn, smoothBasicMemory, color = 'tab:blue')
plt.plot(smn, smoothAdvancedMemory, color = 'tab:orange')
plt.xlabel("m + n")
plt.ylabel("Memory (MB)")
plt.legend(['Basic', 'Advanced'])
plt.title("Memory vs problem size")
#plt.ylim(bottom=10)
#plt.show()
plt.savefig('MemoryPlot.png')
