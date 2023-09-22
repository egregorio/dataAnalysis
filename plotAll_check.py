import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import scipy

# Import data from 7/29
data1 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/\
08172022_Xdata')
#data2 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/\
#08172022_Xdata')

print(np.shape(data1))
shape = np.shape(data1)

#for i in range(0,shape[0]):
#	data1[i,:] = data1[i,:] - data1[i,0]

#for i in range(0,shape[0]):
#	for j in range(0,shape[1]):
#		at90 = np.argmin(data1[i,:])
#		data1[i,:] = data1[i,:] / data1[i,at90]

plt.figure()
plt.title('All Dimensional Y For 21')
plt.plot(data1[0],label='0')
plt.plot(data1[1],label='1')
plt.plot(data1[2],label='2')
plt.plot(data1[3],label='3')
plt.plot(data1[4],label='4')
plt.plot(data1[5],label='5')
plt.plot(data1[6],label='6')
plt.plot(data1[7],label='7')
plt.plot(data1[8],label='8')
plt.plot(data1[9],label='9')
#plt.plot(data1[10],label='10')
#plt.plot(data1[11],label='11')
#plt.plot(data1[12],label='12')
#plt.plot(data1[13],label='13')
#plt.plot(data1[14],label='14')
#plt.plot(data1[15],label='15')
#plt.plot(data1[16],label='16')
#plt.plot(data1[17],label='17')
#plt.plot(data1[18],label='18')
#plt.plot(data1[19],label='19')
plt.axhline(y=0,color='blue',linestyle='--')
#plt.xlim(0,70)
#plt.ylim(-0.05,0)
plt.legend()
plt.show()
#plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/dissertation plots/8172022_allAngle.png')
#plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/dissertation plots/8172022_allDepth.png')

