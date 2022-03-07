import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from functions import *
import scipy


# Import data from 7/29
ymean_729 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/ymeans_729.txt')
ystds_729 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/ystd_729.txt')
# Import data from 9/18
ymean_918 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/ymeans_918.txt')
ystds_918 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/ystd_918.txt')
# Import data from 9/20
ymean_920 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/ymeans_920.txt')
ystds_920 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/ystd_920.txt')
# Import data from 9/21
ymean_921 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/frontview/ymeans_921.txt')
ystds_921 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/frontview/ystd_921.txt')

ymean_729 = ymean_729 - ymean_729[0]
ymean_918 = ymean_918 - ymean_918[0]
ymean_920 = ymean_920 - ymean_920[0]
ymean_921 = ymean_921 - ymean_921[0]

ystds_729 = ystds_729 - ystds_729[0]
ystds_918 = ystds_918 - ystds_918[0]
ystds_920 = ystds_920 - ystds_920[0]
ystds_921 = ystds_921 - ystds_921[0]

plot_74 = np.linspace(0.0002,0.015,74)
plot_65 = np.linspace(0.002,0.015,65)
plot_10 = np.linspace(0.0002,0.0022,10)
plot_20 = np.linspace(0.0002,0.0042,20)

m_729, b_729 = np.polyfit(plot_74,ymean_729[1:75],1)
m_918, b_918 = np.polyfit(plot_74,ymean_918[1:75],1)
m_920, b_920 = np.polyfit(plot_74,ymean_920[1:75],1)
m_921, b_921 = np.polyfit(plot_74,ymean_921[1:75],1)
#m_729, b_729 = np.polyfit(plot_20,ymean_729[1:21],1)
#m_918, b_918 = np.polyfit(plot_20,ymean_918[1:21],1)
#m_920, b_920 = np.polyfit(plot_20,ymean_920[1:21],1)
#m_921, b_921 = np.polyfit(plot_20,ymean_921[1:21],1)

input_y = [ ymean_729[1:75],
            ymean_918[1:75],
            ymean_920[1:75],
            ymean_921[1:75] ]

y_max_length = 74

means_y, y_stds = averageF( input_y, 74)
#means_y, y_stds = averageF( input_y, 20)

m, b = np.polyfit(plot_74, means_y, 1)
#m, b = np.polyfit(plot_20, means_y, 1)

plot_x = np.linspace(0.0002,0.07,349)

linearF = m * plot_x #+ b
linearF_729 = m_729 * plot_x + b_729
linearF_918 = m_918 * plot_x + b_918
linearF_920 = m_920 * plot_x + b_920
linearF_921 = m_921 * plot_x + b_921

print('slopes! mean = ',m,', 7/29 = ',m_729,', 9/18 = ',m_918,', 9/20 = ',m_920,', 9/21 = ',m_921)

#print('slope = ',m)
#print('inter = ',b)

saveData = [m, b]

np.savetxt('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/linearFit.txt',saveData)

plt.figure
x = np.arange(0, 1, 0.02)
plt.subplot(2, 2, 1)
plt.errorbar(plot_x,ymean_918[1:350],yerr=ystds_918[1:350],fmt='k',ecolor='springgreen',label='0.0136 Nm')
plt.plot(plot_x,linearF_729,color='red',label='7/29')
  
plt.subplot(2, 2, 2)
plt.errorbar(plot_x,ymean_920[1:350],yerr=ystds_920[1:350],fmt='k',ecolor='deepskyblue',label='0.0156 Nm')
plt.plot(plot_x,linearF_918,color='red',label='9/18')
  
plt.subplot(2, 2, 3)
plt.errorbar(plot_x,ymean_921[1:350],yerr=ystds_921[1:350],fmt='k',ecolor='mediumpurple',label='0.0153 Nm')
plt.plot(plot_x,linearF_920,color='red',label='9/20')
  
plt.subplot(2, 2, 4)
plt.errorbar(plot_x,ymean_729[1:350],yerr=ystds_729[1:350],fmt='k',ecolor='hotpink',label='0.0294 Nm')
plt.plot(plot_x,linearF_921,color='red',label='9/21')
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/comp.png')

# Plot for the STD in Y direction
#plt.figure()
#plt.title('Y Coordinates / Height v. Time')
#plt.xlabel('Non-Dimensional Time')
#plt.ylabel('Height in Body Lengths')
#plt.errorbar(plot_x,ymean_918[1:100],yerr=ystds_918[1:100],fmt='k',ecolor='springgreen',label='0.0136 Nm')
#plt.errorbar(plot_x,ymean_920[1:100],yerr=ystds_920[1:100],fmt='k',ecolor='deepskyblue',label='0.0156 Nm')
#plt.errorbar(plot_x,ymean_921[1:100],yerr=ystds_921[1:100],fmt='k',ecolor='mediumpurple',label='0.0153 Nm')
#plt.errorbar(plot_x,ymean_729[1:100],yerr=ystds_729[1:100],fmt='k',ecolor='hotpink',label='0.0294 Nm')
#plt.plot(plot_x,linearF,color='r')
#plt.legend()
#plt.xlim(0,0.2143)
#plt.ylim(-1.2,0)
#plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/yLine.png')

#plt.figure()
#plt.plot(plot_x,linearF,color='red',label='interpolation')
#plt.plot(plot_x,linearF_729,color='springgreen',label='7/29')
#plt.plot(plot_x,linearF_918,color='deepskyblue',label='9/18')
#plt.plot(plot_x,linearF_920,color='mediumpurple',label='9/20')
#plt.plot(plot_x,linearF_921,color='hotpink',label='9/21')
#plt.plot(plot_x,linearF,color='red',label='interpolation')
#plt.legend()
#plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/line.png')

print(':)')
