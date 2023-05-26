import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import scipy

# Import data from 7/29
data = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/\
10262021_allData')

print(np.shape(data))

plt.figure()
plt.title('All Dimensional Y For 21')
#plt.plot(data[0],'k')
plt.plot(data[1],'k')
plt.plot(data[2],'k')
#plt.plot(data[3],'k')
#plt.plot(data[4],'k')
#plt.plot(data[5],'k')
#plt.plot(data[6],'k')
#plt.plot(data[7],'k')
#plt.plot(data[8],'k')
plt.plot(data[9],'k')
#plt.plot(data[10],'k')
#plt.xlim(240,320)
plt.show()


