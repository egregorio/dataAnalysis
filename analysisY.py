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

xmean_729 = xmean_729 - xmean_729[0]
xmean_918 = xmean_918 - xmean_918[0]
xmean_920 = xmean_920 - xmean_920[0]
xmean_921 = xmean_921 - xmean_921[0]

ymean_729 = ymean_729 - ymean_729[0]
ymean_918 = ymean_918 - ymean_918[0]
ymean_920 = ymean_920 - ymean_920[0]
ymean_921 = ymean_921 - ymean_921[0]

xstds_729 = xstds_729 - xstds_729[0]
xstds_918 = xstds_918 - xstds_918[0]
xstds_920 = xstds_920 - xstds_920[0]
xstds_921 = xstds_921 - xstds_921[0]

ystds_729 = ystds_729 - ystds_729[0]
ystds_918 = ystds_918 - ystds_918[0]
ystds_920 = ystds_920 - ystds_920[0]
ystds_921 = ystds_921 - ystds_921[0]

# Best Fit Line for Y Direction
bestFit = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/linearFit.txt')
slope = bestFit[0]
inter = bestFit[1]
interpp = np.linspace(0,1,100)


linearF = slope * interpp #+ inter



print('slope = ',slope)

# points for the x axis on graphs, aka time
plot_x = np.linspace(0,0.07,350)


# Plot for the STD in Y direction
plt.figure()
plt.title('Y Coordinates / Height v. Time')
plt.xlabel('Non-Dimensional Time')
plt.ylabel('Height in Body Lengths')
plt.errorbar(plot_x,ymean_918[0:350],yerr=ystds_918[0:350],fmt='k',ecolor='springgreen',label='0.0136 Nm')
plt.errorbar(plot_x,ymean_920[0:350],yerr=ystds_920[0:350],fmt='k',ecolor='deepskyblue',label='0.0156 Nm')
plt.errorbar(plot_x,ymean_921[0:350],yerr=ystds_921[0:350],fmt='k',ecolor='mediumpurple',label='0.0153 Nm')
plt.errorbar(plot_x,ymean_729[0:350],yerr=ystds_729[0:350],fmt='k',ecolor='hotpink',label='0.0294 Nm')
plt.plot(interpp,linearF,color='r',linewidth=2)
#plt.plot(0.29181494661921703, -0.3999999999999997,'o',color='springgreen')
#plt.plot(0.3434163701067616, -0.4717241379310342, 'o', color='deepskyblue')
#plt.plot(0.42348754448398584, -0.5820689655172411,'o',color='mediumpurple')
#plt.plot(0.51067615658363, -0.7006896551724136,'o', color='hotpink')
plt.legend()
plt.xlim(0,0.07)
plt.ylim(-2,0)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/yStd_interp.png')

# points for the x axis on graphs, aka time
plot_x = np.linspace(0,0.004,20)

# Plot for the STD in Y direction
plt.figure()
plt.title('Y Coordinates / Height v. Time')
plt.xlabel('Non-Dimensional Time')
plt.ylabel('Height in Body Lengths')
plt.errorbar(plot_x,ymean_918[0:20],yerr=ystds_918[0:20],fmt='k',ecolor='springgreen',label='0.0136 Nm')
plt.errorbar(plot_x,ymean_920[0:20],yerr=ystds_920[0:20],fmt='k',ecolor='deepskyblue',label='0.0156 Nm')
plt.errorbar(plot_x,ymean_921[0:20],yerr=ystds_921[0:20],fmt='k',ecolor='mediumpurple',label='0.0153 Nm')
plt.errorbar(plot_x,ymean_729[0:20],yerr=ystds_729[0:20],fmt='k',ecolor='hotpink',label='0.0294 Nm')
plt.plot(interpp,linearF,color='r',linewidth=2)
#plt.plot(0.29181494661921703, -0.3999999999999997,'o',color='springgreen')
#plt.plot(0.3434163701067616, -0.4717241379310342, 'o', color='deepskyblue')
#plt.plot(0.42348754448398584, -0.5820689655172411,'o',color='mediumpurple')
#plt.plot(0.51067615658363, -0.7006896551724136,'o', color='hotpink')
plt.legend()
plt.xlim(0,0.004)
plt.ylim(-0.1,0)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/yStd_interp_zoom.png')

print(';)')
