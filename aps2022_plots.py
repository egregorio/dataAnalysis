import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from get_t_bar import *
from conversions import *

#plt.plot(time_918,y_918_mean,color='springgreen',label='0.0136 Nm')
#plt.plot(time_920,y_920_mean,color='deepskyblue',label='0.0154 Nm')
#plt.plot(time_921,y_921_mean,color='mediumpurple',label='0.0153 Nm')

# Data for hinge diver models -- hinge / hips
hips_T136 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/9182021_hinge')
hips_T153 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/9212021_hinge')
hips_H10 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/10262021_hinge')
hips_H22 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/9202021_hinge')
hips_H28 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/10212021_hinge')
# Data for hinged diver models
data_T136 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/09182021_data')
data_T153 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/9212021_data')
data_H10 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/10262021_data')
data_H22 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/09202021_data')
data_H28 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/10212021_data')
# Import data from 04/04, no hinge, no hole
data_F22 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/04042022_data')
data_F10 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/04052022_a1_data')
data_F28 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/04052022_a3_data')

# Import and assign constants
exp_const = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/experiment_constants/constants.txt')
mass_diver = exp_const[0]
fall_bl    = exp_const[1]
spring_bl  = exp_const[2]
impact_v   = exp_const[4]

fall_shape = 2.5 / fall_bl
spring_shape = 2.5 / spring_bl

# Get all the dimensional values and convert meters to body lengths

time_T136 = data_T136[:,0] * fall_shape
std_T136 = data_T136[:,4] / fall_bl
mean_T136 = data_T136[:,3] / fall_bl
mean_T136 = mean_T136 - mean_T136[0]
mean_T136[0] = 0

time_T153 = data_T153[:,0] * fall_shape
std_T153 = data_T153[:,4] / fall_bl
mean_T153 = data_T153[:,3] / fall_bl
mean_T153 = mean_T153 - mean_T153[0]
mean_T153[0] = 0

time_H10 = data_H10[:,0] * fall_shape
std_H10 = data_H10[:,4] / fall_bl
mean_H10 = data_H10[:,3] / fall_bl
mean_H10 = mean_H10 - mean_H10[0]
mean_H10[0] = 0

time_H22 = data_H22[:,0] * fall_shape
std_H22 = data_H22[:,4] / fall_bl
mean_H22 = data_H22[:,3] / fall_bl
mean_H22 = mean_H22 - mean_H22[0]
mean_H22[0] = 0

time_H28 = data_H28[:,0] * fall_shape
std_H28 = data_H28[:,4] / fall_bl
mean_H28 = data_H28[:,3] / fall_bl
mean_H28 = mean_H28 - mean_H28[0]
mean_H28[0] = 0

time_F10 = data_F10[:,0] * spring_shape
std_F10 = data_F10[:,4] / spring_bl
mean_F10 = data_F10[:,3] / spring_bl
mean_F10 = mean_F10 - mean_F10[0]
mean_F10[0] = 0

time_F22 = data_F22[:,0] * spring_shape
std_F22 = data_F22[:,4] / spring_bl
mean_F22 = data_F22[:,3] / spring_bl
mean_F22 = mean_F22 - mean_F22[0]
mean_F22[0] = 0

time_F28 = data_F28[:,0] * spring_shape
std_F28 = data_F28[:,4] / spring_bl
mean_F28 = data_F28[:,3] / spring_bl
mean_F28 = mean_F28 - mean_F28[0]
mean_F28[0] = 0


# Plot for the STD in Y direction
plt.figure()
plt.title('Trajectory of Arms in Y Direction After Impact')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Depth (Arm Lengths)')
plt.errorbar(time_H28,mean_H28,yerr=std_H28,linestyle='-',fmt='limegreen',ecolor='lightgreen',elinewidth=3,label='28.6-Degree, Hinge')
plt.errorbar(time_H22,mean_H22,yerr=std_H22,linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='22.7-Degree, Hinge')
plt.errorbar(time_H10,mean_H10,yerr=std_H10,linestyle='-',fmt='black',ecolor='silver',elinewidth=3,label='10.4-Degree, Hinge')
plt.errorbar(time_F28,mean_F28,yerr=std_F28,linestyle='--',fmt='limegreen',ecolor='lightgreen',elinewidth=3,label='28.6-Degree, Fixed')
plt.errorbar(time_F22,mean_F22,yerr=std_F22,linestyle='--',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='22.7-Degree, Fixed')
plt.errorbar(time_F10,mean_F10,yerr=std_F10,linestyle='--',fmt='black',ecolor='silver',elinewidth=3,label='10.4-Degree, Fixed')
plt.legend(loc='lower left')
#plt.xlim(0,2)
#plt.ylim(-2,0)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/asymmetry_trajectory.png')#_error.png')

