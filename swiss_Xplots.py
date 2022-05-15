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
time_918 = data_918[:,0] * fall_shape
x_918_std = data_918[:,2] / fall_bl
x_918_std = x_918_std - x_918_std[0]
x_918_std[0] = 0
x_918_mean = data_918[:,1] / fall_bl
x_918_mean = x_918_mean - x_918_mean[0]
x_918_mean[0] = 0

time_920 = data_920[:,0] * fall_shape
x_920_std = data_920[:,2] / fall_bl
x_920_std = x_920_std - x_920_std[0]
x_920_std[0] = 0
x_920_mean = data_920[:,1] / fall_bl
x_920_mean = x_920_mean - x_920_mean[0]
x_920_mean[0] = 0

time_921 = data_921[:,0] * fall_shape
x_921_std = data_921[:,2] / fall_bl
x_921_std = x_921_std - x_921_std[0]
x_921_std[0] = 0
x_921_mean = data_921[:,1] / fall_bl
x_921_mean = x_921_mean - x_921_mean[1]
x_921_mean[0] = 0
x_921_mean[1] = 0
 
time_04 = data_04[:,0] * spring_shape
x_04_std = data_04[:,2] / fall_bl
x_04_std = x_04_std - x_04_std[0]
x_04_std[0] = 0
mean_04 = data_04[:,1] / spring_bl
mean_04 = mean_04 - mean_04[0]
mean_04[0] = 0

# Convert half body lengths to angles
angle_918 = np.arcsin(x_918_mean) * (180 / np.pi) * -1
std_918 = np.arcsin(x_918_std)    * (180 / np.pi) * -1


angle_920 = np.arcsin(x_920_mean) * (180 / np.pi) * -1
angle_921 = np.arcsin(x_921_mean) * (180 / np.pi) * -1
angle_404 = np.arcsin(mean_04)    * (180 / np.pi) * -1

std_920 = np.arcsin(x_920_std)    * (180 / np.pi) * -1
std_921 = np.arcsin(x_921_std)    * (180 / np.pi) * -1
std_404 = np.arcsin(x_04_std)    * (180 / np.pi) * -1

range_920 = np.where(angle_920 == max(angle_920))
range_921 = np.where(angle_921 == max(angle_921))
range_404 = np.where(angle_404 == max(angle_404))

max_404 = max(angle_404)

beforePlat920, length920 = beforePlateau(angle_920, max_404)
beforePlat921, length921 = beforePlateau(angle_921, max_404)

#print('4/4 i = ',int(range_404[0]),' 9/18 i = ',length918,' 9/20 i = ',length920,' 9/21 i = ',length921)
#print('4/4 i = ',data_04[int(range_404[0]),5],'9/18 i = ',data_918[length918,5],'9/20 i = ',data_920[length920,5],'9/21 i = ',data_921[length921,5])
#print('4/4 t = ',time_04[int(range_404[0])],'9/18 t = ',time_918[length918],'9/20 t = ',time_920[length920],'9/21 t = ',time_921[length921])

time7_20, length7_20 = beforeBL1(time_920,0.729)
time7_21, length7_21 = beforeBL1(time_921,0.839)
time7_04, length7_04 = beforeBL1(time_04,1.719)
print(length7_04)

#print(max(angle_404))
#print(angle_404[251])

#print('index of t = 1','4/4 = ',data_04[

# Plot for the STD in Y direction
plt.figure()
plt.title('Angle of Roll After Impact')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Angle of Bend in Degrees')
plt.errorbar(time_918,angle_918,std_918,fmt='darkgreen',ecolor='lightgreen',label='0.0136 Nm')
plt.errorbar(time_920,angle_920,std_920,fmt='darkblue',ecolor='lightskyblue',label='0.0154 Nm')
plt.errorbar(time_921,angle_921,std_921,fmt='indigo',ecolor='thistle',label='0.0153 Nm')
plt.errorbar(time_04, angle_404,std_404,fmt='mediumvioletred',ecolor='lightpink',label='No Hinge')
plt.legend(loc='upper left')
plt.xlim(0,3)
plt.ylim(0,80)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/x_afterImpact_full')

angle_918 = np.arcsin(x_918_mean[0:300]) * (180 / np.pi) * -1
std_918 = np.arcsin(x_918_std[0:300])    * (180 / np.pi) * -1
time_918 = time_918[0:300]
range_918 = np.where(angle_918 == max(angle_918))
beforePlat918, length918 = beforePlateau(angle_918, max_404)
time7_18, length7_18 = beforeBL1(time_918,0.669)
print(length7_18)


