import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from get_t_bar import *
from conversions import *

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

# Import impact velocity in body lengths
bestFit = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/linearFit.txt')
impactVelocity = bestFit[0]
# Body length in pixels
bodyLength = 135.601280856614

ymean_729 = ymean_729 - ymean_729[0]
ymean_918 = ymean_918 - ymean_918[0]
ymean_920 = ymean_920 - ymean_920[0]
ymean_921 = ymean_921 - ymean_921[0]

ymean_729[0] = 0
ymean_918[0] = 0
ymean_920[0] = 0
ymean_921[0] = 0

ystds_729 = ystds_729 - ystds_729[0]
ystds_918 = ystds_918 - ystds_918[0]
ystds_920 = ystds_920 - ystds_920[0]
ystds_921 = ystds_921 - ystds_921[0]

ystds_729[0] = 0
ystds_918[0] = 0
ystds_920[0] = 0
ystds_921[0] = 0

t_bar_729 = frames_to_t_bar(ymean_729,impactVelocity, bodyLength)
t_bar_918 = frames_to_t_bar(ymean_918,impactVelocity, bodyLength)
t_bar_920 = frames_to_t_bar(ymean_920,impactVelocity, bodyLength)
t_bar_921 = frames_to_t_bar(ymean_921,impactVelocity, bodyLength)

mean_bl_729 = pixel_to_bl(ymean_729,bodyLength)
mean_bl_918 = pixel_to_bl(ymean_918,bodyLength)
mean_bl_920 = pixel_to_bl(ymean_920,bodyLength)
mean_bl_921 = pixel_to_bl(ymean_921,bodyLength)

stds_bl_729 = pixel_to_bl(ystds_729,bodyLength)
stds_bl_918 = pixel_to_bl(ystds_918,bodyLength)
stds_bl_920 = pixel_to_bl(ystds_920,bodyLength)
stds_bl_921 = pixel_to_bl(ystds_921,bodyLength)

linearF = get_linearFit(impactVelocity,t_bar_918)

# points for the x axis on graphs, aka time
plot_x = np.linspace(0,0.07,350)



# Plot for the STD in Y direction
plt.figure()
plt.title('Depth v. Time')
plt.xlabel('Non-Dimensional Time')
plt.ylabel('Depth in Half Body Lengths')
plt.errorbar(t_bar_918,mean_bl_918,yerr=stds_bl_918,fmt='k',ecolor='springgreen',label='0.0136 Nm')
plt.errorbar(t_bar_920,mean_bl_920,yerr=stds_bl_920,fmt='k',ecolor='deepskyblue',label='0.0156 Nm')
plt.errorbar(t_bar_921,mean_bl_921,yerr=stds_bl_921,fmt='k',ecolor='mediumpurple',label='0.0153 Nm')
plt.errorbar(t_bar_729,mean_bl_729,yerr=stds_bl_729,fmt='k',ecolor='hotpink',label='0.0294 Nm')
#plt.plot(t_bar_918,linearF,color='r',linewidth=2)
plt.legend()
plt.xlim(0,2)
plt.ylim(-2,0)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/yStd_interp.png')

print(';)')
