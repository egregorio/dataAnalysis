import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import scipy
from get_t_bar import *
from conversions import *

# Import data from 7/29
xmean_729 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/xmeans_729.txt')
xstds_729 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/xstd_729.txt')
# Import data from 9/18
xmean_918 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/xmeans_918.txt')
xstds_918 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/xstd_918.txt')
# Import data from 9/20
xmean_920 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/xmeans_920.txt')
xstds_920 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/xstd_920.txt')
# Import data from 9/21
xmean_921 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/frontview/xmeans_921.txt')
xstds_921 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/frontview/xstd_921.txt')

# Length of the hypotenuse in half bodylengths is 1
hype = 1
# Length of half bodylength in pixels
bodyLength = 135.601280856614

# Center data around the zero position for arms
xmean_729 = xmean_729 - xmean_729[1]
xmean_918 = xmean_918 - xmean_918[1]
xmean_920 = xmean_920 - xmean_920[1]
xmean_921 = xmean_921 - xmean_921[1]

xstds_729 = xstds_729 - xstds_729[1]
xstds_918 = xstds_918 - xstds_918[1]
xstds_920 = xstds_920 - xstds_920[1]
xstds_921 = xstds_921 - xstds_921[1]

# Re-establish the zero position is equal to zero
xmean_729[1] = 0
xmean_918[1] = 0
xmean_920[1] = 0
xmean_921[1] = 0

xstds_729[1] = 0
xstds_918[1] = 0
xstds_920[1] = 0
xstds_921[1] = 0

# Convert from Pixels to Body Lengths
mean_bl_729 = pixel_to_bl(xmean_729,bodyLength)
mean_bl_918 = pixel_to_bl(xmean_918,bodyLength)
mean_bl_920 = pixel_to_bl(xmean_920,bodyLength)
mean_bl_921 = pixel_to_bl(xmean_921,bodyLength)

stds_bl_729 = pixel_to_bl(xstds_729,bodyLength)
stds_bl_918 = pixel_to_bl(xstds_918,bodyLength)
stds_bl_920 = pixel_to_bl(xstds_920,bodyLength)
stds_bl_921 = pixel_to_bl(xstds_921,bodyLength)

# Convert Distances to Angles
angles_729 = np.arcsin(mean_bl_729) * (180 / np.pi) * -1
angles_918 = np.arcsin(mean_bl_918) * (180 / np.pi) * -1
angles_920 = np.arcsin(mean_bl_920) * (180 / np.pi) * -1
angles_921 = np.arcsin(mean_bl_921) * (180 / np.pi) * -1

# Impact velocity
# Best Fit Line for Y Direction
bestFit = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/linearFit.txt')
impactVelocity = bestFit[0]

t_bar_729 = get_t_bar(xmean_729)#,impactVelocity, 135.601280856614)
t_bar_918 = get_t_bar(xmean_918)#,impactVelocity, 135.601280856614)
t_bar_920 = get_t_bar(xmean_920)#,impactVelocity, 135.601280856614)
t_bar_921 = get_t_bar(xmean_921)#,impactVelocity, 135.601280856614)

# points for the x axis on graphs, aka time
plot_x = np.linspace(0,0.07,350)

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
#plt.ylim(-0.55,0.05)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/xStd_interp.png')

plot_x = np.linspace(0,0.03,150)

# Plot for the angles!
plt.figure()
plt.title('X Coordinates v. Time')
plt.xlabel('Non-Dimensional Time')
plt.ylabel('Angle in Degrees')
plt.plot(t_bar_729,angles_729,color='hotpink',label='0.0294 Nm')
plt.plot(t_bar_921,angles_921,color='mediumpurple',label='0.0153 Nm')
plt.plot(t_bar_920,angles_920,color='deepskyblue',label='0.0156 Nm')
plt.plot(t_bar_918,angles_918,color='springgreen',label='0.0136 Nm')
plt.legend(loc='upper left')
plt.xlim(0,1)
plt.ylim(0,20)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/angleszoom.png')
# Plot for the angles!
plt.figure()
plt.title('Change in Angle v. Time')
plt.xlabel('Non-Dimensional Time')
plt.ylabel('Angle in Degrees')
plt.plot(t_bar_729,angles_729,color='hotpink',label='0.0294 Nm')
plt.plot(t_bar_921,angles_921,color='mediumpurple',label='0.0153 Nm')
plt.plot(t_bar_920,angles_920,color='deepskyblue',label='0.0156 Nm')
plt.plot(t_bar_918,angles_918,color='springgreen',label='0.0136 Nm')
plt.legend(loc='upper left')
plt.xlim(0,2)
plt.ylim(0,60)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/angles.png')


print(';)')