# Plot for the STD in Y direction
plt.figure()
plt.title('Trajectory of Arms in Y Direction After Impact')# for 22.7 Degree Models')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Depth (Arm Lengths)')
plt.errorbar(time_T136,mean_T136,yerr=std_T136,linestyle='-',fmt='mediumorchid',ecolor='thistle',elinewidth=3,label='0.00768Nm')
plt.errorbar(time_H22,mean_H22,yerr=std_H22,linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='0.0180Nm')
plt.errorbar(time_T153,mean_T153,yerr=std_T153,linestyle='-',fmt='darkcyan',ecolor='paleturquoise',elinewidth=3,label='0.0153Nm')
plt.errorbar(time_F22,mean_F22,yerr=std_F22,linestyle='--',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='Fixed')
plt.legend(loc='lower left')
#plt.xlim(0,2)
plt.ylim(-2,0)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/stiffness_trajectory.png')#_error.png')

time_T136 = 1 + hips_T136[:,0] * fall_shape
std_T136 = hips_T136[:,4] / fall_bl
mean_T136 = hips_T136[:,3] / fall_bl
mean_T136 = mean_T136 - mean_T136[0]
mean_T136[0] = 0

time_T153 = 1 + hips_T153[:,0] * fall_shape
std_T153 = hips_T153[:,4] / fall_bl
mean_T153 = hips_T153[:,3] / fall_bl
mean_T153 = mean_T153 - mean_T153[0]
mean_T153[0] = 0

time_H10 = 1 + hips_H10[:,0] * fall_shape
std_H10 = hips_H10[:,4] / fall_bl
mean_H10 = hips_H10[:,3] / fall_bl
mean_H10 = mean_H10 - mean_H10[0]
mean_H10[0] = 0

time_H22 = 1 + hips_H22[:,0] * fall_shape
std_H22 = hips_H22[:,4] / fall_bl
mean_H22 = hips_H22[:,3] / fall_bl
mean_H22 = mean_H22 - mean_H22[0]
mean_H22[0] = 0


time_H28 = 1 + hips_H28[:,0] * fall_shape
std_H28 = hips_H28[:,4] / fall_bl
mean_H28 = hips_H28[:,3] / fall_bl
mean_H28 = mean_H28 - mean_H28[0]
mean_H28[0] = 0

plt.figure()
plt.title('Trajectory of Arms in Y Direction After Impact')# for 22.7 Degree Models')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Depth (Arm Lengths)')
plt.errorbar(time_H28,mean_H28,yerr=std_H28,linestyle='-',fmt='limegreen',ecolor='lightgreen',elinewidth=3,label='28.6-Degree, Hinge')
plt.errorbar(time_H10,mean_H10,yerr=std_H10,linestyle='-',fmt='black',ecolor='silver',elinewidth=3,label='10.4-Degree, Hinge')
plt.errorbar(time_T136,mean_T136,yerr=std_T136,linestyle='-',fmt='mediumorchid',ecolor='thistle',elinewidth=3,label='0.00768Nm')
plt.errorbar(time_H22,mean_H22,yerr=std_H22,linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='0.0180Nm')
plt.errorbar(time_T153,mean_T153,yerr=std_T153,linestyle='-',fmt='darkcyan',ecolor='paleturquoise',elinewidth=3,label='0.0153Nm')
plt.legend(loc='lower left')
plt.xlim(1.5,2)
#plt.ylim(-2,0)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/hinge_trajectory.png')#_error.png')

#plt.plot(time_918,y_918_mean,color='springgreen',label='0.0136 Nm')
#plt.plot(time_920,y_920_mean,color='deepskyblue',label='0.0154 Nm')
#plt.plot(time_921,y_921_mean,color='mediumpurple',label='0.0153 Nm')

print(';)')
