import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import glob
import os
from get_t_bar import *

# Data for impact velocity hinge diver models -- hinge / hips
vel_918 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/9182021_hinge')
vel_921 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/9212021_hinge')
vel_H10 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/10262021_hinge')
vel_H22 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/9202021_hinge')
vel_H28 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/10212021_hinge')
# Data for hinge diver models -- hinge / hips
hips_S3 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/hipsData/09182021_hipsData')
hips_S2 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/hipsData/09202021_hipsData')
hips_S1 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/hipsData/09212021_hipsData')
hips_W28 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/hipsData/10212021_hipsData')
hips_W10 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/hipsData/10262021_hipsData')
hips_W17 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/hipsData/08172022_hipsData')
# Data for hinged diver models
data_S3 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/09182021_data')
data_S2 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/09202021_data')
data_S1 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/09212021_data')
data_W28 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/10212021_data')
data_W17 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/08172022_data')
data_W10 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/10262021_data')

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

#feet_time   = [ feet_W28[:,0], feet_S3[:,0], feet_S2[:,0], feet_S1[:,0], feet_W17[:,0], feet_W10[:,0] ]
#feet_X_mean = [ feet_W28[:,1], feet_S3[:,1], feet_S2[:,1], feet_S1[:,1], feet_W17[:,1], feet_W10[:,1] ]
#feet_X_stds = [ feet_W28[:,2], feet_S3[:,2], feet_S2[:,2], feet_S1[:,2], feet_W17[:,2], feet_W10[:,2] ]
#feet_Y_mean = [ feet_W28[:,3], feet_S3[:,3], feet_S2[:,3], feet_S1[:,3], feet_W17[:,3], feet_W10[:,3] ]
#feet_Y_stds = [ feet_W28[:,4], feet_S3[:,4], feet_S2[:,4], feet_S1[:,4], feet_W17[:,4], feet_W10[:,4] ]

hips_time   = [ hips_W28[:,0], hips_S3[:,0], hips_S2[:,0], hips_S1[:,0], hips_W17[:,0], hips_W10[:,0] ]
hips_X_mean = [ hips_W28[:,1], hips_S3[:,1], hips_S2[:,1], hips_S1[:,1], hips_W17[:,1], hips_W10[:,1] ]
hips_X_stds = [ hips_W28[:,2], hips_S3[:,2], hips_S2[:,2], hips_S1[:,2], hips_W17[:,2], hips_W10[:,2] ]
hips_Y_mean = [ hips_W28[:,3], hips_S3[:,3], hips_S2[:,3], hips_S1[:,3], hips_W17[:,3], hips_W10[:,3] ]
hips_Y_stds = [ hips_W28[:,4], hips_S3[:,4], hips_S2[:,4], hips_S1[:,4], hips_W17[:,4], hips_W10[:,4] ]

arms_time   = [ data_W28[:,0], data_S3[:,0], data_S2[:,0], data_S1[:,0], data_W17[:,0], data_W10[:,0] ]
arms_X_mean = [ data_W28[:,1], data_S3[:,1], data_S2[:,1], data_S1[:,1], data_W17[:,1], data_W10[:,1] ]
arms_X_stds = [ data_W28[:,2], data_S3[:,2], data_S2[:,2], data_S1[:,2], data_W17[:,2], data_W10[:,2] ]
arms_Y_mean = [ data_W28[:,3], data_S3[:,3], data_S2[:,3], data_S1[:,3], data_W17[:,3], data_W10[:,3] ]
arms_Y_stds = [ data_W28[:,4], data_S3[:,4], data_S2[:,4], data_S1[:,4], data_W17[:,4], data_W10[:,4] ]


# Get all the dimensional values and convert meters to body lengths
for i in range(0,6):
	hips_time[i][:] = hips_time[i][:] * fall_shape# + 1
	arms_time[i][:] = arms_time[i][:] * fall_shape

	hips_X_stds[i][:] = hips_X_stds[i][:] - hips_X_stds[i][0]
	hips_X_stds[i][0] = 0
	arms_X_stds[i][:] = arms_X_stds[i][:] - arms_X_stds[i][0]
	arms_X_stds[i][0] = 0

	hips_X_mean[i][:] = hips_X_mean[i][:] - hips_X_mean[i][0]
	hips_X_mean[i][0] = 0
	arms_X_mean[i][:] = arms_X_mean[i][:] - arms_X_mean[i][0]
	arms_X_mean[i][0] = 0

	hips_Y_stds[i][:] = hips_Y_stds[i][:] / fall_bl
	arms_Y_stds[i][:] = arms_Y_stds[i][:] / fall_bl

	hips_Y_mean[i][:] = hips_Y_mean[i][:] / fall_bl
	hips_Y_mean[i][:] = hips_Y_mean[i][:] - hips_Y_mean[i][0]
	hips_Y_mean[i][0] = 0
	arms_Y_mean[i][:] = arms_Y_mean[i][:] / fall_bl
	arms_Y_mean[i][:] = arms_Y_mean[i][:] - arms_Y_mean[i][0]
	arms_Y_mean[i][0] = 0

