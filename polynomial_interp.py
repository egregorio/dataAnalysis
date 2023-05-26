import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from get_t_bar import *

# Data for hinge diver models -- hinge / hips
hips_H22 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/9202021_hinge')
# Data for hinged diver models
data_H22 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/09202021_data')
# Import data from 04/04, no hinge, no hole
data_F22 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/04042022_data')
# Import data from 9/20
data_920 = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/09202021_data')

# Import and assign constants
exp_const = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/experiment_constants/constants.txt')
mass_diver = exp_const[0]
fall_bl    = exp_const[1]
spring_bl  = exp_const[2]
impact_v   = exp_const[4]

fall_shape = 2.5 / fall_bl
spring_shape = 2.5 / spring_bl

# Get all the dimensional values and convert meters to body lengths
time_H22 = data_H22[:,0] * fall_shape
std_H22 = data_H22[:,4] / fall_bl
mean_H22 = data_H22[:,3] / fall_bl
mean_H22 = mean_H22 - mean_H22[0]
mean_H22[0] = 0

time_F22 = data_F22[:,0] * spring_shape
std_F22 = data_F22[:,4] / spring_bl
mean_F22 = data_F22[:,3] / spring_bl
mean_F22 = mean_F22 - mean_F22[0]
mean_F22[0] = 0

time_920 = data_920[:,0] * fall_shape
x_920_std = data_920[:,2] / fall_bl
x_920_std = x_920_std - x_920_std[0]
x_920_std[0] = 0
x_920_mean = data_920[:,1] / fall_bl
x_920_mean = x_920_mean - x_920_mean[0]
x_920_mean[0] = 0

angle_920 = np.arcsin(x_920_mean) * (180 / np.pi) * -1
std_920 = np.arcsin(x_920_std)    * (180 / np.pi) * -1
range_920 = np.where(angle_920 == max(angle_920))

# Plot for the STD in Y direction
plt.figure()
#plt.title('Trajectory of Arms in Y Direction After Impact')
#plt.xlabel('Non-Dimensional Time ( Time (s) * Impact Velocity (m/s) / Arm Length (m) )')
#plt.ylabel('Depth (Arm Lengths)')
plt.errorbar(time_H22,mean_H22,yerr=std_H22,linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='W22 S2: 0.0180Nm')
plt.errorbar(time_F22,mean_F22,yerr=std_F22,linestyle='--',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='22.7-Degree, Fixed')
plt.legend(loc='lower left')
#plt.xlim(0,2)
#plt.ylim(-2,0)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/hinged diver simulations/plots/time_series_plot.png')#_error.png')


# Interpolation points
time = [0,0.0741885626,0.1483771252,0.2179289026,0.3384853168,0.4775888717,0.5888717156,0.7094281298,0.8253477589,\
	0.9459041731,1.057187017,1.145285935,1.224111283,1.289026275,1.353941267,1.41885626,1.483771252,1.539412674,\
	1.599690881,1.655332303,1.70633694,1.757341577,1.812982998,1.86862442,1.933539413,1.970633694,2.054095827,\
	2.170015456,2.239567233,2.318392581,2.397217929,2.513137558,2.624420402,2.744976816,2.819165379]

angle = [0,0,0,0.4790419162,1.27744511,3.193612774,5.109780439,7.824351297,11.17764471,15.00998004,19.32135729,\
	 23.47305389,27.14570858,30.65868263,34.49101796,38.32335329,42.4750499,46.62674651,50.45908184,54.29141717,\
	 58.1237525,61.95608782,65.46906188,68.18363273,70.73852295,71.21756487,71.21756487,71.21756487,71.21756487,\
	 71.21756487,71.21756487,71.21756487,71.21756487,71.21756487,71.21756487]

poly = np.polyfit(time,angle,7)
p = np.poly1d(poly)
time_p = np.linspace(0, 3, 100)

print(poly)

