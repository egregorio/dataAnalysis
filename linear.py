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


input_y = [ ymean_729[1:75],
            ymean_918[1:75],
            ymean_920[1:75],
            ymean_921[1:75] ]

y_max_length = 75

means_y, y_stds = averageF( input_y, 74)

plot_x = np.linspace(0,0.2143,74)

m, b = np.polyfit(plot_x, means_y, 1)

#print('slope = ',m)
#print('inter = ',b)

saveData = [m, b]

np.savetxt('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/linearFit.txt',saveData)

# Plot for the STD in Y direction
plt.figure()
plt.title('Y Coordinates / Height v. Time')
plt.xlabel('Non-Dimensional Time')
plt.ylabel('Height in Body Lengths')
plt.errorbar(plot_x,ymean_918[0:74],yerr=ystds_918[0:74],fmt='k',ecolor='springgreen',label='0.0136 Nm')
plt.errorbar(plot_x,ymean_920[0:74],yerr=ystds_920[0:74],fmt='k',ecolor='deepskyblue',label='0.0156 Nm')
plt.errorbar(plot_x,ymean_921[0:74],yerr=ystds_921[0:74],fmt='k',ecolor='mediumpurple',label='0.0153 Nm')
plt.errorbar(plot_x,ymean_729[0:74],yerr=ystds_729[0:74],fmt='k',ecolor='hotpink',label='0.0294 Nm')
plt.plot(plot_x,means_y,color='r')
plt.legend()
plt.xlim(0,0.2143)
#plt.ylim(-1.2,0)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/yLine.png')

print(':)')
