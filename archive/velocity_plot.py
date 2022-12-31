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
# Import data from 04/04, no hinge, no hole
data_405 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/04052022_asym1')

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

time_405 = data_405[:,0] * spring_shape
y_405_mean = data_405[:,3] / spring_bl
y_405_mean = y_405_mean - y_405_mean[0]
y_405_mean[0] = 0

velocity_918 = np.diff(y_918_mean)/np.diff(time_918)*-1
velocity_920 = np.diff(y_920_mean)/np.diff(time_920)*-1
velocity_921 = np.diff(y_921_mean)/np.diff(time_921)*-1
velocity_404 = np.diff(y_404_mean)/np.diff(time_404)*-1
velocity_405 = np.diff(y_405_mean)/np.diff(time_405)*-1

save_path = '/Users/elizabeth/Box Sync/dataAnalysis/data_to_plot'
save_array = zip(velocity_918, velocity_920, velocity_921, velocity_404)
please_save = os.path.join(save_path,'velocity_arrays')
np.savetxt(please_save,save_array)



def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


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
velocity_405 = moving_average(velocity_405, n=20)

print(velocity_404[0],velocity_404[-1])

plt.figure()
plt.title('Y Velocity After Impact')
plt.xlabel('Non Dimensional Time ( T = t * v / l )')
plt.ylabel('Velocity (Arm Length / T )')
plt.plot(time_918[0:-155],velocity_918[0:-135],color='springgreen',label='0.0136 Nm')
plt.plot(time_920[0:-145],velocity_920[0:-125],color='deepskyblue',label='0.0154 Nm')
plt.plot(time_921[0:-62],velocity_921[0:-42],color='mediumpurple',label='0.0153 Nm')
#plt.plot(time_404[0:-20],velocity_404,color='hotpink',label='No Hinge')
plt.xlim(0,2.0)
#plt.ylim(0,2)
plt.legend(loc='lower left')
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/velocity_hinge.png')

plt.figure()
plt.title('Y Velocity After Impact')
plt.xlabel('Non Dimensional Time ( T = t * v / l )')
plt.ylabel('Velocity (Arm Length / T )')
plt.plot(time_918[0:-155],velocity_918[0:-135],color='springgreen',label='0.0136 Nm')
plt.plot(time_920[0:-145],velocity_920[0:-125],color='deepskyblue',label='0.0154 Nm')
plt.plot(time_921[0:-62],velocity_921[0:-42],color='mediumpurple',label='0.0153 Nm')
plt.axhline(y=1.17)
plt.plot(time_404[0:-20],velocity_404,color='hotpink',label='No Hinge')
plt.plot(time_405[0:-20],velocity_405,color='hotpink',label='No Hinge')
plt.xlim(0,2.0)
#plt.ylim(0,2)
plt.legend(loc='lower left')
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/velocity.png')

# torque non d = ( mass * velocity * length ) / torque
fall_coefficient   = ( mass_diver * impact_v * fall_bl   )
spring_coefficient = ( mass_diver * impact_v * spring_bl )

nonD_918 = fall_coefficient / 0.0136
nonD_920 = fall_coefficient / 0.0154
nonD_921 = fall_coefficient / 0.0153

time_918 = data_918[:,0] * nonD_918
time_920 = data_920[:,0] * nonD_920
time_921 = data_921[:,0] * nonD_921

velocity_918 = np.diff(y_918_mean)/np.diff(time_918)*-1
velocity_920 = np.diff(y_920_mean)/np.diff(time_920)*-1
velocity_921 = np.diff(y_921_mean)/np.diff(time_921)*-1
velocity_404 = np.diff(y_404_mean)/np.diff(time_404)*-1

velocity_918 = moving_average(velocity_918, n=20)
velocity_920 = moving_average(velocity_920, n=20)
velocity_921 = moving_average(velocity_921, n=20)
velocity_404 = moving_average(velocity_404, n=20)

print(np.argmin(velocity_918))
print(np.argmin(velocity_920))
print(np.argmin(velocity_921))

plt.figure()
plt.title('Y Velocity After Impact')
plt.xlabel('Non Dimensional Time ( T = t * ( m v l ) / tau )')
plt.ylabel('Velocity (Arm Length / T )')
plt.plot(time_918[0:-155],velocity_918[0:-135],color='springgreen',label='0.0136 Nm')
plt.plot(time_920[0:-145],velocity_920[0:-125],color='deepskyblue',label='0.0154 Nm')
plt.plot(time_921[0:-65],velocity_921[0:-45],color='mediumpurple',label='0.0153 Nm')
#plt.xlim(0,1.0)
#plt.ylim(0,2)
plt.legend(loc='lower left')
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/velocity_torque.png')


