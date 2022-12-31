import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from conversions import *

# Import data from 7/29
data_729 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/7292021_beforeImpact')
# Import data from 9/18
data_918 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/9182021_beforeImpact')
# Import data from 9/20
data_920 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/9202021_beforeImpact')
# Import data from 9/21
data_921 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/9212021_beforeImpact')

# Get all the dimensional values and convert meters to body lengths
time_729 = data_729[:,0]
time_729 = time_729[-100:-1]
time_729 = time_729 - time_729[0]
time_729[0] = 0
y_729_mean = data_729[:,1]
y_729_mean = y_729_mean[-100:-1]
y_729_mean = y_729_mean - y_729_mean[0]
y_729_mean[0] = 0

time_918 = data_918[:,0]
time_918 = time_918[0:100]
y_918_mean = data_918[:,1]
y_918_mean = y_918_mean[0:100]
y_918_mean = y_918_mean - y_918_mean[0]
y_918_mean[0] = 0

time_920 = data_920[:,0]
time_920 = time_920[0:100]
y_920_mean = data_920[:,1]
y_920_mean = y_920_mean[0:100]
y_920_mean = y_920_mean - y_920_mean[0]
y_920_mean[0] = 0

time_921 = data_921[:,0]
time_921 = time_921[-100:-1]
time_921 = time_921 - time_921[0]
time_921[0] = 0
y_921_mean = data_921[:,1]
y_921_mean = y_921_mean[-100:-1]
y_921_mean = y_921_mean - y_921_mean[0]
y_921_mean[0] = 0

# Find the linear interpolations of the imported data
slope_729, b_729 = np.polyfit(time_729,y_729_mean,1)
slope_918, b_918 = np.polyfit(time_918,y_918_mean,1)
slope_920, b_920 = np.polyfit(time_920,y_920_mean,1)
slope_921, b_921 = np.polyfit(time_921,y_921_mean,1)

linearF_729 = get_linearFit(slope_729,time_729)
linearF_918 = get_linearFit(slope_918,time_918)
linearF_920 = get_linearFit(slope_920,time_920)
linearF_921 = get_linearFit(slope_921,time_921)

mean_m = np.mean([slope_729, slope_918, slope_920, slope_921])
mean_b = np.mean([b_729, b_918, b_920, b_921])
stds_m = np.std([slope_729, slope_918, slope_920, slope_921])
stds_b = np.std([b_729, b_918, b_920, b_921])

print(mean_m)

saveData = [mean_m, mean_b]

np.savetxt('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/beforeImpact_linearFit.txt',saveData)

linearF = get_linearFit(mean_m,time_918)

# Plot for the STD in Y direction
plt.figure()
plt.title('Before Impact')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.plot(time_729,y_729_mean,color='hotpink',label='0.0294 Nm')
plt.plot(time_918,y_918_mean,color='springgreen',label='0.0136 Nm')
plt.plot(time_920,y_920_mean,color='deepskyblue',label='0.0156 Nm')
plt.plot(time_921,y_921_mean,color='mediumpurple',label='0.0153 Nm')
plt.plot(time_918,linearF,color='r',linewidth=2,label='V = 2.3 m/s')
plt.legend()
#plt.xlim(0,2)
#plt.ylim(-2,0)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/beforeImpact.png')

# Import data from 7/29
data_a729 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/7292021_data')
# Import data from 9/18
data_a918 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/9182021_data')
# Import data from 9/20
data_a920 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/9202021_data')
# Import data from 9/21
data_a921 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/9212021_data')

time_a729 = data_a729[:,0]
y_a729_mean = data_a729[:,3]
y_a729_mean = y_a729_mean - y_a729_mean[0]
y_a729_mean[0] = 0
time_a918 = data_a918[:,0]
y_a918_mean = data_a918[:,3]
y_a918_mean = y_a918_mean - y_a918_mean[0]
y_a918_mean[0] = 0
time_a920 = data_a920[:,0]
y_a920_mean = data_a920[:,3]
y_a920_mean = y_a920_mean - y_a920_mean[0]
y_a920_mean[0] = 0
time_a921 = data_a921[:,0]
y_a921_mean = data_a921[:,3]
y_a921_mean = y_a921_mean - y_a921_mean[1]
y_a921_mean[0] = 0
y_a921_mean[1] = 0

plot_fit = np.linspace(-0.01,0,10)
best_fit = get_linearFit(mean_m,plot_fit)


# Plot for the STD in Y direction
plt.figure()
plt.title('Impact')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.plot(time_a729,y_a729_mean,color='hotpink',label='0.0294 Nm')
plt.plot(time_a918,y_a918_mean,color='springgreen',label='0.0136 Nm')
plt.plot(time_a920,y_a920_mean,color='deepskyblue',label='0.0156 Nm')
plt.plot(time_a921,y_a921_mean,color='mediumpurple',label='0.0153 Nm')
plt.plot(plot_fit,best_fit,color='r',linewidth=2,label='V = 2.3 m/s')
plt.legend()
plt.xlim(-0.01,0.04)
plt.ylim(-0.02,0.03)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/Impact.png')


print(';)')
