import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import scipy

# Import data from 7/29
data_21 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/10212021_allData')
data_26 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/10262021_allData')

print(np.shape(data_21))
print(np.shape(data_26))

plt.figure()
plt.title('All Dimensional Y For 21')
plt.plot(data_21[0])
plt.plot(data_21[1])
plt.plot(data_21[2])
plt.plot(data_21[3])
plt.plot(data_21[4])
plt.plot(data_21[5])
plt.plot(data_21[6])
plt.plot(data_21[7])
plt.plot(data_21[8])
plt.show()

plt.figure()
plt.title('All Dimensional Y For 26')
plt.plot(data_26[0])
plt.plot(data_26[1])
plt.plot(data_26[2])
plt.plot(data_26[3])
plt.plot(data_26[4])
plt.plot(data_26[5])
plt.plot(data_26[6])
plt.plot(data_26[7])
plt.plot(data_26[8])
plt.plot(data_26[9])
plt.plot(data_26[10])
#plt.show()

