import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from get_t_bar import *
from conversions import *

# Import data from 9/18
data_918 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/9182021_data')
# Import data from 9/20
data_920 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/9202021_data')
# Import data from 9/21
data_921 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/9212021_data')

# Import and assign constants
exp_const = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/experiment_constants/constants.txt')
mass_diver = exp_const[0]
fall_bl    = exp_const[1]
impact_v   = exp_const[3]

fall_shape = impact_v / fall_bl

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

# Convert half body lengths to angles
angle_918 = np.arcsin(x_918_mean) * (180 / np.pi) * -1
std_918 = np.arcsin(x_918_std)    * (180 / np.pi) * -1

angle_920 = np.arcsin(x_920_mean) * (180 / np.pi) * -1
std_920 = np.arcsin(x_920_std)    * (180 / np.pi) * -1
range_920 = np.where(angle_920 == max(angle_920))

angle_921 = np.arcsin(x_921_mean) * (180 / np.pi) * -1
std_921 = np.arcsin(x_921_std)    * (180 / np.pi) * -1
range_921 = np.where(angle_921 == max(angle_921))


angle_918 = np.arcsin(x_918_mean[0:300]) * (180 / np.pi) * -1
std_918 = np.arcsin(x_918_std[0:300])    * (180 / np.pi) * -1
time_918 = time_918[0:300]
range_918 = np.where(angle_918 == max(angle_918))

# Plot for the STD in Y direction
plt.figure()
plt.title('Angle of Roll After Impact, Averaged Over All Trials')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Angle of Bend in Degrees')
plt.plot(angle_918[0:range_918[0]],color='springgreen',label='0.0136 Nm')
plt.plot(angle_920[0:range_920[0]],color='deepskyblue',label='0.0154 Nm')
plt.plot(angle_921[0:range_921[0]],color='mediumpurple',label='0.0153 Nm')
plt.legend(loc='upper left')
#plt.xlim(0,2.25)
plt.ylim(0,80)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/for moment - fall 2021/angle_afterImpact.png')

# Plot for the STD in Y direction
plt.figure()
plt.title('Angle of Roll After Impact First Ten Frames, Averaged Over All Trials')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Angle of Bend in Degrees')
plt.plot(angle_918[0:50],color='springgreen',label='9/18')
plt.plot(angle_920[0:50],color='deepskyblue',label='9/20')
plt.plot(angle_921[0:50],color='mediumpurple',label='9/21')
plt.legend(loc='upper left')
#plt.xlim(0,2.25)
#plt.ylim(0,80)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/for moment - fall 2021/angle_first ten.png')


# Import data from 9/18
x_918 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/for moment - fall 2021/dimensional data/09182021_allData_X')
# Import data from 9/20
x_920 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/for moment - fall 2021/dimensional data/09202021_allData_X')
# Import data from 9/21
x_921 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/for moment - fall 2021/dimensional data/09212021_allData_X')


def findAngle(x_array,radius):
	shape = np.shape(x_array)
	trials = shape[0]
	frames = shape[1]
	angle_array = []
	for i in range(0,trials):
		this_trial = [0]
		for j in range(1,frames):
			opposite = x_array[i,j]
			opposite = opposite - x_array[i,0]
			oh = opposite / radius
			theta = np.arcsin(oh) * (180 / np.pi) * -1
			this_trial.append(theta)
		angle_array.append(this_trial)
	return angle_array

a_918 = findAngle(x_918,fall_bl)	
a_920 = findAngle(x_920,fall_bl)	
a_921 = findAngle(x_921,fall_bl)	


plt.figure()
plt.title('Angle of Roll After Impact, All Trials')
plt.xlabel('Frames')
plt.ylabel('Angle of Bend in Degrees')
plt.plot(a_918[0])
plt.plot(a_918[1])
plt.plot(a_918[2])
plt.plot(a_918[3])
plt.plot(a_918[4])
plt.plot(a_918[5])
plt.plot(a_918[6])
plt.plot(a_918[7])
plt.plot(a_918[8])
plt.plot(a_918[9])
plt.plot(a_918[10])
plt.plot(a_918[11])
plt.plot(a_918[12])
plt.plot(a_920[0])
plt.plot(a_920[1])
plt.plot(a_920[2])
plt.plot(a_920[3])
plt.plot(a_920[4])
plt.plot(a_920[5])
plt.plot(a_920[6])
plt.plot(a_920[7])
plt.plot(a_920[8])
plt.plot(a_920[9])
plt.plot(a_920[10])
plt.plot(a_920[11])
plt.plot(a_920[12])
plt.plot(a_920[13])
plt.plot(a_920[14])
plt.plot(a_920[15])
plt.plot(a_920[16])
plt.plot(a_921[0])
plt.plot(a_921[1])
plt.plot(a_921[2])
plt.plot(a_921[3])
plt.plot(a_921[4])
plt.plot(a_921[5])
plt.plot(a_921[6])
plt.plot(a_921[7])
plt.plot(a_921[8])
plt.plot(a_921[9])
plt.ylim(-5,5)
plt.xlim(0,50)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/for moment - fall 2021/angle_all.png')


print(';)')
