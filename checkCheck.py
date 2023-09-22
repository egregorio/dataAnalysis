import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from get_t_bar import *

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
x_918_std = data_918[:,2]# / fall_bl
x_918_std = x_918_std# - x_918_std[0]
std_918 = x_918_std
x_918_mean = data_918[:,1]# / fall_bl
x_918_mean = x_918_mean - x_918_mean[0]
x_918_mean[0] = 0

time_920 = data_920[:,0] * fall_shape
x_920_std = data_920[:,2] #/ fall_bl
x_920_std = x_920_std# - x_920_std[0]
std_920 = x_920_std
x_920_mean = data_920[:,1] #/ fall_bl
x_920_mean = x_920_mean - x_920_mean[0]
x_920_mean[0] = 0

time_921 = data_921[:,0] * fall_shape
x_921_std = data_921[:,2] #/ fall_bl
x_921_std = x_921_std# - x_921_std[0]
std_921 = x_921_std
x_921_mean = data_921[:,1] #/ fall_bl
x_921_mean = x_921_mean - x_921_mean[1]
x_921_mean[0] = 0
x_921_mean[1] = 0
 
time_1021 = data_1021[:,0] * fall_shape
x_1021_std = data_1021[:,2] #/ fall_bl
x_1021_std = x_1021_std# - x_1021_std[0]
std_1021 = x_1021_std
x_1021_mean = data_1021[:,1] #/ fall_bl
x_1021_mean = x_1021_mean - x_1021_mean[1]
x_1021_mean[0] = 0
 
time_1026 = data_1026[:,0] * fall_shape
x_1026_std = data_1026[:,2] #/ fall_bl
x_1026_std = x_1026_std# - x_1026_std[0]
std_1026 = x_1026_std
x_1026_mean = data_1026[:,1] #/ fall_bl
x_1026_mean = x_1026_mean - x_1026_mean[1]
x_1026_mean[0] = 0
 

switch_H28 = np.argmin(x_1021_mean)
switch_S3 = np.argmin(x_918_mean[:-60])
switch_S2 = np.argmin(x_920_mean)
switch_S1 = np.argmin(x_921_mean)
switch_H10 = np.argmin(x_1026_mean)

x_array = [x_1021_mean,x_918_mean,x_920_mean,x_921_mean,x_1026_mean]
std_array = [std_1021,std_918,std_920,std_921,std_1026]
max_array = [switch_H28, switch_S3, switch_S2, switch_S1, switch_H10]
angle_array = [x_1021_mean,x_918_mean,x_920_mean,x_921_mean,x_1026_mean]
std_angle = [std_1021,std_918,std_920,std_921,std_1026]

print(angle_array[1][100])

for i in range(0,len(x_array)):
	index_at_90 = max_array[i]
		
	alpha_i = x_array[i][:]
	alpha_m = x_array[i][index_at_90]
	std = std_array[i][:]

	alpha = abs( alpha_i / alpha_m )
	theta = np.arcsin(alpha)

	sigma = np.arcsin(std / alpha_m)

	angle_array[i][:] = theta
	std_angle[i][:] = sigma

#print(angle_array[1][100])
#print(std_angle[1][100])

angle_1021 = angle_array[0] * ( 180 / np.pi )
angle_918  = angle_array[1] * ( 180 / np.pi )
angle_920  = angle_array[2] * ( 180 / np.pi )
angle_921  = angle_array[3] * ( 180 / np.pi )
angle_1026 = angle_array[4] * ( 180 / np.pi )


std_1021 = std_angle[0] * ( 180 / np.pi )
std_918  = std_angle[1] * ( 180 / np.pi )
std_920  = std_angle[2] * ( 180 / np.pi )
std_921  = std_angle[3] * ( 180 / np.pi )
std_1026 = std_angle[4] * ( 180 / np.pi )


angle_1021[switch_H28:] = 180 - angle_1021[switch_H28:]
angle_918[switch_S3:] = 180 - angle_918[switch_S3:]
angle_920[switch_S2:] = 180 - angle_920[switch_S2:]
angle_921[switch_S1:] = 180 - angle_921[switch_S1:]
angle_1026[switch_H10:] = 180 - angle_1026[switch_H10:]



# Plot for the STD in Y direction
plt.figure()
plt.errorbar(time_1021,angle_1021,yerr=std_1021,linestyle='-',fmt='limegreen',ecolor='lightgreen',elinewidth=3,label='W28')
plt.errorbar(time_918,angle_918,yerr=std_918,linestyle='-',fmt='mediumorchid',ecolor='thistle',elinewidth=3,label='W22 S3: 0.00768 Nm')
plt.errorbar(time_920,angle_920,yerr=std_920,linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='W22 S2: 0.0180 Nm')
plt.errorbar(time_921,angle_921,yerr=std_921,linestyle='-',fmt='darkcyan',ecolor='paleturquoise',elinewidth=3,label='W22 S1: 0.0153 Nm')
plt.errorbar(time_1026,angle_1026,yerr=std_1026,linestyle='-',fmt='black',ecolor='silver',elinewidth=3,label='W10')
#plt.axhline(y = 110,linestyle='--')
#plt.legend(loc='lower left')
plt.xlim(0,5)
plt.ylim(0,120)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/all_angle.png')

