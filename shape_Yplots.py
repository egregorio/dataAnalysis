import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from get_t_bar import *
from conversions import *

# Import data from 9/18
data_918 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/9182021_data')
# Import data from 9/20
data_920 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/9202021_data')
# Import data from 9/21
data_921 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/9212021_data')
# Import data from 04/04, no hinge, no hole
data_04 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/04042022_data')
# Import data from 04/04, no hinge, no hole
data_405_a1 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/04052022_asym1')
# Import data from 04/04, no hinge, no hole
data_1021 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/10212021_data')
# Import data from 04/04, no hinge, no hole
data_1026 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/10262021_data')

# Import and assign constants
exp_const = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/experiment_constants/constants.txt')
mass_diver = exp_const[0]
fall_bl    = exp_const[1]
spring_bl  = exp_const[2]
impact_v   = exp_const[3]

fall_shape = impact_v / fall_bl
spring_shape = impact_v / spring_bl

# Get all the dimensional values and convert meters to body lengths
time_918 = data_918[:,0] * fall_shape
y_918_std = data_918[:,4] / fall_bl
y_918_std = y_918_std - y_918_std[0]
y_918_std[0] = 0
y_918_mean = data_918[:,3] / fall_bl
y_918_mean = y_918_mean - y_918_mean[0]
y_918_mean[0] = 0

time_920 = data_920[:,0] * fall_shape
y_920_std = data_920[:,4] / fall_bl
y_920_std = y_920_std - y_920_std[0]
y_920_std[0] = 0
y_920_mean = data_920[:,3] / fall_bl
y_920_mean = y_920_mean - y_920_mean[0]
y_920_mean[0] = 0

time_921 = data_921[:,0] * fall_shape
y_921_std = data_921[:,4] / fall_bl
y_921_std = y_921_std - y_921_std[0]
y_921_std[0] = 0
y_921_mean = data_921[:,3] / fall_bl
y_921_mean[0] = 0
y_921_mean = y_921_mean - y_921_mean[0]
y_921_mean[0] = 0

time_1021 = data_1021[:,0] * fall_shape
y_1021_std = data_1021[:,4] / fall_bl
y_1021_std = y_1021_std - y_1021_std[0]
y_1021_std[0] = 0
y_1021_mean = data_1021[:,3] / fall_bl
y_1021_mean[0] = 0
y_1021_mean = y_1021_mean - y_1021_mean[0]
y_1021_mean[0] = 0

time_1026 = data_1026[:,0] * fall_shape
y_1026_std = data_1026[:,4] / fall_bl
y_1026_std = y_1026_std - y_1026_std[0]
y_1026_std[0] = 0
y_1026_mean = data_1026[:,3] / fall_bl
y_1026_mean[0] = 0
y_1026_mean = y_1026_mean - y_1026_mean[0]
y_1026_mean[0] = 0

time_04 = data_04[:,0] * spring_shape
y_04_std = data_04[:,4] / fall_bl
y_04_std = y_04_std - y_04_std[0]
y_04_std[0] = 0
mean_04 = data_04[:,3] / spring_bl
mean_04 = mean_04 - mean_04[0]
mean_04[0] = 0

time_405_a1 = data_405_a1[:,0] * spring_shape
y_405_a1_std = data_405_a1[:,4] / fall_bl
y_405_a1_std = y_405_a1_std - y_405_a1_std[0]
y_405_a1_std[0] = 0
mean_405_a1 = data_405_a1[:,3] / spring_bl
mean_405_a1 = mean_405_a1 - mean_405_a1[0]
mean_405_a1[0] = 0

time1_04, length1_04 = beforeBL1(time_04,1.09)
time1_18, length1_18 = beforeBL1(time_918,1.09)

print('4/4 i = ',length1_04,' 9/18 i = ',length1_18)

# Plot for the STD in Y direction
plt.figure()
plt.title('Movement of Arms in Y Direction After Impact')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Depth (Arm Lengths)')
plt.errorbar(time_918,y_918_mean,y_918_std,fmt='darkgreen',ecolor='lightgreen',label='0.0136 Nm')
plt.errorbar(time_920,y_920_mean,y_920_std,fmt='darkblue',ecolor='lightskyblue',label='0.0154 Nm')
plt.errorbar(time_921,y_921_mean,y_921_std,fmt='indigo',ecolor='thistle',label='0.0153 Nm')
plt.errorbar(time_1021,y_1021_mean,y_1021_std,fmt='darkred',ecolor='lightcoral',label='10/21')
plt.errorbar(time_1026,y_1026_mean,y_1026_std,fmt='saddlebrown',ecolor='burlywood',label='10/26')
plt.errorbar(time_04, mean_04,y_04_std, fmt='mediumvioletred',ecolor='lightpink',label='No Hinge')
plt.errorbar(time_405_a1, mean_405_a1,y_405_a1_std, fmt='mediumvioletred',ecolor='lightpink',label='No Hinge')
plt.legend()
plt.xlim(0,3)
plt.ylim(-2,0)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/y_afterImpact_shape_error.png')

# Plot for the STD in Y direction
plt.figure()
plt.title('Movement of Arms in Y Direction After Impact')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Depth (Arm Lengths)')
plt.plot(time_918,y_918_mean,color='springgreen',label='0.0136 Nm')
plt.plot(time_920,y_920_mean,color='deepskyblue',label='0.0154 Nm')
plt.plot(time_921,y_921_mean,color='mediumpurple',label='0.0153 Nm')
plt.plot(time_1021,y_1021_mean,color='red',label='10/21')
plt.plot(time_1026,y_1026_mean,color='darkorange',label='10/26')
plt.plot(time_04, mean_04, color='hotpink',label='No Hinge')
plt.plot(time_405_a1, mean_405_a1,color='green',label='No Hinge')
plt.legend()
plt.xlim(0,3)
plt.ylim(-2,0)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/y_afterImpact_shape.png')

# Plot for the STD in Y direction
plt.figure()
plt.title('Movement of Arms in Y Direction After Impact')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Depth (Arm Lengths)')
plt.plot(time_918,y_918_mean,color='springgreen',label='0.0136 Nm')
plt.plot(time_920,y_920_mean,color='deepskyblue',label='0.0154 Nm')
plt.plot(time_921,y_921_mean,color='mediumpurple',label='0.0153 Nm')
plt.plot(time_1021,y_1021_mean,color='red',label='10/21')
plt.plot(time_1026,y_1026_mean,color='darkorange',label='10/26')
plt.plot(time_04, mean_04, color='hotpink',label='No Hinge')
plt.legend()
plt.xlim(0,0.8)
plt.ylim(-1,0)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/y_afterImpact_shape_zoom.png')

best_fit_data = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/beforeImpact_linearFit.txt')
slope_fit = best_fit_data[0]
plot_fit = np.linspace(-0.05,0.05,1000)
best_fit = get_linearFit(slope_fit,plot_fit)


print(';)')
