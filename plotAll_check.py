import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import scipy

# Import data from 7/29
data = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/08172022_sg_v_allData')
#data = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/08172022_asym_n2_allData')
#data = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/04052022_asym1_allData')
#data = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/04042022_allData')
#data = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/10212021_allData')
#data = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/10262021_allData')
#data = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/10262021_allData_x')

print(np.shape(data))

plt.figure()
plt.title('All Dimensional Y For 21')
plt.plot(data[0],'k')
plt.plot(data[1],'r')
#plt.plot(data[2],'r')
#plt.plot(data[3],'r')
#plt.plot(data[4],'r')
#plt.plot(data[5],'r')
#plt.plot(data[6],'b')
#plt.plot(data[7],'b')
#plt.plot(data[8],'b')
#plt.plot(data[9],'b')
#plt.plot(data[10],'b')
#plt.xlim(0,300)
plt.show()


