import numpy as np
import matplotlib.pyplot as plt
import scipy
from functions import *

# Import Data from 9/20
raw001 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/frontview/001data.csv',delimiter=',',skiprows=0)
raw003 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/frontview/003data.csv',delimiter=',',skiprows=0)
raw004 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/frontview/004data.csv',delimiter=',',skiprows=0)
raw006 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/frontview/006data.csv',delimiter=',',skiprows=0)
raw007 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/frontview/007data.csv',delimiter=',',skiprows=0)
raw008 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/frontview/008data.csv',delimiter=',',skiprows=0)
raw009 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/frontview/009data.csv',delimiter=',',skiprows=0)
raw010 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/frontview/010data.csv',delimiter=',',skiprows=0)
raw011 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/frontview/011data.csv',delimiter=',',skiprows=0)
# Import Data from 9/18
raw015 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/015data.csv',delimiter=',',skiprows=0)
raw017 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/017data.csv',delimiter=',',skiprows=0)
raw018 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/018data.csv',delimiter=',',skiprows=0)
raw020 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/020data.csv',delimiter=',',skiprows=0)
raw021 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/021data.csv',delimiter=',',skiprows=0)
raw022 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/022data.csv',delimiter=',',skiprows=0)
raw024 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/024data.csv',delimiter=',',skiprows=0)
raw026 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/026data.csv',delimiter=',',skiprows=0)
raw027 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/027data.csv',delimiter=',',skiprows=0)
raw028 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/028data.csv',delimiter=',',skiprows=0)
raw029 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/029data.csv',delimiter=',',skiprows=0)
raw030 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9182021/030data.csv',delimiter=',',skiprows=0)


# Get Arms Kinematics for 9/20
x01, y01, x01_length, y01_length = getArms920(raw001)
x03, y03, x03_length, y03_length = getArms920(raw003)
x04, y04, x04_length, y04_length = getArms920(raw004)
x06, y06, x06_length, y06_length = getArms920(raw006)
x07, y07, x07_length, y07_length = getArms920(raw007)
x08, y08, x08_length, y08_length = getArms920(raw008)
x09, y09, x09_length, y09_length = getArms920(raw009)
x10, y10, x10_length, y10_length = getArms920(raw010)
x11, y11, x11_length, y11_length = getArms920(raw011)
# Get Arms Kinematics for 9/18
x15, y15, x15_length, y15_length = getArms918(raw015)
x17, y17, x17_length, y17_length = getArms918(raw017)
x18, y18, x18_length, y18_length = getArms918(raw018)
x20, y20, x20_length, y20_length = getArms918(raw020)
x21, y21, x21_length, y21_length = getArms918(raw021)
x22, y22, x22_length, y22_length = getArms918(raw022)
x24, y24, x24_length, y24_length = getArms918(raw024)
x26, y26, x26_length, y26_length = getArms918(raw026)
x27, y27, x27_length, y27_length = getArms918(raw027)
x28, y28, x28_length, y28_length = getArms918(raw028)
x29, y29, x29_length, y29_length = getArms918(raw029)
x30, y30, x30_length, y30_length = getArms918(raw030)

############################################################################
####################### Front View 9/20 ####################################
############################################################################
input_x_920 = [ x01, x03, x04, x06, 
                x07, x08, x09, x10, x11 ]

input_y_920 = [ y01, y03, y04, y06, 
                y07, y08, y09, y10, y11 ]

x_lengths_920 = [x01_length, x03_length, x04_length, x06_length,
                 x07_length, x08_length, x09_length, x10_length, x11_length]

y_lengths_920 = [y01_length, y03_length, y04_length, y06_length,
                 y07_length, y08_length, y09_length, y10_length, y11_length]

x_max_length_920 = max(x_lengths_920)
y_max_length_920 = max(y_lengths_920)

padded_x_920 = create_one(input_x_920, x_max_length_920)
padded_y_920 = create_one(input_y_920, y_max_length_920)

means_x_920, x_stds_920 = averageF( padded_x_920, x_max_length_920)
means_y_920, y_stds_920 = averageF( padded_y_920, y_max_length_920)

############################################################################
##################### 9/18 #################################################
############################################################################

input_x_918 = [ x15, x17, x18, x20,
                x21, x22, x24, x26, x27,
                x28, x29, x30 ]

input_y_918 = [ y15, y17, y18, y20,
                y21, y22, y24, y26, y27,
                y28, y29, y30 ]

x_lengths_918 = [x15_length, x17_length, x18_length,
                 x20_length, x21_length, x22_length, x24_length,
                 x26_length, x27_length, x28_length, x29_length, x30_length]

y_lengths_918 = [y15_length, y17_length, y18_length,
                 y20_length, y21_length, y22_length, y24_length,
                 y26_length, y27_length, y28_length, y29_length, y30_length]

x_max_length_918 = max(x_lengths_918)
y_max_length_918 = max(y_lengths_918)

padded_x_918 = create_one(input_x_918, x_max_length_918)
padded_y_918 = create_one(input_y_918, y_max_length_918)

means_x_918, x_stds_918 = averageF( padded_x_918, x_max_length_918)
means_y_918, y_stds_918 = averageF( padded_y_918, y_max_length_918)

###########################################################################
###########################################################################

plot_x = np.linspace(0,1,350)#x_max_length)

# Plot for the Means in Y direction
plt.figure()
plt.title('Y Coordinates / Height v. Time')
plt.xlabel('Non-Dimensional Time')
plt.ylabel('Height in Body Lengths')
plt.plot(plot_x,means_x_920[0:350],color='c',label='9/20')
plt.plot(plot_x,means_x_918[0:350],color='m',label='9/18')
plt.legend()
plt.xlim(0,1)
plt.ylim(1.6,2.6)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_fall_2021/yMean.png')

# Plot for the Means in X direction
plt.figure()
plt.title('X Coordinates v. Time')
plt.xlabel('Non-Dimensional Time')
plt.ylabel('Horizonal Position in Body Lengths')
plt.plot(plot_x,means_y_920[0:350],color='c',label='9/20')
plt.plot(plot_x,means_y_918[0:350],color='m',label='9/18')
plt.legend()
plt.xlim(0,1)
plt.ylim(0.2,0.8)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_fall_2021/xMean.png')

# Plot for the STD in Y direction
plt.figure()
plt.title('Y Coordinates / Height v. Time')
plt.xlabel('Non-Dimensional Time')
plt.ylabel('Height in Body Lengths')
plt.errorbar(plot_x,means_x_920[0:350],yerr=x_stds_920[0:350],fmt='k',ecolor='c',label='9/20')
plt.errorbar(plot_x,means_x_918[0:350],yerr=x_stds_918[0:350],fmt='k',ecolor='m',label='9/18')
plt.legend()
plt.xlim(0,1)
plt.ylim(1.6,2.6)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_fall_2021/yStd.png')

# Plot for the STD in X direction
plt.figure()
plt.title('X Coordinates v. Time')
plt.xlabel('Non-Dimensional Time')
plt.ylabel('Horizonal Position in Body Lengths')
plt.errorbar(plot_x,means_y_920[0:350],yerr=y_stds_920[0:350],fmt='k',ecolor='c',label='9/20')
plt.errorbar(plot_x,means_y_918[0:350],yerr=y_stds_918[0:350],fmt='k',ecolor='m',label='9/18')
plt.legend()
plt.xlim(0,1)
plt.ylim(0.2,0.8)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_fall_2021/xStd.png')

print('youre amazing!!')
