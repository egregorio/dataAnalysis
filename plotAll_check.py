import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import scipy

# Import data from 7/29
#data = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/04052022_asym1_allData')
#data = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/04042022_allData')
#data = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/10212021_allData')
#data = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/10262021_allData')
data = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/10262021_allData_x')

print(np.shape(data))

plt.figure()
plt.title('All Dimensional Y For 21')
plt.plot(data[0])
plt.plot(data[1])
plt.plot(data[2])
plt.plot(data[3])
plt.plot(data[4])
plt.plot(data[5])
plt.plot(data[6])
plt.plot(data[7])
plt.plot(data[8])
plt.plot(data[9])
plt.plot(data[10])
#plt.xlim(0,300)
plt.show()


