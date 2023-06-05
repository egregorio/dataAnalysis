import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import scipy

# Import data from 7/29
data1 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/\
08172022_asym_n1_allData')
data2 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/\
08172022_asym_n2_allData')

print(np.shape(data1))
print(np.shape(data2))

plt.figure()
plt.title('All Dimensional Y For 21')
plt.plot(data2[0],'r')
plt.plot(data2[1],'r')
plt.plot(data2[2],'r')
plt.plot(data2[3],'r')
#plt.plot(data2[4],'r')
plt.plot(data2[5],'r')
plt.plot(data2[6],'y')
plt.plot(data2[7],'y')
plt.plot(data2[8],'r')
plt.plot(data1[0],'k')
plt.plot(data1[1],'k')
plt.plot(data1[2],'k')
plt.plot(data1[3],'k')
plt.plot(data1[4],'g')
plt.plot(data1[5],'k')
plt.plot(data1[6],'k')
plt.plot(data1[7],'g')
plt.plot(data1[8],'k')
plt.plot(data1[9],'k')
plt.plot(data1[10],'k')
#plt.xlim(240,320)
plt.show()


