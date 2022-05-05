import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from get_t_bar import *
from conversions import *

# Import data from 7/29
data_729 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/7292021_data')
# Import data from 9/18
data_918 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/9182021_data')
# Import data from 9/20
data_920 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/9202021_data')
# Import data from 9/21
data_921 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/9212021_data')
# Import data from 04/04, no hinge, no hole
data_04 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/04042022_data')

# Body length in meters
bodyLength = 0.0623644234696804

# Get all the dimensional values and convert meters to body lengths
time_729 = data_729[:,0]
y_729_mean = data_729[:,3]# / bodyLength

time_918 = data_918[:,0]
y_918_mean = data_918[:,3]# / bodyLength

time_920 = data_920[:,0]
y_920_mean = data_920[:,3]# / bodyLength

time_921 = data_921[:,0]
y_921_mean = data_921[:,3]# / bodyLength
y_921_mean[0] = 0

time_04 = data_04[:,0]
mean_04 = data_04[:,3]# / bodyLength

# Plot for the STD in Y direction
plt.figure()
plt.title('After Impact')
plt.xlabel('Time (s)')
plt.ylabel('Depth (m)')
plt.plot(time_918,y_918_mean,color='springgreen',label='0.0136 Nm')
plt.plot(time_920,y_920_mean,color='deepskyblue',label='0.0156 Nm')
plt.plot(time_921,y_921_mean,color='mediumpurple',label='0.0153 Nm')
plt.plot(time_729,y_729_mean,color='hotpink',label='0.0294 Nm')
plt.plot(time_04, mean_04, color='orangered',label='No Hinge')
plt.legend()
#plt.xlim(0,2)
plt.ylim(-2.5,0)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/y_afterImpact.png')

best_fit_data = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/beforeImpact_linearFit.txt')
slope_fit = best_fit_data[0]
plot_fit = np.linspace(-0.05,0.05,1000)
best_fit = get_linearFit(slope_fit,plot_fit)

# Plot for the STD in Y direction
plt.figure()
plt.title('After Impact')
plt.xlabel('Time (s)')
plt.ylabel('Depth (m)')
plt.plot(time_918,y_918_mean,color='springgreen',label='0.0136 Nm')
plt.plot(time_920,y_920_mean,color='deepskyblue',label='0.0156 Nm')
plt.plot(time_921,y_921_mean,color='mediumpurple',label='0.0153 Nm')
plt.plot(time_729,y_729_mean,color='hotpink',label='0.0294 Nm')
plt.plot(time_04, mean_04, color='gold',label='No Hinge')
#plt.plot(plot_fit,best_fit,color='crimson',label='V = 2.3m/s')
plt.legend()
plt.xlim(0,0.05)
plt.ylim(-0.15,0)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/y_afterImpact_zoom.png')

print(';)')