# Plot for the STD in Y direction
plt.figure()
#plt.title('Angle of Roll After Impact')
#plt.xlabel('Non-Dimensional Time ( Time (s) * Impact Velocity (m/s) / Arm Length (m) )')
#plt.ylabel('Angle of Bend in Degrees')
plt.plot(time,angle,'o',color='k')
plt.plot(time_p,p(time_p),linestyle='--',color='green',label='Interpolation')
plt.errorbar(time_920,angle_920,yerr=std_920,linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='W22 S2: 0.0180 Nm')
#plt.legend(loc='upper left')
plt.xlim(0,3)
plt.ylim(0,80)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/hinged diver simulations/plots/time_series_angle.png')

hips_time_H22 = 1 + hips_H22[:,0] * fall_shape
hips_mean_H22 = hips_H22[:,3] / fall_bl

low = 50
high = 200

slope_H22, b_H22 = np.polyfit(hips_time_H22[low:high],hips_mean_H22[low:high],1)
Linear_H22 = get_linearFit(slope_H22, hips_time_H22)

plt.figure()
plt.title('Trajectory of Arms in Y Direction After Impact')# for 22.7 Degree Models')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Depth (Arm Lengths)')
plt.plot(hips_time_H22,Linear_H22,color='royalblue',label='0.0180Nm')
plt.legend(loc='lower left')
plt.xlim(0,4)
#plt.ylim(-2,0)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/hinged diver simulations/plots/hinge_trajectory.png')#_error.png')

# Subtracking depth from hinge
Linear_H22 = get_linearFit(slope_H22, time_H22)
mean_H22 = mean_H22 - Linear_H22

# Plot for the STD in Y direction
plt.figure()
plt.title('Trajectory of Arms in Y Direction After Impact')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Amount of Upturn (Arm Lengths)')
plt.errorbar(time_H22,mean_H22,yerr=std_H22,linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='22.7-Degree, Hinge')
plt.errorbar(time_H22,mean_H22,yerr=std_H22,linestyle='-',fmt='royalblue',ecolor='lightsteelblue',elinewidth=3,label='0.0180Nm')
plt.legend(loc='upper left')
#plt.xlim(0,2)
plt.ylim(0,2)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/hinged diver simulations/plots/y_upturn.png')#_error.png')


# Compute the full angle for use in simulations
theta1_H22 = np.arctan( x_920_mean / mean_H22 ) * (180 / np.pi) * -1
theta2_H22 = np.arctan( mean_H22 / x_920_mean ) * (180 / np.pi) * -1

# Interpolation Points
time = [0,0.1346749226,0.1671826625,0.213622291,0.3111455108,0.427244582,0.4829721362,\
	0.5665634675,0.6547987616,0.7523219814,0.8452012384,0.9613003096,1.072755418,\
	1.188854489,1.309597523,1.425696594,1.551083591,1.681114551,1.806501548,\
	1.931888545,2.057275542,2.13622291,2.243034056,2.373065015,2.479876161,\
	2.586687307,2.684210526]
angle = [0.4,0.4,13.2,20.4,30,40.4,46,50.8,55.2,57.6,60,61.2,61.2,60.8,59.6,\
	 57.2,54.4,50.4,46,41.6,36.4,34.4,31.6,32,32.4,32.4,31.6]

poly = np.polyfit(time,angle,5)
p = np.poly1d(poly)
time_p = np.linspace(0, 3, 100)

# Plot for the STD in Y direction
plt.figure()
plt.title('Angle of Arms After Impact')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Angle in Degrees')
plt.plot(time_H22,theta1_H22,linestyle='-',color='royalblue',label='22.7-Degree, Hinge')
plt.plot(time,angle,'o',color='k')
plt.plot(time_p,p(time_p),linestyle='--',color='green',label='Interpolation')
#plt.plot(time_H22,theta2_H22,linestyle='--',color='royalblue',label='22.7-Degree, Hinge')
#plt.legend(loc='upper left')
#plt.xlim(0,2)
#plt.ylim(0,2)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/hinged diver simulations/plots/angle.png')#_error.png')


print(poly)



print(';)')