#print('H_28 = ',switch_H28,' S3 = ',switch_S3,' S2 = ',switch_S2,' S1 = ',switch_S1,' N1 = ',switch_N1,' N2 = ',switch_N2,' H10 = ',switch_H10)

for i in range(0,6):
	switch = np.argmin(arms_X_mean[i][:-60])
	arms_X_mean[i][:] = 90 * ( arms_X_mean[i][:] / arms_X_mean[i][switch] )
	hips_X_mean[i][:] = 90 * ( hips_X_mean[i][:] / arms_X_mean[i][switch] )


arms_time_W28 = arms_time[0][:]; hips_time_W28 = hips_time[0][:]
arms_time_S3  = arms_time[1][:]; hips_time_S3  = hips_time[1][:]
arms_time_S2  = arms_time[2][:]; hips_time_S2  = hips_time[2][:]
arms_time_S1  = arms_time[3][:]; hips_time_S1  = hips_time[3][:]
arms_time_W17 = arms_time[4][:]; hips_time_W17 = hips_time[4][:]
arms_time_W10 = arms_time[5][:]; hips_time_W10 = hips_time[5][:]
print(len(arms_time_W28),len(arms_time_W10))

arms_X_W28 = arms_X_mean[0][:]; arms_sX_W28 = arms_X_stds[0][:]
arms_X_S3  = arms_X_mean[1][:]; arms_sX_S3  = arms_X_stds[1][:]
arms_X_S2  = arms_X_mean[2][:]; arms_sX_S2  = arms_X_stds[2][:]
arms_X_S1  = arms_X_mean[3][:]; arms_sX_S1  = arms_X_stds[3][:]
arms_X_W17 = arms_X_mean[4][:]; arms_sX_W17 = arms_X_stds[4][:]
arms_X_W10 = arms_X_mean[5][:]; arms_sX_W10 = arms_X_stds[5][:]

hips_X_W28 = hips_X_mean[0][:]; hips_sX_W28 = hips_X_stds[0][:]
hips_X_S3  = hips_X_mean[1][:]; hips_sX_S3  = hips_X_stds[1][:]
hips_X_S2  = hips_X_mean[2][:]; hips_sX_S2  = hips_X_stds[2][:]
hips_X_S1  = hips_X_mean[3][:]; hips_sX_S1  = hips_X_stds[3][:]
hips_X_W17 = hips_X_mean[4][:]; hips_sX_W17 = hips_X_stds[4][:]
hips_X_W10 = hips_X_mean[5][:]; hips_sX_W10 = hips_X_stds[5][:]


