import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from get_t_bar import *
from conversions import *

# Import data from 9/18
data_918 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/09182021_data')
# Import data from 9/20
data_920 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/09202021_data')
# Import data from 9/21
data_921 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/9212021_data')
# Import data from 10/21
data_1021 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/10212021_data')
# Import data from 10/26
data_1026 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/10262021_data')
# Import data from 04/04, no hinge, no hole
data_04 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/04042022_data')
# Import data from 04/05, no hinge, no hole
data_1 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/04052022_asym1_data')
# Import data from 04/05, no hinge, no hole
data_3 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/04052022_asym3_data')

# Import and assign constants
exp_const = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/experiment_constants/constants.txt')
mass_diver = exp_const[0]
fall_bl    = exp_const[1]
spring_bl  = exp_const[2]
impact_v   = exp_const[3]

fall_shape = 2.5 / fall_bl
#fall_torque = 
spring_shape = 2.5 / spring_bl
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
 
time_1021 = data_1021[:,0] * fall_shape
x_1021_std = data_1021[:,2] / fall_bl
x_1021_std = x_1021_std - x_1021_std[0]
x_1021_std[0] = 0
x_1021_mean = data_1021[:,1] / fall_bl
x_1021_mean = x_1021_mean - x_1021_mean[1]
x_1021_mean[0] = 0
 
time_1026 = data_1026[:,0] * fall_shape
x_1026_std = data_1026[:,2] / fall_bl
x_1026_std = x_1026_std - x_1026_std[0]
x_1026_std[0] = 0
x_1026_mean = data_1026[:,1] / fall_bl
x_1026_mean = x_1026_mean - x_1026_mean[1]
x_1026_mean[0] = 0
 
time_04 = data_04[:,0] * spring_shape
x_04_std = data_04[:,2] / spring_bl
x_04_std = x_04_std - x_04_std[0]
x_04_std[0] = 0
mean_04 = data_04[:,1] / spring_bl
mean_04 = mean_04 - mean_04[0]
mean_04[0] = 0

time_1 = data_1[:,0] * spring_shape
x_1_std = data_1[:,2] / spring_bl
x_1_std = x_1_std - x_1_std[0]
x_1_std[0] = 0
mean_1 = data_1[:,1] / spring_bl
mean_1 = mean_1 - mean_1[0]
mean_1[0] = 0

time_3 = data_3[:,0] * spring_shape
x_3_std = data_3[:,2] / spring_bl
x_3_std = x_3_std - x_3_std[0]
x_3_std[0] = 0
mean_3 = data_3[:,1] / spring_bl
mean_3 = mean_3 - mean_3[0]
mean_3[0] = 0


# Convert half body lengths to angles
angle_918 = np.arcsin(x_918_mean) * (180 / np.pi) * -1
std_918 = np.arcsin(x_918_std)    * (180 / np.pi) * -1

angle_920 = np.arcsin(x_920_mean) * (180 / np.pi) * -1
std_920 = np.arcsin(x_920_std)    * (180 / np.pi) * -1

angle_921 = np.arcsin(x_921_mean) * (180 / np.pi) * -1
std_921 = np.arcsin(x_921_std)    * (180 / np.pi) * -1

angle_1021 = np.arcsin(x_1021_mean) * (180 / np.pi) * -1
std_1021 = np.arcsin(x_1021_std)    * (180 / np.pi) * -1

angle_1026 = np.arcsin(x_1026_mean) * (180 / np.pi) * -1
std_1026 = np.arcsin(x_1026_std)    * (180 / np.pi) * -1

angle_404 = np.arcsin(mean_04)    * (180 / np.pi) * -1
std_404 = np.arcsin(x_04_std)    * (180 / np.pi) * -1

angle_1 = np.arcsin(mean_1)    * (180 / np.pi) * -1
std_1 = np.arcsin(x_1_std)    * (180 / np.pi) * -1

angle_3 = np.arcsin(mean_3)    * (180 / np.pi) * -1
std_3 = np.arcsin(x_3_std)    * (180 / np.pi) * -1


range_920 = np.where(angle_920 == max(angle_920))
range_921 = np.where(angle_921 == max(angle_921))
range_1021 = np.where(angle_1021 == max(angle_1021))
range_1026 = np.where(angle_1026 == max(angle_1026))
range_404 = np.where(angle_404 == max(angle_404))
range_1 = np.where(angle_1 == max(angle_1))
range_3 = np.where(angle_3 == max(angle_3))


# Plot for the STD in Y direction
plt.figure()
plt.title('Angle of Roll After Impact')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Angle of Bend in Degrees')
plt.errorbar(time_918,angle_918,yerr=std_918,linestyle='-',fmt='mediumorchid',ecolor='thistle',elinewidth=3,label='0.00768 Nm')
plt.errorbar(time_920,angle_920,yerr=std_920,linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='0.0180 Nm')
plt.errorbar(time_921,angle_921,yerr=std_921,linestyle='-',fmt='darkcyan',ecolor='paleturquoise',elinewidth=3,label='0.0153 Nm')
plt.errorbar(time_04, angle_404,yerr=std_404,linestyle='--',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='Fixed')
plt.legend(loc='upper left')
plt.xlim(0,2)
plt.ylim(0,80)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/all_trials/stiffness_angle.png')

# Plot for the STD in Y direction
plt.figure()
plt.title('Angle of Roll After Impact')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Angle of Bend in Degrees')
plt.errorbar(time_1021,angle_1021,yerr=std_1021,linestyle='-',fmt='limegreen',ecolor='lightgreen',elinewidth=3,label='28.6-Degree, Hinge')
plt.errorbar(time_920,angle_920,yerr=std_920,linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='22.7-Degree, Hinge')
plt.errorbar(time_1026,angle_1026,yerr=std_1026,linestyle='-',fmt='black',ecolor='silver',elinewidth=3,label='10.4-Degree, Hinge')
plt.errorbar(time_3, angle_3,yerr=std_3,linestyle='--',fmt='limegreen',ecolor='lightgreen',elinewidth=3,label='28.6-Degree, Fixed')
plt.errorbar(time_04, angle_404,yerr=std_404,linestyle='--',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='22.7-Degree, Fixed')
plt.errorbar(time_1, angle_1,yerr=std_1,linestyle='--',fmt='black',ecolor='silver',elinewidth=3,label='10.4-Degree, Fixed')
plt.legend(loc='upper left')
plt.xlim(0,2)
plt.ylim(0,80)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/all_trials/asymmetric_angle.png')

print(';)')
