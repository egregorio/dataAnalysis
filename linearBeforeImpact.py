import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import scipy
from linearFunctions import *
from get_t_bar import *
from conversions import *

# Import Data from 9/20
sew014 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/014data.csv',delimiter=',',skiprows=0)
sew015 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/015data.csv',delimiter=',',skiprows=0)
sew016 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/016data.csv',delimiter=',',skiprows=0)
sew017 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/017data.csv',delimiter=',',skiprows=0)
sew018 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/018data.csv',delimiter=',',skiprows=0)
sew019 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/019data.csv',delimiter=',',skiprows=0)
sew020 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/020data.csv',delimiter=',',skiprows=0)
sew021 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/021data.csv',delimiter=',',skiprows=0)
sew022 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/022data.csv',delimiter=',',skiprows=0)
sew023 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/023data.csv',delimiter=',',skiprows=0)
sew024 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/024data.csv',delimiter=',',skiprows=0)
sew025 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/025data.csv',delimiter=',',skiprows=0)
sew026 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/026data.csv',delimiter=',',skiprows=0)
sew027 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/027data.csv',delimiter=',',skiprows=0)
sew028 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/028data.csv',delimiter=',',skiprows=0)
sew029 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/029data.csv',delimiter=',',skiprows=0)
sew030 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/9202021/030data.csv',delimiter=',',skiprows=0)
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



# Get Arms Kinematics for 9/20
s_x14, s_y14, s_x14_length, s_y14_length = getArms(sew014)
s_x15, s_y15, s_x15_length, s_y15_length = getArms(sew015)
s_x16, s_y16, s_x16_length, s_y16_length = getArms(sew016)
s_x17, s_y17, s_x17_length, s_y17_length = getArms(sew017)
s_x18, s_y18, s_x18_length, s_y18_length = getArms(sew018)
s_x19, s_y19, s_x19_length, s_y19_length = getArms(sew019)
s_x20, s_y20, s_x20_length, s_y20_length = getArms(sew020)
s_x21, s_y21, s_x21_length, s_y21_length = getArms(sew021)
s_x22, s_y22, s_x22_length, s_y22_length = getArms(sew022)
s_x23, s_y23, s_x23_length, s_y23_length = getArms(sew023)
s_x24, s_y24, s_x24_length, s_y24_length = getArms(sew024)
s_x25, s_y25, s_x25_length, s_y25_length = getArms(sew025)
s_x26, s_y26, s_x26_length, s_y26_length = getArms(sew026)
s_x27, s_y27, s_x27_length, s_y27_length = getArms(sew027)
s_x28, s_y28, s_x28_length, s_y28_length = getArms(sew028)
s_x29, s_y29, s_x29_length, s_y29_length = getArms(sew029)
s_x30, s_y30, s_x30_length, s_y30_length = getArms(sew030)
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
####################### Front View 9/20 ####################################
############################################################################
input_x = [ s_x14, s_x15, s_x16, s_x17, s_x18, s_x19,
            s_x20, s_x21, s_x22, s_x23, s_x24, s_x25,
            s_x26, s_x27, s_x28, s_x29, s_x30 ]

x_lengths = [s_x14_length, s_x25_length,
             s_x15_length, s_x16_length, s_x17_length, s_x18_length, s_x19_length,
             s_x20_length, s_x21_length, s_x22_length, s_x23_length, s_x24_length,
             s_x26_length, s_x27_length, s_x28_length, s_x29_length, s_x30_length]


x_max_length = max(x_lengths)

padded_x = create_one(input_x, x_max_length)

means_x, x_stds = averageF( padded_x, x_max_length)

means_x_920 = means_x - means_x[0]

#print('920  = ',len(means_x))

time_920 = get_time(means_x_920)

############################################################################
####################### Front View 9/21 ####################################
############################################################################
input_x_921 = [ x01, x03, x04, x06,
                x07, x08, x09, x10, x11 ]

x_lengths_921 = [x01_length, x03_length, x04_length, x06_length,
                 x07_length, x08_length, x09_length, x10_length, x11_length]

x_max_length_921 = max(x_lengths_921)

padded_x_921 = create_one(input_x_921, x_max_length_921)

means_x_921, x_stds_921 = averageF( padded_x_921, x_max_length_921)

means_x_921 = means_x_921 - means_x_921[0]

#print('921  = ',len(means_x_921))

time_921 = get_time(means_x_921)

############################################################################
##################### 9/18 #################################################
############################################################################

input_x_918 = [ x15, x17, x18, x20,
                x21, x22, x24, x26, x27,
                x28, x29, x30 ]

x_lengths_918 = [x15_length, x17_length, x18_length,
                 x20_length, x21_length, x22_length, x24_length,
                 x26_length, x27_length, x28_length, x29_length, x30_length]


x_max_length_918 = max(x_lengths_918)

padded_x_918 = create_one(input_x_918, x_max_length_918)

means_x_918, x_stds_918 = averageF( padded_x_918, x_max_length_918)

means_x_918 = means_x_918 - means_x_918[0]

#print('918  = ',len(means_x_918))

time_918 = get_time(means_x_918)

###########################################################################
####################################july###################################
###########################################################################

x_array_july = [j01x, j02x, j03x, j04x, j05x,
           j16x, j17x, j18x, j19x, j20x,
           j11x, j12x, j13x, j14x, j15x,
           j16x, j17x, j18x, j19x, j20x,
           j21x, j22x, j23x, j24x, j25x,
           j26x, j27x, j28x, j29x, j30x]

