import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import scipy


# Import data from 7/29
xmean_729 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/xmeans_729.txt')
ymean_729 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/ymeans_729.txt')
xstds_729 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/xstd_729.txt')
ystds_729 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/ystd_729.txt')
# Import data from 9/18
xmean_918 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/xmeans_918.txt')
ymean_918 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/ymeans_918.txt')
xstds_918 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/xstd_918.txt')
ystds_918 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/ystd_918.txt')
# Import data from 9/20
xmean_920 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/xmeans_920.txt')
ymean_920 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/ymeans_920.txt')
xstds_920 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/xstd_920.txt')
ystds_920 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/ystd_920.txt')
# Import data from 9/21
xmean_921 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/frontview/xmeans_921.txt')
ymean_921 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/frontview/ymeans_921.txt')
xstds_921 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/frontview/xstd_921.txt')
ystds_921 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/frontview/ystd_921.txt')


plot_x = np.linspace(0,1,350)


# Plot for the STD in Y direction
plt.figure()
plt.title('Y Coordinates / Height v. Time')
plt.xlabel('Non-Dimensional Time')
plt.ylabel('Height in Body Lengths')
plt.errorbar(plot_x,ymean_918[0:350],yerr=ystds_918[0:350],fmt='k',ecolor='springgreen',label='0.0136 Nm')
plt.errorbar(plot_x,ymean_920[0:350],yerr=ystds_920[0:350],fmt='k',ecolor='deepskyblue',label='0.0156 Nm')
plt.errorbar(plot_x,ymean_921[0:350],yerr=ystds_921[0:350],fmt='k',ecolor='mediumpurple',label='0.0153 Nm')
plt.errorbar(plot_x,ymean_729[0:350],yerr=ystds_729[0:350],fmt='k',ecolor='hotpink',label='0.0294 Nm')
plt.legend()
#plt.xlim(0,1)
#plt.ylim(-1.2,0)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/yStd.png')

# Plot for the STD in X direction
plt.figure()
plt.title('X Coordinates v. Time')
plt.xlabel('Non-Dimensional Time')
plt.ylabel('Horizonal Position in Body Lengths')
plt.errorbar(plot_x,xmean_918[0:350],yerr=xstds_918[0:350],fmt='k',ecolor='springgreen',label='0.0136 Nm')
plt.errorbar(plot_x,xmean_920[0:350],yerr=xstds_920[0:350],fmt='k',ecolor='deepskyblue',label='0.0156 Nm')
plt.errorbar(plot_x,xmean_921[0:350],yerr=xstds_921[0:350],fmt='k',ecolor='mediumpurple',label='0.0153 Nm')
plt.errorbar(plot_x,xmean_729[0:350],yerr=xstds_729[0:350],fmt='k',ecolor='hotpink',label='0.0294 Nm')
plt.legend()
plt.xlim(0,1)
plt.ylim(-0.55,0.05)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/xStd.png')

print(':)')