# Plot for the STD in Y direction
plt.figure()
plt.title('Angle of Roll After Impact')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Angle of Bend in Degrees')
plt.errorbar(time_918[0:range_918[0]],angle_918[0:range_918[0]],std_918[0:range_918[0]],fmt='darkgreen',ecolor='lightgreen',label='0.0136 Nm')
plt.errorbar(time_920[0:range_920[0]],angle_920[0:range_920[0]],std_920[0:range_920[0]],fmt='darkblue',ecolor='lightskyblue',label='0.0154 Nm')
plt.errorbar(time_921[0:range_921[0]],angle_921[0:range_921[0]],std_921[0:range_921[0]],fmt='indigo',ecolor='thistle',label='0.0153 Nm')
plt.errorbar(time_04[0:range_404[0]], angle_404[0:range_404[0]],std_404[0:range_404[0]],fmt='mediumvioletred',ecolor='lightpink',label='No Hinge')
plt.legend(loc='upper left')
plt.xlim(0,2)
plt.ylim(0,80)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/x_afterImpact_error.png')

# Plot for the STD in Y direction
plt.figure()
plt.title('Angle of Roll After Impact')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Angle of Bend in Degrees')
plt.plot(time_918[0:range_918[0]],angle_918[0:range_918[0]],color='springgreen',label='0.0136 Nm')
plt.plot(time_920[0:range_920[0]],angle_920[0:range_920[0]],color='deepskyblue',label='0.0154 Nm')
plt.plot(time_921[0:range_921[0]],angle_921[0:range_921[0]],color='mediumpurple',label='0.0153 Nm')
plt.plot(time_04[0:range_404[0]], angle_404[0:range_404[0]], color='hotpink',label='No Hinge')
plt.legend(loc='upper left')
plt.xlim(0,2.25)
plt.ylim(0,80)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/x_afterImpact.png')

# Plot for the STD in Y direction
plt.figure()
plt.title('Angle of Roll Stopping at Plateau')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Angle of Bend in Degrees')
plt.plot(time7_18,angle_918[0:length7_18],color='springgreen',label='0.0136 Nm, t* = 0.6')
plt.plot(time7_20,angle_920[0:length7_20],color='deepskyblue',label='0.0154 Nm, t* = 0.7')
plt.plot(time7_21,angle_921[0:length7_21],color='mediumpurple',label='0.0153 Nm, t* = 0.8')
plt.plot(time7_04,angle_404[0:length7_04],color='hotpink',label='No Hinge, t* = 1.7')
plt.legend(loc='lower right')
plt.xlim(0,2)
plt.ylim(0,8)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/x_afterImpact_stopAt9.png')

# Plot for the STD in Y direction
plt.figure()
plt.title('Angle of Roll for the First Body Length After Impact')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Angle of Bend in Degrees')
plt.plot(time_918,angle_918,color='springgreen',label='0.0136 Nm')
plt.plot(time_920,angle_920,color='deepskyblue',label='0.0154 Nm')
plt.plot(time_921,angle_921,color='mediumpurple',label='0.0153 Nm')
plt.plot(time_04, angle_404, color='hotpink',label='No Hinge')
plt.legend(loc='upper left')
plt.xlim(0,1)
plt.ylim(0,20)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/x_afterImpact_zoom.png')

# torque non d = ( mass * velocity * length ) / torque
fall_coefficient   = ( mass_diver * impact_v * fall_bl   )
spring_coefficient = ( mass_diver * impact_v * spring_bl )

nonD_918 = fall_coefficient / 0.0136
nonD_920 = fall_coefficient / 0.0154
nonD_921 = fall_coefficient / 0.0153

time_918 = data_918[:,0] * nonD_918
time_920 = data_920[:,0] * nonD_920
time_921 = data_921[:,0] * nonD_921

time_918 = time_918[0:300]


# Plot for the STD in Y direction
plt.figure()
plt.title('First Body Length in Y After Impact')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Depth (Arm Lengths)')
plt.plot(time_918,angle_918,color='springgreen',label='0.0136 Nm')
plt.plot(time_920,angle_920,color='deepskyblue',label='0.0154 Nm')
plt.plot(time_921,angle_921,color='mediumpurple',label='0.0153 Nm')
#plt.plot(time_04, mean_04, color='hotpink',label='No Hinge')
plt.legend()
plt.xlim(0,0.015)
plt.ylim(0,8)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/x_afterImpact_torque.png')

print(';)')
