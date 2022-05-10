import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import scipy

# Import data from 7/29
data_729 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/7292021_allData')

print(np.shape(data_729))

plt.figure()
plt.title('All Dimensional Y For July')
plt.plot(data_729[0])
plt.plot(data_729[1])
plt.plot(data_729[2])
plt.plot(data_729[3])
plt.plot(data_729[4])
#plt.plot(data_729[5])
plt.plot(data_729[6])
plt.plot(data_729[7])
plt.plot(data_729[8])
#plt.plot(data_729[9])
plt.plot(data_729[10])
#plt.plot(data_729[11])
plt.plot(data_729[12])
plt.plot(data_729[13])
#plt.plot(data_729[14])
#plt.plot(data_729[15])
plt.plot(data_729[16])
plt.plot(data_729[17])
#plt.plot(data_729[18])
plt.plot(data_729[19])
#plt.plot(data_729[20])
plt.plot(data_729[21])
plt.plot(data_729[22])
#plt.plot(data_729[23])
#plt.plot(data_729[24])
#plt.plot(data_729[25])
plt.plot(data_729[26])
#plt.plot(data_729[27])
plt.plot(data_729[28])
plt.plot(data_729[29])
plt.show()
