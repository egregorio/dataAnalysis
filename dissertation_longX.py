import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from get_t_bar import *

data_S3 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/09182021_data')
data_S2 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/09202021_data')
data_S1 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/09212021_data')
data_W28 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/10212021_data')
data_W10 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/10262021_data')
data_F22 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/04042022_data')
data_F10 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/04052022_a1_data')
data_F28 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/04052022_a3_data')
data_W17 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/08172022_data')

before_S3 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/09182021_before')
before_S2 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/09202021_before')
before_S1 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/09212021_before')
before_W28 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/10212021_before')
before_W10 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/10262021_before')
#before_F22 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/04042022_before')
#before_F10 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/04052022_a1_before')
#before_F28 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/04052022_a3_before')
before_W17 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/08172022_before')

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


arms_time   = [ data_W28[:,0], data_S3[:,0], data_S2[:,0], data_S1[:,0], data_W17[:,0], data_W10[:,0] ]
arms_X_mean = [ data_W28[:,1], data_S3[:,1], data_S2[:,1], data_S1[:,1], data_W17[:,1], data_W10[:,1] ]
arms_X_stds = [ data_W28[:,2], data_S3[:,2], data_S2[:,2], data_S1[:,2], data_W17[:,2], data_W10[:,2] ]
arms_Y_mean = [ data_W28[:,3], data_S3[:,3], data_S2[:,3], data_S1[:,3], data_W17[:,3], data_W10[:,3] ]
arms_Y_stds = [ data_W28[:,4], data_S3[:,4], data_S2[:,4], data_S1[:,4], data_W17[:,4], data_W10[:,4] ]


before_time   = [ before_W28[:,0], before_S3[:,0], before_S2[:,0], before_S1[:,0], before_W17[:,0], before_W10[:,0] ]
before_X_mean = [ before_W28[:,1], before_S3[:,1], before_S2[:,1], before_S1[:,1], before_W17[:,1], before_W10[:,1] ]
before_X_stds = [ before_W28[:,2], before_S3[:,2], before_S2[:,2], before_S1[:,2], before_W17[:,2], before_W10[:,2] ]
before_Y_mean = [ before_W28[:,3], before_S3[:,3], before_S2[:,3], before_S1[:,3], before_W17[:,3], before_W10[:,3] ]
before_Y_stds = [ before_W28[:,4], before_S3[:,4], before_S2[:,4], before_S1[:,4], before_W17[:,4], before_W10[:,4] ]


# Get all the dimensional values and convert meters to body lengths
for i in range(0,6):
        arms_time[i][:] = arms_time[i][:] # * fall_shape

        arms_X_stds[i][:] = arms_X_stds[i][:] - arms_X_stds[i][0]
        arms_X_stds[i][0] = 0

        arms_X_mean[i][:] = arms_X_mean[i][:] - arms_X_mean[i][0]
        arms_X_mean[i][0] = 0

        arms_Y_stds[i][:] = arms_Y_stds[i][:]# / fall_bl

        arms_Y_mean[i][:] = arms_Y_mean[i][:]# / fall_bl
        arms_Y_mean[i][:] = arms_Y_mean[i][:] - arms_Y_mean[i][0]
        arms_Y_mean[i][0] = 0

        before_time[i][:] = before_time[i][:] - before_time[i][-1] # * fall_shape

        before_X_stds[i][:] = before_X_stds[i][:] - before_X_stds[i][0]
        before_X_stds[i][0] = 0

        before_X_mean[i][:] = before_X_mean[i][:] - before_X_mean[i][0]
        before_X_mean[i][0] = 0

        before_Y_stds[i][:] = before_Y_stds[i][:]# / fall_bl

        before_Y_mean[i][:] = before_Y_mean[i][:]# / fall_bl
        before_Y_mean[i][:] = before_Y_mean[i][:] - before_Y_mean[i][-1]
        before_Y_mean[i][-1] = 0




#for i in range(0,6):
#        switch = np.argmin(arms_X_mean[i][:-60])
#        arms_X_mean[i][:] = 90 * ( arms_X_mean[i][:] / arms_X_mean[i][switch] )
#        before_X_mean[i][:] = 90 * ( before_X_mean[i][:] / before_X_mean[i][switch] )

arms_time_W28 = arms_time[0][:]
arms_time_S3  = arms_time[1][:]
arms_time_S2  = arms_time[2][:]
arms_time_S1  = arms_time[3][:]
arms_time_W17 = arms_time[4][:]
arms_time_W10 = arms_time[5][:]

arms_X_W28 = arms_X_mean[0][:]; arms_sX_W28 = arms_X_stds[0][:]
arms_X_S3  = arms_X_mean[1][:]; arms_sX_S3  = arms_X_stds[1][:]
arms_X_S2  = arms_X_mean[2][:]; arms_sX_S2  = arms_X_stds[2][:]
arms_X_S1  = arms_X_mean[3][:]; arms_sX_S1  = arms_X_stds[3][:]
arms_X_W17 = arms_X_mean[4][:]; arms_sX_W17 = arms_X_stds[4][:]
arms_X_W10 = arms_X_mean[5][:]; arms_sX_W10 = arms_X_stds[5][:]

