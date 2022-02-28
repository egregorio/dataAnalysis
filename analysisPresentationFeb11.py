import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import scipy
from functions import *

# Import Data from 9/21
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
# Import Data from July
j01 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/001data.csv',delimiter=',',skiprows=0)
j02 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/002data.csv',delimiter=',',skiprows=0)
j03 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/003data.csv',delimiter=',',skiprows=0)
j04 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/004data.csv',delimiter=',',skiprows=0)
j05 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/005data.csv',delimiter=',',skiprows=0)
j06 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/006data.csv',delimiter=',',skiprows=0)
j07 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/007data.csv',delimiter=',',skiprows=0)
j08 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/008data.csv',delimiter=',',skiprows=0)
j09 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/009data.csv',delimiter=',',skiprows=0)
j10 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/010data.csv',delimiter=',',skiprows=0)
j11 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/011data.csv',delimiter=',',skiprows=0)
j12 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/012data.csv',delimiter=',',skiprows=0)
j13 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/013data.csv',delimiter=',',skiprows=0)
j14 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/014data.csv',delimiter=',',skiprows=0)
j15 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/015data.csv',delimiter=',',skiprows=0)
j16 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/016data.csv',delimiter=',',skiprows=0)
j17 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/017data.csv',delimiter=',',skiprows=0)
j18 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/018data.csv',delimiter=',',skiprows=0)
j19 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/019data.csv',delimiter=',',skiprows=0)
j20 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/020data.csv',delimiter=',',skiprows=0)
j21 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/021data.csv',delimiter=',',skiprows=0)
j22 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/022data.csv',delimiter=',',skiprows=0)
j23 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/023data.csv',delimiter=',',skiprows=0)
j24 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/024data.csv',delimiter=',',skiprows=0)
j25 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/025data.csv',delimiter=',',skiprows=0)
j26 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/026data.csv',delimiter=',',skiprows=0)
j27 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/027data.csv',delimiter=',',skiprows=0)
j28 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/028data.csv',delimiter=',',skiprows=0)
j29 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/029data.csv',delimiter=',',skiprows=0)
j30 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/july/030data.csv',delimiter=',',skiprows=0) 

# Get Arms Kinematics for 9/21
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
# Get Arms Kinematics for July
j01x, j01y, j01x_length, j01y_length = getArmsJuly(j01)#,f01x,f01y) 
j02x, j02y, j02x_length, j02y_length = getArmsJuly(j02)#,f01x,f01y) 
j03x, j03y, j03x_length, j03y_length = getArmsJuly(j03)#,f01x,f01y) 
j04x, j04y, j04x_length, j04y_length = getArmsJuly(j04)#,f01x,f01y) 
j05x, j05y, j05x_length, j05y_length = getArmsJuly(j05)#,f01x,f01y) 
j06x, j06y, j06x_length, j06y_length = getArmsJuly(j06)#,f01x,f01y) 
j07x, j07y, j07x_length, j07y_length = getArmsJuly(j07)#,f01x,f01y) 
j08x, j08y, j08x_length, j08y_length = getArmsJuly(j08)#,f01x,f01y) 
j09x, j09y, j09x_length, j09y_length = getArmsJuly(j09)#,f01x,f01y) 
j10x, j10y, j10x_length, j10y_length = getArmsJuly(j10)#,f01x,f01y) 
j11x, j11y, j11x_length, j11y_length = getArmsJuly(j11)#,f01x,f01y) 
j12x, j12y, j12x_length, j12y_length = getArmsJuly(j12)#,f01x,f01y) 
j13x, j13y, j13x_length, j13y_length = getArmsJuly(j13)#,f01x,f01y) 
j14x, j14y, j14x_length, j14y_length = getArmsJuly(j14)#,f01x,f01y) 
j15x, j15y, j15x_length, j15y_length = getArmsJuly(j15)#,f01x,f01y) 
j16x, j16y, j16x_length, j16y_length = getArmsJuly(j16)#,f01x,f01y) 
j17x, j17y, j17x_length, j17y_length = getArmsJuly(j17)#,f01x,f01y) 
j18x, j18y, j18x_length, j18y_length = getArmsJuly(j18)#,f01x,f01y) 
j19x, j19y, j19x_length, j19y_length = getArmsJuly(j19)#,f01x,f01y) 
j20x, j20y, j20x_length, j20y_length = getArmsJuly(j20)#,f01x,f01y) 
j21x, j21y, j21x_length, j21y_length = getArmsJuly(j21)#,f01x,f01y) 
j22x, j22y, j22x_length, j22y_length = getArmsJuly(j22)#,f01x,f01y) 
j23x, j23y, j23x_length, j23y_length = getArmsJuly(j23)#,f01x,f01y) 
j24x, j24y, j24x_length, j24y_length = getArmsJuly(j24)#,f01x,f01y) 
j25x, j25y, j25x_length, j25y_length = getArmsJuly(j25)#,f01x,f01y) 
j26x, j26y, j26x_length, j26y_length = getArmsJuly(j26)#,f01x,f01y) 
j27x, j27y, j27x_length, j27y_length = getArmsJuly(j27)#,f01x,f01y) 
j28x, j28y, j28x_length, j28y_length = getArmsJuly(j28)#,f01x,f01y) 
j29x, j29y, j29x_length, j29y_length = getArmsJuly(j29)#,f01x,f01y) 
j30x, j30y, j30x_length, j30y_length = getArmsJuly(j30)#,f01x,f01y) 


