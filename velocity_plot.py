import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
#from scipy.interpolate import CubicSpline
from get_t_bar import *
from conversions import *

# Import data from 9/18
data_918 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/9182021_data')
# Import data from 9/20
data_920 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/9202021_data')
# Import data from 9/21
data_921 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/9212021_data')
# Import data from 04/04, no hinge, no hole
data_404 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/04042022_data')

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

time_404 = data_404[:,0] * spring_shape
y_404_mean = data_404[:,3] / spring_bl
y_404_mean = y_404_mean - y_404_mean[0]
y_404_mean[0] = 0

velocity_918 = np.diff(y_918_mean)/np.diff(time_918)*-1
velocity_920 = np.diff(y_920_mean)/np.diff(time_920)*-1
velocity_921 = np.diff(y_921_mean)/np.diff(time_921)*-1
velocity_404 = np.diff(y_404_mean)/np.diff(time_404)*-1

save_path = '/Users/elizabeth/Box Sync/dataAnalysis/data_to_plot'
save_array = zip(velocity_918, velocity_920, velocity_921, velocity_404)
please_save = os.path.join(save_path,'velocity_arrays')
np.savetxt(please_save,save_array)

print(len(velocity_918),len(time_918))


def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

print(len(velocity_918),len(time_918[0:-3]))

plt.figure()
plt.title('Y Velocity After Impact')
plt.xlabel('Non Dimensional Time ( T = t * v / l )')
plt.ylabel('Velocity (Arm Length / T )')
plt.plot(time_918[0:-1],velocity_918,'o',color='springgreen',label='0.0136 Nm')
plt.plot(time_920[0:-1],velocity_920,'o',color='deepskyblue',label='0.0154 Nm')
plt.plot(time_921[0:-1],velocity_921,'o',color='mediumpurple',label='0.0153 Nm')
plt.plot(time_404[0:-1],velocity_404,'o',color='hotpink',label='No Hinge')
plt.xlim(0,1.0)
plt.ylim(0,2)
plt.legend(loc='lower left')
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/velocity_points.png')

velocity_918 = moving_average(velocity_918, n=20)
velocity_920 = moving_average(velocity_920, n=20)
velocity_921 = moving_average(velocity_921, n=20)
velocity_404 = moving_average(velocity_404, n=20)

plt.figure()
plt.title('Y Velocity After Impact')
plt.xlabel('Non Dimensional Time ( T = t * v / l )')
plt.ylabel('Velocity (Arm Length / T )')
plt.plot(time_918[0:-20],velocity_918,color='springgreen',label='0.0136 Nm')
plt.plot(time_920[0:-20],velocity_920,color='deepskyblue',label='0.0154 Nm')
plt.plot(time_921[0:-20],velocity_921,color='mediumpurple',label='0.0153 Nm')
plt.plot(time_404[0:-20],velocity_404,color='hotpink',label='No Hinge')
plt.xlim(0,1.0)
plt.ylim(0,2)
plt.legend(loc='lower left')
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/velocity.png')