arms_Y_W28 = arms_Y_mean[0][:]; arms_sY_W28 = arms_Y_stds[0][:]
arms_Y_S3  = arms_Y_mean[1][:]; arms_sY_S3  = arms_Y_stds[1][:]
arms_Y_S2  = arms_Y_mean[2][:]; arms_sY_S2  = arms_Y_stds[2][:]
arms_Y_S1  = arms_Y_mean[3][:]; arms_sY_S1  = arms_Y_stds[3][:]
arms_Y_W17 = arms_Y_mean[4][:]; arms_sY_W17 = arms_Y_stds[4][:]
arms_Y_W10 = arms_Y_mean[5][:]; arms_sY_W10 = arms_Y_stds[5][:]

before_time_W28 = before_time[0][:]
before_time_S3  = before_time[1][:]
before_time_S2  = before_time[2][:]
before_time_S1  = before_time[3][:]
before_time_W17 = before_time[4][:]
before_time_W10 = before_time[5][:]

before_X_W28 = before_X_mean[0][:]; before_sX_W28 = before_X_stds[0][:]
before_X_S3  = before_X_mean[1][:]; before_sX_S3  = before_X_stds[1][:]
before_X_S2  = before_X_mean[2][:]; before_sX_S2  = before_X_stds[2][:]
before_X_S1  = before_X_mean[3][:]; before_sX_S1  = before_X_stds[3][:]
before_X_W17 = before_X_mean[4][:]; before_sX_W17 = before_X_stds[4][:]
before_X_W10 = before_X_mean[5][:]; before_sX_W10 = before_X_stds[5][:]

before_Y_W28 = before_Y_mean[0][:]; before_sY_W28 = before_Y_stds[0][:]
before_Y_S3  = before_Y_mean[1][:]; before_sY_S3  = before_Y_stds[1][:]
before_Y_S2  = before_Y_mean[2][:]; before_sY_S2  = before_Y_stds[2][:]
before_Y_S1  = before_Y_mean[3][:]; before_sY_S1  = before_Y_stds[3][:]
before_Y_W17 = before_Y_mean[4][:]; before_sY_W17 = before_Y_stds[4][:]
before_Y_W10 = before_Y_mean[5][:]; before_sY_W10 = before_Y_stds[5][:]


plt.figure()
plt.axvline(x = 0, linestyle='--',color='mediumblue')# Angle W10
plt.axvline(x = -0.0017262830482115132, linestyle='--',color='indianred')# Angle W10
#plt.errorbar(before_time_W28,before_Y_W28,yerr=before_sY_W28,linestyle='-',fmt='limegreen',ecolor='lightgreen',elinewidth=3)#,label='W28')
#plt.errorbar(before_time_S3, before_Y_S3, yerr=before_sY_S3, linestyle='-',fmt='mediumorchid',ecolor='thistle')#,elinewidth=3,label='W22 S3')
#plt.errorbar(before_time_S2, before_Y_S2, yerr=before_sY_S2, linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3)#,label='W22 S2')
#plt.errorbar(before_time_S1, before_Y_S1, yerr=before_sY_S1, linestyle='-',fmt='darkcyan',ecolor='paleturquoise',elinewidth=3)#,label='W22 S1')
#plt.errorbar(before_time_W17,before_Y_W17,yerr=before_sY_W17,linestyle='-',fmt='firebrick',ecolor='mistyrose',elinewidth=3)#,label='W17')
plt.errorbar(before_time_W10,before_Y_W10,yerr=before_sY_W10,linestyle='-',fmt='black',ecolor='silver',elinewidth=3)#,label='W10')
#plt.errorbar(arms_time_W28,arms_Y_W28,yerr=arms_sY_W28,linestyle='-',fmt='limegreen',ecolor='lightgreen',elinewidth=3,label='W28')
#plt.errorbar(arms_time_S3[:-50], arms_Y_S3[:-50], yerr=arms_sY_S3[:-50], linestyle='-',fmt='mediumorchid',ecolor='thistle',elinewidth=3,label='W22 S3')
#plt.errorbar(arms_time_S2, arms_Y_S2, yerr=arms_sY_S2, linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='W22 S2')
#plt.errorbar(arms_time_S1, arms_Y_S1, yerr=arms_sY_S1, linestyle='-',fmt='darkcyan',ecolor='paleturquoise',elinewidth=3,label='W22 S1')
#plt.errorbar(arms_time_W17,arms_Y_W17,yerr=arms_sY_W17,linestyle='-',fmt='firebrick',ecolor='mistyrose',elinewidth=3,label='W17')
plt.errorbar(arms_time_W10,arms_Y_W10,yerr=arms_sY_W10,linestyle='-',fmt='black',ecolor='silver',elinewidth=3,label='W10')
plt.legend()
plt.xlim(-0.03,0.15)
plt.ylim(-0.3,0.2)
#fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/dissertation plots/\
long_W10.png')#_error.png')

print(';)')