# Plot for the STD in Y direction
plt.figure()
plt.errorbar(time_920,angle_920,yerr=std_920,linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='W22 S2: 0.0180 Nm')
#plt.axhline(y = 110,linestyle='--')
#plt.legend(loc='lower left')
plt.xlim(0,3)
plt.ylim(0,120)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/time_series_angle.png')

pinch_off = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/pinch_off/pinch_off_time.txt',skiprows=1)
H10_pinch_off = 2.5 / ( pinch_off[0] + fall_bl )
F10_pinch_off = 2.5 / ( pinch_off[1] + spring_bl )
T136_pinch_off = 2.5 / ( pinch_off[2] + fall_bl )
H22_pinch_off = 2.5 / ( pinch_off[3] + fall_bl )
T153_pinch_off = 2.5 / ( pinch_off[4] + fall_bl )
F22_pinch_off = 2.5 / ( pinch_off[5] + spring_bl )
H28_pinch_off = 2.5 / ( pinch_off[6] + fall_bl )
F28_pinch_off = 2.5 / ( pinch_off[7] + spring_bl )

nonD_H10 = data_1026[:,0] * H10_pinch_off
nonD_F10 = data_1[:,0] * F10_pinch_off
nonD_T136 = data_918[:,0] * T136_pinch_off
nonD_H22 = data_920[:,0] * H22_pinch_off
nonD_T153 = data_921[:,0] * T153_pinch_off
nonD_F22 = data_04[:,0] * F22_pinch_off
nonD_H28 = data_1021[:,0] * H28_pinch_off
nonD_F28 = data_3[:,0] * F28_pinch_off

# Plot for the STD in Y direction
plt.figure()
plt.errorbar(nonD_T136[:-50],angle_918[:-50],yerr=std_918[:-50],linestyle='-',fmt='mediumorchid',ecolor='thistle',elinewidth=3,label='W22 S3')
plt.errorbar(nonD_H22,angle_920,yerr=std_920,linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='W22 S2')
plt.errorbar(nonD_T153,angle_921,yerr=std_921,linestyle='-',fmt='darkcyan',ecolor='paleturquoise',elinewidth=3,label='W22 S1')
plt.errorbar(nonD_H28[:-50],angle_1021[:-50],yerr=std_1021[:-50],linestyle='-',fmt='limegreen',ecolor='lightgreen',elinewidth=3,label='W28')
plt.errorbar(nonD_H10,angle_1026,yerr=std_1026,linestyle='-',fmt='black',ecolor='silver',elinewidth=3,label='W10')
#plt.legend(loc='upper left')
plt.xlim(0,2)
plt.ylim(0,120)
#plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/dissertation plots/pinchOff_angle.png')#_error.png')
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/pinch_off/pinchOff_angle.png')#_error.png')

time_to_turn = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/\
time_to_turn_depth.txt')
H28_time_to_turn = time_to_turn[0]
T136_time_to_turn = time_to_turn[1]
H22_time_to_turn = time_to_turn[2]
T153_time_to_turn = time_to_turn[3]
H10_time_to_turn = time_to_turn[4]

time_918 = data_918[:,0] * fall_shape
time_920 = data_920[:,0] * fall_shape
time_921 = data_921[:,0] * fall_shape
time_1021 = data_1021[:,0] * fall_shape
time_1026 = data_1026[:,0] * fall_shape

nonD_H28 = time_1021 / H28_time_to_turn
nonD_H22 = time_920 / H22_time_to_turn
nonD_T136 = time_918 / T136_time_to_turn
nonD_T153 = time_921 / T153_time_to_turn
nonD_H10 = time_1026 / H10_time_to_turn

# Plot for the STD in Y direction
plt.figure()
plt.errorbar(nonD_H28[:-50],angle_1021[:-50],yerr=std_1021[:-50],linestyle='-',fmt='limegreen',ecolor='lightgreen',elinewidth=3,label='W28')
plt.errorbar(nonD_T136[:-50],angle_918[:-50],yerr=std_918[:-50],linestyle='-',fmt='mediumorchid',ecolor='thistle',elinewidth=3,label='W22 S3')
plt.errorbar(nonD_H22,angle_920,yerr=std_920,linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='W22 S2')
plt.errorbar(nonD_T153,angle_921,yerr=std_921,linestyle='-',fmt='darkcyan',ecolor='paleturquoise',elinewidth=3,label='W22 S1')
plt.errorbar(nonD_H10,angle_1026,yerr=std_1026,linestyle='-',fmt='black',ecolor='silver',elinewidth=3,label='W10')
#plt.legend(loc='upper left')
plt.xlim(0,1.2)
plt.ylim(0,120)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/\
timeTurn_angle.png')#_error.png')

print(';)')