plt.figure()
#plt.errorbar(arms_time_W28,arms_X_W28,yerr=arms_sX_W28,linestyle='-',fmt='limegreen',ecolor='lightgreen',elinewidth=3,label='W28')
plt.errorbar(hips_time_W28,hips_X_W28,yerr=hips_sX_W28,linestyle='-',fmt='limegreen',ecolor='lightgreen',elinewidth=3)#,label='W28')
#plt.errorbar(arms_time_S3, arms_X_S3, yerr=arms_sX_S3, linestyle='-',fmt='mediumorchid',ecolor='thistle',elinewidth=3,label='W22 S3')
plt.errorbar(hips_time_S3, hips_X_S3, yerr=hips_sX_S3, linestyle='-',fmt='mediumorchid',ecolor='thistle',elinewidth=3)#,label='W22 S3')
#plt.errorbar(arms_time_S2, arms_X_S2, yerr=arms_sX_S2, linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='W22 S2')
plt.errorbar(hips_time_S2, hips_X_S2, yerr=hips_sX_S2, linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3)#,label='W22 S2')
#plt.errorbar(arms_time_S1, arms_X_S1, yerr=arms_sX_S1, linestyle='-',fmt='darkcyan',ecolor='paleturquoise',elinewidth=3,label='W22 S1')
plt.errorbar(hips_time_S1, hips_X_S1, yerr=hips_sX_S1, linestyle='-',fmt='darkcyan',ecolor='paleturquoise',elinewidth=3)#,label='W22 S1')
#plt.errorbar(arms_time_W17,arms_X_W17,yerr=arms_sX_W17,linestyle='-',fmt='firebrick',ecolor='mistyrose',elinewidth=3,label='W17')
plt.errorbar(hips_time_W17,hips_X_W17,yerr=hips_sX_W17,linestyle='-',fmt='firebrick',ecolor='mistyrose',elinewidth=3)#,label='W17')
#plt.errorbar(arms_time_W10,arms_X_W10,yerr=arms_sX_W10,linestyle='-',fmt='black',ecolor='silver',elinewidth=3,label='W10')
plt.errorbar(hips_time_W10,hips_X_W10,yerr=hips_sX_W10,linestyle='-',fmt='black',ecolor='silver',elinewidth=3)#,label='W10')
#plt.legend()
#plt.xlim(0,1)
#plt.ylim(0,60)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/dissertation plots/\
angle_hips.png')#_error.png')

arms_Y_W28 = arms_Y_mean[0][:]; arms_sY_W28 = arms_Y_stds[0][:]
arms_Y_S3  = arms_Y_mean[1][:]; arms_sY_S3  = arms_Y_stds[1][:]
arms_Y_S2  = arms_Y_mean[2][:]; arms_sY_S2  = arms_Y_stds[2][:]
arms_Y_S1  = arms_Y_mean[3][:]; arms_sY_S1  = arms_Y_stds[3][:]
arms_Y_W17 = arms_Y_mean[4][:]; arms_sY_W17 = arms_Y_stds[4][:]
arms_Y_W10 = arms_Y_mean[5][:]; arms_sY_W10 = arms_Y_stds[5][:]

hips_Y_W28 = hips_Y_mean[0][:]; hips_sY_W28 = hips_Y_stds[0][:]
hips_Y_S3  = hips_Y_mean[1][:]; hips_sY_S3  = hips_Y_stds[1][:]
hips_Y_S2  = hips_Y_mean[2][:]; hips_sY_S2  = hips_Y_stds[2][:]
hips_Y_S1  = hips_Y_mean[3][:]; hips_sY_S1  = hips_Y_stds[3][:]
hips_Y_W17 = hips_Y_mean[4][:]; hips_sY_W17 = hips_Y_stds[4][:]
hips_Y_W10 = hips_Y_mean[5][:]; hips_sY_W10 = hips_Y_stds[5][:]




