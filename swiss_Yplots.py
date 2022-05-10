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

# Import and assign constants
exp_const = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/experiment_constants/constants.txt')
mass_diver = exp_const[0]
fall_bl    = exp_const[1]
spring_bl  = exp_const[2]
impact_v   = exp_const[3]

fall_shape = impact_v / fall_bl
#fall_torque = 
spring_shape = impact_v / spring_bl
#spring_torque = 

# Get all the dimensional values and convert meters to body lengths
time_729 = data_729[:,0] * fall_shape
y_729_mean = data_729[:,3] / fall_bl
y_729_mean = y_729_mean - y_729_mean[0]
y_729_mean[0] = 0

time_918 = data_918[:,0] * fall_shape
y_918_mean = data_918[:,3] / fall_bl
y_918_mean = y_918_mean - y_918_mean[0]
y_918_mean[0] = 0

time_920 = data_920[:,0] * fall_shape
y_920_mean = data_920[:,3] / fall_bl
y_920_mean = y_920_mean - y_920_mean[0]
y_920_mean[0] = 0

time_921 = data_921[:,0] * fall_shape
y_921_mean = data_921[:,3] / fall_bl
y_921_mean[0] = 0
y_921_mean = y_921_mean - y_921_mean[0]
y_921_mean[0] = 0

time_04 = data_04[:,0] * spring_shape
mean_04 = data_04[:,3] / spring_bl
mean_04 = mean_04 - mean_04[0]
mean_04[0] = 0

time1_04, length1_04 = beforeBL1(time_04,2.09)
time1_18, length1_18 = beforeBL1(time_04,2.09)

print('4/4 i = ',length1_04,' 9/18 i = ',length1_18)

# Plot for the STD in Y direction
plt.figure()
plt.title('After Impact')
plt.xlabel('Time (s)')
plt.ylabel('Depth (m)')
plt.plot(time_918,y_918_mean,color='springgreen',label='0.0136 Nm')
plt.plot(time_920,y_920_mean,color='deepskyblue',label='0.0156 Nm')
plt.plot(time_921,y_921_mean,color='mediumpurple',label='0.0153 Nm')
#plt.plot(time_729,y_729_mean,color='hotpink',label='0.0294 Nm')
plt.plot(time_04, mean_04, color='hotpink',label='No Hinge')
plt.legend()
plt.xlim(0,3)
plt.ylim(-2,0)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/y_afterImpact.png')

best_fit_data = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/beforeImpact_linearFit.txt')
slope_fit = best_fit_data[0]
plot_fit = np.linspace(-0.05,0.05,1000)
best_fit = get_linearFit(slope_fit,plot_fit)

# Plot for the STD in Y direction
plt.figure()
plt.title('After Impact')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Depth (Arm Lengths)')
plt.plot(time_918,y_918_mean,color='springgreen',label='0.0136 Nm')
plt.plot(time_920,y_920_mean,color='deepskyblue',label='0.0156 Nm')
plt.plot(time_921,y_921_mean,color='mediumpurple',label='0.0153 Nm')
#plt.plot(time_729,y_729_mean,color='hotpink',label='0.0294 Nm')
plt.plot(time_04, mean_04, color='hotpink',label='No Hinge')
#plt.plot(plot_fit,best_fit,color='crimson',label='V = 2.3m/s')
plt.legend()
plt.xlim(0,1)
plt.ylim(-1.4,0)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/y_afterImpact_zoom.png')

print(';)')
