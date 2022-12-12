import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from get_t_bar import *
from conversions import *
import os

# Import data from 9/18
data_918 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/9182021_data')
# Import data from 04/04, no hinge, no hole
data_04 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/04042022_data')

# Import and assign constants
exp_const = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/experiment_constants/constants.txt')
mass_diver = exp_const[0]
fall_bl    = exp_const[1]
spring_bl  = exp_const[2]
impact_v   = exp_const[4]

fall_shape = impact_v / fall_bl
spring_shape = impact_v / spring_bl

# Get all the dimensional values and convert meters to body lengths 9/18
time_918 = data_918[:,0] * fall_shape

x_918_std = data_918[:,2] / fall_bl
x_918_std = x_918_std - x_918_std[0]
x_918_std[0] = 0
x_918_mean = data_918[:,1] / fall_bl
x_918_mean = x_918_mean - x_918_mean[0]
x_918_mean[0] = 0

y_918_std = data_918[:,4] / fall_bl
y_918_std = y_918_std - y_918_std[0]
y_918_std[0] = 0
y_918_mean = data_918[:,3] / fall_bl
y_918_mean = y_918_mean - y_918_mean[0]
y_918_mean[0] = 0
y_918_mean = y_918_mean[0:300]
# Get all the dimensional values and convert meters to body lengths 4/4
time_04 = data_04[:,0] * spring_shape

x_04_std = data_04[:,2] / fall_bl
x_04_std = x_04_std - x_04_std[0]
x_04_std[0] = 0
mean_04 = data_04[:,1] / spring_bl
mean_04 = mean_04 - mean_04[0]
mean_04[0] = 0

y_04_std = data_04[:,4] / fall_bl
y_04_std = y_04_std - y_04_std[0]
y_04_std[0] = 0
y_04_mean = data_04[:,3] / spring_bl
y_04_mean = y_04_mean - y_04_mean[0]
y_04_mean[0] = 0.00001

# Convert half body lengths to angles
angle_404 = np.arcsin(mean_04)    * (180 / np.pi) * -1
std_404 = np.arcsin(x_04_std)    * (180 / np.pi) * -1
range_404 = np.where(angle_404 == max(angle_404))
max_404 = max(angle_404)
time7_04, length7_04 = beforeBL1(time_04,1.719)

angle_918 = np.arcsin(x_918_mean[0:300]) * (180 / np.pi) * -1
std_918 = np.arcsin(x_918_std[0:300])    * (180 / np.pi) * -1
time_918 = time_918[0:300]

time_404 = data_04[:,0] * spring_shape

path_918 = '/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/hinge video'

for i in range(0,len(time_918)):
	fig, (ax1, ax2) = plt.subplots(2,figsize=(6,7.5))
	ax1.set_title('Trajectory of Arms in Y Direction After Impact')
	ax1.set_ylabel('Depth in Arm Lengths')
	ax1.plot(time_918,y_918_mean,color='seagreen',label='0.0136 Nm')
	ax1.plot(time_918[i],y_918_mean[i],'go')
	ax1.set_xlim(0,2)
	ax2.set_title('Angle of Roll After Impact')
	ax2.plot(time_918,angle_918,color='seagreen',label='0.0136 Nm')
	ax2.plot(time_918[i],angle_918[i],'go')
	ax2.set_xlim(0,2)
	ax2.set_xlabel('Non-Dimensional Time ( t * v / l )')
	ax2.set_ylabel('Angle of Bend in Degrees')
        please_save_918 = os.path.join(path_918,str(i))
	plt.savefig(please_save_918)
	i = i + 1

#path_404 = '/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/no hinge video'

#for i in range(0,len(time_918)):
#	fig, (ax1, ax2) = plt.subplots(2,figsize=(6,7.5))
#	ax1.set_title('Trajectory of Arms in Y Direction After Impact')
#	ax1.set_ylabel('Depth in Arm Lengths')
#	ax1.plot(time_404,y_04_mean,color='mediumvioletred',label='No Hinge')
#	ax1.plot(time_404[i],y_04_mean[i],'o',color='deeppink')
#	ax1.set_xlim(0,1.5)
#	ax2.set_title('Angle of Roll After Impact')
#	ax2.plot(time_404,angle_404,color='mediumvioletred',label='No Hinge')
#	ax2.plot(time_404[i],angle_404[i],'o',color='deeppink')
#	ax2.set_xlim(0,1.5)
#	ax2.set_xlabel('Non-Dimensional Time ( t * v / l )')
#	ax2.set_ylabel('Angle of Bend in Degrees')
#       please_save_404 = os.path.join(path_404,str(i))
#	plt.savefig(please_save_404)
#	i = i + 1


print(';)')