fig, ax1 = plt.subplots()
#plt.axvline(x = 2.084478022, linestyle='--',color='k')# Angle S1
#plt.axvline(x = 2.259615385, linestyle='-',color='k')# Depth S1
#plt.axvline(x = 1.960447201, linestyle='--',color='k')# Angle S2
#plt.axvline(x = 2.112792297, linestyle='-',color='k')# Depth S2
#plt.axvline(x = 1.83218707, linestyle='--',color='k')# Angle S3
#plt.axvline(x = 2.013755158, linestyle='-',color='k')# Depth S3
#plt.axvline(x = 1.675788723, linestyle='--',color='k')# Angle W28
#plt.axvline(x = 1.869325997, linestyle='-',color='k')# Depth W28
#plt.axvline(x = 2.71933129, linestyle='--',color='k')# Angle W17
#plt.axvline(x = 2.879120879, linestyle='-',color='k')# Depth W17
plt.axvline(x = 4.13395663, linestyle='--',color='k')# Angle W10
plt.axvline(x = 4.050894085, linestyle='-',color='k')# Depth W10
#ax1.errorbar(arms_time_W28,arms_Y_W28,yerr=arms_sY_W28,linestyle='-',fmt='limegreen',ecolor='lightgreen',elinewidth=3,label='W28')
#ax1.errorbar(arms_time_S3, arms_Y_S3, yerr=arms_sY_S3, linestyle='-',fmt='mediumorchid',ecolor='thistle',elinewidth=3,label='W22 S3')
#ax1.errorbar(arms_time_S2, arms_Y_S2, yerr=arms_sY_S2, linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3)#,label='W22 S2')
#ax1.errorbar(arms_time_S1, arms_Y_S1, yerr=arms_sY_S1, linestyle='-',fmt='darkcyan',ecolor='paleturquoise',elinewidth=3)#,label='W22 S1')
#ax1.errorbar(arms_time_W17,arms_Y_W17,yerr=arms_sY_W17,linestyle='-',fmt='firebrick',ecolor='mistyrose',elinewidth=3,label='W17')
ax1.errorbar(arms_time_W10,arms_Y_W10,yerr=arms_sY_W10,linestyle='-',fmt='black',ecolor='silver',elinewidth=3,label='W10')
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
#ax2.errorbar(arms_time_W28,arms_X_W28,yerr=arms_sX_W28,linestyle='-',fmt='limegreen',ecolor='lightgreen',elinewidth=3)#,label='W28')
#ax2.errorbar(arms_time_S3, arms_X_S3, yerr=arms_sX_S3, linestyle='-',fmt='mediumorchid',ecolor='thistle',elinewidth=3)#,label='W22 S3')
#ax2.errorbar(arms_time_S2, arms_X_S2, yerr=arms_sX_S2, linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='W22 S2')
#ax2.errorbar(arms_time_S1, arms_X_S1, yerr=arms_sX_S1, linestyle='-',fmt='darkcyan',ecolor='paleturquoise',elinewidth=3,label='W22 S1')
#ax2.errorbar(arms_time_W17,arms_X_W17,yerr=arms_sX_W17,linestyle='-',fmt='firebrick',ecolor='mistyrose',elinewidth=3)#,label='W17')
ax2.errorbar(arms_time_W10,arms_X_W10,yerr=arms_sX_W10,linestyle='-',fmt='black',ecolor='silver',elinewidth=3)#,label='W10')
#plt.legend()
plt.xlim(0,5)
#plt.ylim(0,60)
#fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/dissertation plots/\
angle_and_depth_W10.png')#_error.png')


plt.figure()
#plt.errorbar(arms_time_W28,arms_Y_W28,yerr=arms_sY_W28,linestyle='-',fmt='limegreen',ecolor='lightgreen',elinewidth=3,label='W28')
plt.errorbar(hips_time_W28,hips_Y_W28,yerr=hips_sY_W28,linestyle='-',fmt='limegreen',ecolor='lightgreen',elinewidth=3)#,label='W28')
#plt.errorbar(arms_time_S3, arms_Y_S3, yerr=arms_sY_S3, linestyle='-',fmt='mediumorchid',ecolor='thistle',elinewidth=3,label='W22 S3')
plt.errorbar(hips_time_S3, hips_Y_S3, yerr=hips_sY_S3, linestyle='-',fmt='mediumorchid',ecolor='thistle',elinewidth=3)#,label='W22 S3')
#plt.errorbar(arms_time_S2, arms_Y_S2, yerr=arms_sY_S2, linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='W22 S2')
plt.errorbar(hips_time_S2, hips_Y_S2, yerr=hips_sY_S2, linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3)#,label='W22 S2')
#plt.errorbar(arms_time_S1, arms_Y_S1, yerr=arms_sY_S1, linestyle='-',fmt='darkcyan',ecolor='paleturquoise',elinewidth=3,label='W22 S1')
plt.errorbar(hips_time_S1, hips_Y_S1, yerr=hips_sY_S1, linestyle='-',fmt='darkcyan',ecolor='paleturquoise',elinewidth=3)#,label='W22 S1')
#plt.errorbar(arms_time_W17,arms_Y_W17,yerr=arms_sY_W17,linestyle='-',fmt='firebrick',ecolor='mistyrose',elinewidth=3,label='W17')
plt.errorbar(hips_time_W17,hips_Y_W17,yerr=hips_sY_W17,linestyle='-',fmt='firebrick',ecolor='mistyrose',elinewidth=3)#,label='W17')
#plt.errorbar(arms_time_W10,arms_Y_W10,yerr=arms_sY_W10,linestyle='-',fmt='black',ecolor='silver',elinewidth=3,label='W10')
plt.errorbar(hips_time_W10,hips_Y_W10,yerr=hips_sY_W10,linestyle='-',fmt='black',ecolor='silver',elinewidth=3)#,label='W10')
#plt.legend()
#plt.xlim(0,1)
#plt.ylim(0,60)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/dissertation plots/\
depth_hips.png')#_error.png')