############################################################################
####################### Front View 9/21 ####################################
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
####################################july###################################
###########################################################################

x_array_july = [j01x, j02x, j03x, j04x, j05x,
           j16x, j17x, j18x, j19x, j20x,
           j11x, j12x, j13x, j14x, j15x,
           j16x, j17x, j18x, j19x, j20x,
           j21x, j22x, j23x, j24x, j25x,
           j26x, j27x, j28x, j29x, j30x]
y_array_july = [j01y, j02y, j03y, j04y, j05y,
           j06y, j07y, j08y, j09y, j10y,
           j11y, j12y, j13y, j14y, j15y,
           j16y, j17y, j18y, j19y, j20y,
           j21y, j22y, j23y, j24y, j25y,
           j26y, j27y, j28y, j29y, j30y]

x_lengths_july = [j01x_length, j02x_length, j03x_length, j04x_length, j05x_length,
             j06x_length, j07x_length, j08x_length, j09x_length, j10x_length,
             j11x_length, j12x_length, j13x_length, j14x_length, j15x_length,
             j16x_length, j17x_length, j18x_length, j19x_length, j20x_length,
             j21x_length, j22x_length, j23x_length, j24x_length, j25x_length,
             j26x_length, j27x_length, j28x_length, j29x_length, j30x_length]
y_lengths_july = [j01y_length, j02y_length, j03y_length, j04y_length, j05y_length,
             j06y_length, j07y_length, j08y_length, j09y_length, j10y_length,
             j11y_length, j12y_length, j13y_length, j14y_length, j15y_length,
             j16y_length, j17y_length, j18y_length, j19y_length, j20y_length,
             j21y_length, j22y_length, j23y_length, j24y_length, j25y_length,
             j26y_length, j27y_length, j28y_length, j29y_length, j30y_length]

x_max_july = max(x_lengths_july)
y_max_july = max(y_lengths_july)

x_padded_data_july = create_one(x_array_july, x_max_july)
y_padded_data_july = create_one(y_array_july, y_max_july)

means_x_july, x_stds_july = averageF(x_padded_data_july, x_max_july)
means_y_july, y_stds_july = averageF(y_padded_data_july, y_max_july)

###########################################################################
###########################################################################

plot_x = np.linspace(0,1,350)#x_max_length)


# Best Fit Line for Y Direction
interpp = np.linspace(0,1,100)

linearFit = -1.3848*interpp + 0.0031

# Plot for the STD in Y direction
plt.figure()
plt.title('Y Coordinates / Height v. Time')
plt.xlabel('Non-Dimensional Time')
plt.ylabel('Height in Body Lengths')
#plt.errorbar(plot_x,means_x_918[0:350],yerr=x_stds_918[0:350],fmt='k',ecolor='springgreen',label='0.0136 Nm')
#plt.errorbar(plot_x,means_x_920[0:350],yerr=x_stds_920[0:350],fmt='k',ecolor='deepskyblue',label='0.0153 Nm')
#plt.errorbar(plot_x,means_x_july[0:350],yerr=x_stds_july[0:350],fmt='k',ecolor='hotpink',label='0.0294 Nm')
plt.plot(interpp,linearFit,color='r')
plt.axhline(y=-0.415,color='r')
plt.axhline(y=-0.605,color='r')
plt.axhline(y=-0.71,color='r')
plt.plot(0.30260869565217385,-0.4152808988764044,'o',color='springgreen',label='0.0136 Nm, t=0.3026')
plt.plot(0.43999999999999984,-0.6040449438202247,'o',color='deepskyblue',label='0.0153 Nm, t=0.4399')
plt.plot(0.5147826086956521, -0.7092134831460674,'o',color='hotpink', label='0.0294 Nm, t=0.5147')
plt.legend(numpoints=1)
plt.xlim(0,1)
plt.ylim(-1.2,0)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_fall_2021/ana_yStd.png')

# Plot for the STD in X direction
plt.figure()
plt.title('X Coordinates v. Time')
plt.xlabel('Non-Dimensional Time')
plt.ylabel('Horizonal Position in Body Lengths')
plt.errorbar(plot_x,means_y_918[0:350],yerr=y_stds_918[0:350],fmt='k',ecolor='springgreen',label='0.0136 Nm')
plt.errorbar(plot_x,means_y_920[0:350],yerr=y_stds_920[0:350],fmt='k',ecolor='deepskyblue',label='0.0153 Nm')
plt.errorbar(plot_x,means_y_july[0:350],yerr=y_stds_july[0:350],fmt='k',ecolor='hotpink',label='0.0294 Nm')
plt.legend()
plt.xlim(0,1)
plt.ylim(-0.55,0.05)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_fall_2021/ana_xStd.png')

print('youre amazing!!')