x_lengths_july = [j01x_length, j02x_length, j03x_length, j04x_length, j05x_length,
             j06x_length, j07x_length, j08x_length, j09x_length, j10x_length,
             j11x_length, j12x_length, j13x_length, j14x_length, j15x_length,
             j16x_length, j17x_length, j18x_length, j19x_length, j20x_length,
             j21x_length, j22x_length, j23x_length, j24x_length, j25x_length,
             j26x_length, j27x_length, j28x_length, j29x_length, j30x_length]

x_max_july = max(x_lengths_july)

x_padded_data_july = create_one(x_array_july, x_max_july)

means_x_july, x_stds_july = averageF(x_padded_data_july, x_max_july)

means_x_july = means_x_july - means_x_july[0]

#print('july = ',len(means_x_july))

time_july = get_time(means_x_july)

###########################################################################
###########################################################################

# Convert frames to dimensional time in seconds
time_729 = frames_to_sec(means_x_july)
time_918 = frames_to_sec(means_x_918)
time_920 = frames_to_sec(means_x_920)
time_921 = frames_to_sec(means_x_921)

# Convert position from pixels to body lengths in pixels
b_729 = pixel_to_bl(means_x_july,135.601280856614)
b_918 = pixel_to_bl(means_x_918, 135.601280856614)
b_920 = pixel_to_bl(means_x_920, 135.601280856614)
b_921 = pixel_to_bl(means_x_921, 135.601280856614)

# Convert body lengths in pixels to body lengths in m
m_729 = pixel_to_m(means_x_july,55.228133)
m_918 = pixel_to_m(means_x_918,55.228133)
m_920 = pixel_to_m(means_x_920,55.228133)
m_921 = pixel_to_m(means_x_921,55.228133)

###########################################################################
###########################################################################

plt.figure()
plt.title('Y Coordinates / Height v. Time')
plt.xlabel('Dimensional Time (s)')
plt.ylabel('Height in Body Lengths')
plt.plot(time_918[-75:-30],b_918[-75:-30],color='springgreen',label='9/18')
plt.plot(time_920[-75:-30],b_920[-75:-30],color='deepskyblue',label='9/20')
plt.plot(time_921[-85:-40],b_921[-85:-40],color='mediumpurple',label='9/21')
plt.plot(time_729[-95:-50],b_729[-95:-50],color='hotpink',label='7/29')
#plt.xlim(-0.015,-0.01)
plt.legend()
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/before_yMean.png')

#plot_x = np.linspace(-0.0248,-0.0198,25)

t_bar_729 = get_t_bar(means_x_july)
t_bar_918 = get_t_bar(means_x_918)
t_bar_920 = get_t_bar(means_x_920)
t_bar_921 = get_t_bar(means_x_921)

slope_729, b_729 = np.polyfit(time_729[-95:-50],m_729[-95:-50],1)
slope_918, b_918 = np.polyfit(time_918[-75:-30],m_918[-75:-30],1)
slope_920, b_920 = np.polyfit(time_920[-75:-30],m_920[-75:-30],1)
slope_921, b_921 = np.polyfit(time_921[-85:-40],m_921[-85:-40],1)

plot_x = np.linspace(0,1,100)

#linearF_729 = m_729 * t_bar_729
#linearF_918 = m_918 * t_bar_918
#linearF_920 = m_920 * t_bar_920
#linearF_921 = m_921 * t_bar_921

linearF_729 = get_linearFit(slope_729,time_729)
linearF_918 = get_linearFit(slope_918,time_918)
linearF_920 = get_linearFit(slope_920,time_920)
linearF_921 = get_linearFit(slope_921,time_921)

#print('stand dev of slope = ',y_stds)
#print('slopes! 7/29 = ',m_729,', 9/18 = ',m_918,', 9/20 = ',m_920,', 9/21 = ',m_921)

mean_m = np.mean([slope_729, slope_918, slope_920, slope_921])
mean_b = np.mean([b_729, b_918, b_920, b_921])
stds_m = np.std([slope_729, slope_918, slope_920, slope_921])
stds_b = np.std([b_729, b_918, b_920, b_921])

print('average slope = ',mean_m,' average intercept = ',mean_b,' without refraction')

#mean_linearF = mean_m * plot_x + mean_b


# convert the slope to below the water length scale!
#mean_m = mean_m * ( 128.517417486157 / 135.601280856614 )
#mean_b = mean_b * ( 128.517417486157 / 135.601280856614 )

print('average slope = ',mean_m,' average intercept = ',mean_b,' with refraction')

saveData = [mean_m, mean_b]

np.savetxt('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/linearFit.txt',saveData)

linearF = get_linearFit(mean_m,t_bar_918)

plt.figure()
plt.title('Linear Interpolation of Impact Velocity')
plt.xlabel('Non Dimensional Time (t*)')
plt.ylabel('Height in Body Lengths')
plt.plot(t_bar_729,linearF_729,color='springgreen',label='7/29')
plt.plot(t_bar_918,linearF_918,color='deepskyblue',label='9/18')
plt.plot(t_bar_920,linearF_920,color='mediumpurple',label='9/20')
plt.plot(t_bar_921,linearF_921,color='hotpink',label='9/21')
plt.plot(t_bar_918,linearF,color='red',label='interpolation')
#plt.ylim(-0.5,0)
#plt.xlim(0,1)
plt.legend()
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/line.png')


impactVelocity = mean_m #* ( 135.601280856614 ) * ( 1 / 55.228133 ) * ( 1 / 39.37 )

print(impactVelocity)

#print(( 135.601280856614 ) * ( 1 / 55.228133 ) * ( 1 / 39.37 ) )

print('youre amazing!!')