hips_time   = [ hips_W28[:,0], hips_S3[:,0], hips_S2[:,0], hips_S1[:,0], hips_W17[:,0], hips_W10[:,0] ]
hips_X_mean = [ hips_W28[:,1], hips_S3[:,1], hips_S2[:,1], hips_S1[:,1], hips_W17[:,1], hips_W10[:,1] ]
hips_X_stds = [ hips_W28[:,2], hips_S3[:,2], hips_S2[:,2], hips_S1[:,2], hips_W17[:,2], hips_W10[:,2] ]
hips_Y_mean = [ hips_W28[:,3], hips_S3[:,3], hips_S2[:,3], hips_S1[:,3], hips_W17[:,3], hips_W10[:,3] ]
hips_Y_stds = [ hips_W28[:,4], hips_S3[:,4], hips_S2[:,4], hips_S1[:,4], hips_W17[:,4], hips_W10[:,4] ]

hips_time_W28 = hips_time[0][:]
hips_time_S3  = hips_time[1][:]
hips_time_S2  = hips_time[2][:]
hips_time_S1  = hips_time[3][:]
hips_time_W17 = hips_time[4][:]
hips_time_W10 = hips_time[5][:]

hips_Y_W28 = hips_Y_mean[0][:]; hips_sY_W28 = hips_Y_stds[0][:]
hips_Y_S3  = hips_Y_mean[1][:]; hips_sY_S3  = hips_Y_stds[1][:]
hips_Y_S2  = hips_Y_mean[2][:]; hips_sY_S2  = hips_Y_stds[2][:]
hips_Y_S1  = hips_Y_mean[3][:]; hips_sY_S1  = hips_Y_stds[3][:]
hips_Y_W17 = hips_Y_mean[4][:]; hips_sY_W17 = hips_Y_stds[4][:]
hips_Y_W10 = hips_Y_mean[5][:]; hips_sY_W10 = hips_Y_stds[5][:]

low = 50
high = 200

slope_W28, b_W28 = np.polyfit(hips_time_W28[low:high],hips_Y_W28[low:high],1)
slope_S3,  b_S3  = np.polyfit(hips_time_S3[low:high], hips_Y_S3[low:high],1)
slope_S2,  b_S2  = np.polyfit(hips_time_S2[low:high], hips_Y_S2[low:high],1)
slope_S1,  b_S1  = np.polyfit(hips_time_S1[low:high], hips_Y_S1[low:high],1)
slope_W17, b_H17 = np.polyfit(hips_time_W17[low:high],hips_Y_W17[low:high],1)
slope_W10, b_H10 = np.polyfit(hips_time_W10[low:high],hips_Y_W10[low:high],1)

Linear_W28 = get_linearFit(slope_W28,hips_time_W28)
Linear_S3  = get_linearFit(slope_S3, hips_time_S3)
Linear_S2  = get_linearFit(slope_S2, hips_time_S2)
Linear_S1  = get_linearFit(slope_S1, hips_time_S1)
Linear_W17 = get_linearFit(slope_W17,hips_time_W17)
Linear_W10 = get_linearFit(slope_W10,hips_time_W10)

#print('W28 = ',slope_W28,' W22 S3 = ',slope_S3,' W22 S2 = ',slope_S2,' W22 S1 = ',slope_S1,' W17 = ',slope_W17,' W10 = ',slope_W10)

plt.figure()
#plt.title('Trajectory of Arms in Y Direction After Impact')# for 22.7 Degree Models')
plt.xlabel('Time (s)')
plt.ylabel('Depth (m)')
plt.plot(hips_time_W28,Linear_W28,color='limegreen',   label='W28')
plt.plot(hips_time_S3, Linear_S3, color='mediumorchid',label='W22 S3')
plt.plot(hips_time_S2, Linear_S2, color='royalblue',   label='W22 S2')
plt.plot(hips_time_S1, Linear_S1, color='darkcyan',    label='W22 S1')
plt.plot(hips_time_W17,Linear_W17,color='firebrick',   label='W17')
plt.plot(hips_time_W10,Linear_W10,color='black',       label='W10')
plt.legend(loc='lower left')
#plt.xlim(0,0.014)
#plt.ylim(-0.08,0.02)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/dissertation plots/velocity_after_impact.png')#_error.png')



print(';)')
