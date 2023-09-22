import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Import and assign constants
exp_const = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/experiment_constants/constants.txt')
mass_diver = exp_const[0]
fall_bl    = exp_const[1]
spring_bl  = exp_const[2]
impact_v   = exp_const[4]

fall_shape = 2.5 / fall_bl
spring_shape = 2.5 / spring_bl

# Import data from 04/04, no hinge, no hole
all_stat = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/air_cavity_statistics.txt',skiprows=2)
#,delimiter=' '
x_axis = [0.1,0.25,0.5,0.75,1,1.25,1.5,1.75,2,2.25,2.5,2.75,3,3.25,3.5,3.75]
#fall_xaxis = [ 0.0022, 0.0058, 0.0118, 0.0178, 0.0238, 0.0298, 0.0358, 0.0418, 0.0478, 0.0538, 0.0598, 0.0658, 0.0718, 0.0778, 0.0838, 0.0898]#, 0.0958 ]
#spring_xaxis = [0.0022, 0.0056, 0.0114, 0.0174, 0.0232, 0.029, 0.0348, 0.0406, 0.0464, 0.0524, 0.0582, 0.064, 0.0698, 0.0756, 0.0814, 0.0874]#, 0.0932 ]

a_10_hm = all_stat[:,0] # 10/26
a_10_hs = all_stat[:,1] # 10/26
a_10_fm = all_stat[:,2] # 04/05_a1
a_10_fs = all_stat[:,3] # 04/05_a1
t_007_m = all_stat[:,4] # 09/18
t_007_s = all_stat[:,5] # 09/18
t_018_m = all_stat[:,6] # 09/20
t_018_s = all_stat[:,7] # 09/20
t_015_m = all_stat[:,8] # 09/21
t_015_s = all_stat[:,9] # 09/21
a_22_fm = all_stat[:,10] # 04/04_a2
a_22_fs = all_stat[:,11] # 04/04_a2
a_28_hm = all_stat[:,12] # 10/21
a_28_hs = all_stat[:,13] # 10/21
a_28_fm = all_stat[:,14] # 04/05_a3
a_28_fs = all_stat[:,15] # 04/05_a3


# Plot for the STD in Y direction
plt.figure()
plt.title('Development of Air Cavity After Impact for 28.6-Degree Wedge')
plt.xlabel('Non-Dimensional Time ( Time (s) * Impact Velocity (m/s) / Arm Length (m) )')
plt.ylabel('Estimated Size of Body and Air Cavity')
plt.errorbar(x_axis,a_28_hm,yerr=a_28_hs,marker='o',linestyle='-',markeredgecolor='black',fmt='black',ecolor='black',label='Hinge')
plt.errorbar(x_axis,a_28_fm,yerr=a_28_fs,marker='s',linestyle='--',markeredgecolor='black',fmt='black',ecolor='black',label='Fixed')
plt.ylim(0,5)
plt.xlim(0,4)
plt.legend(loc='upper left')
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/3minute.png')

# Plot for the STD in Y direction
plt.figure()
#plt.title('Development of Air Cavity After Impact')
#plt.xlabel('Non-Dimensional Time ( Time (s) * Impact Velocity (m/s) / Arm Length (m) )')
#plt.ylabel('Estimated Size of Body and Air Cavity')
#plt.errorbar(x_axis,a_28_hm,yerr=a_28_hs,marker='o',linestyle='-',markeredgecolor='limegreen',fmt='limegreen',ecolor='limegreen',label='W28, Hinge')
plt.errorbar(x_axis,t_007_m,yerr=t_007_s,marker='o',linestyle='-',markeredgecolor='mediumorchid',fmt='mediumorchid',ecolor='mediumorchid',label='W22 S3, Hinge')
plt.errorbar(x_axis,t_018_m,yerr=t_018_s,marker='o',linestyle='-',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='W22 S2, Hinge')
plt.errorbar(x_axis,t_015_m,yerr=t_015_s,marker='o',linestyle='-',markeredgecolor='turquoise',fmt='turquoise',ecolor='turquoise',label='W22 S1, Hinge')
#plt.errorbar(x_axis,t_018_m,yerr=t_018_s,marker='o',linestyle='-',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='22.7-Degree, Hinge')
#plt.errorbar(x_axis,a_10_hm,yerr=a_10_hs,marker='o',linestyle='-',markeredgecolor='black',fmt='black',ecolor='black',label='W10, Hinge')
#plt.errorbar(x_axis,a_28_fm,yerr=a_28_fs,marker='s',linestyle='--',markeredgecolor='limegreen',fmt='limegreen',ecolor='limegreen',label='W28, Fixed')
plt.errorbar(x_axis,a_22_fm,yerr=a_22_fs,marker='s',linestyle='--',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='W22, Fixed')
#plt.errorbar(x_axis,a_10_fm,yerr=a_10_fs,marker='s',linestyle='--',markeredgecolor='black',fmt='black',ecolor='black',label='W10, Fixed')
plt.ylim(0,6)
plt.xlim(0,4)
plt.legend(loc='upper left')
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/dissertation plots/\
normalized_dissertation.png')

# Plot for the STD in Y direction
plt.figure()
#plt.title('Development of Air Cavity After Impact')
#plt.xlabel('Non-Dimensional Time ( Time (s) * Impact Velocity (m/s) / Arm Length (m) )')
#plt.ylabel('Estimated Size of Body and Air Cavity')
plt.errorbar(x_axis,a_28_hm,yerr=a_28_hs,marker='o',linestyle='-',markeredgecolor='limegreen',fmt='limegreen',ecolor='limegreen',label='W28, Hinge')
plt.errorbar(x_axis,t_007_m,yerr=t_007_s,marker='o',linestyle='-',markeredgecolor='mediumorchid',fmt='mediumorchid',ecolor='mediumorchid',label='W22 S3, Hinge')
plt.errorbar(x_axis,t_018_m,yerr=t_018_s,marker='o',linestyle='-',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='W22 S2, Hinge')
plt.errorbar(x_axis,t_015_m,yerr=t_015_s,marker='o',linestyle='-',markeredgecolor='turquoise',fmt='turquoise',ecolor='turquoise',label='W22 S1, Hinge')
#plt.errorbar(x_axis,t_018_m,yerr=t_018_s,marker='o',linestyle='-',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='22.7-Degree, Hinge')
plt.errorbar(x_axis,a_10_hm,yerr=a_10_hs,marker='o',linestyle='-',markeredgecolor='black',fmt='black',ecolor='black',label='W10, Hinge')
plt.errorbar(x_axis,a_28_fm,yerr=a_28_fs,marker='s',linestyle='--',markeredgecolor='limegreen',fmt='limegreen',ecolor='limegreen',label='W28, Fixed')
plt.errorbar(x_axis,a_22_fm,yerr=a_22_fs,marker='s',linestyle='--',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='W22, Fixed')
plt.errorbar(x_axis,a_10_fm,yerr=a_10_fs,marker='s',linestyle='--',markeredgecolor='black',fmt='black',ecolor='black',label='W10, Fixed')
plt.ylim(0,6)
plt.xlim(0,4)
plt.legend(loc='upper left')
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/normalized.png')

# Plot for the STD in Y direction
plt.figure()
#plt.title('Development of Air Cavity After Impact')
#plt.xlabel('Non-Dimensional Time ( Time (s) * Impact Velocity (m/s) / Arm Length (m) )')
#plt.ylabel('Estimated Size of Body and Air Cavity')
plt.errorbar(x_axis,a_28_hm,yerr=a_28_hs,marker='o',linestyle='-',markeredgecolor='limegreen',fmt='limegreen',ecolor='limegreen',label='W28, Hinge')
plt.errorbar(x_axis,t_007_m,yerr=t_007_s,marker='o',linestyle='-',markeredgecolor='mediumorchid',fmt='mediumorchid',ecolor='mediumorchid',label='W22 S3, Hinge')
plt.errorbar(x_axis,t_018_m,yerr=t_018_s,marker='o',linestyle='-',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='W22 S2, Hinge')
plt.errorbar(x_axis,t_015_m,yerr=t_015_s,marker='o',linestyle='-',markeredgecolor='turquoise',fmt='turquoise',ecolor='turquoise',label='W22 S1, Hinge')
#plt.errorbar(x_axis,t_018_m,yerr=t_018_s,marker='o',linestyle='-',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='22.7-Degree, Hinge')
#plt.errorbar(x_axis,a_10_hm,yerr=a_10_hs,marker='o',linestyle='-',markeredgecolor='black',fmt='black',ecolor='black',label='W10, Hinge')
#plt.errorbar(x_axis,a_28_fm,yerr=a_28_fs,marker='s',linestyle='--',markeredgecolor='limegreen',fmt='limegreen',ecolor='limegreen',label='W28, Fixed')
#plt.errorbar(x_axis,a_22_fm,yerr=a_22_fs,marker='s',linestyle='--',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='W22, Fixed')
#plt.errorbar(x_axis,a_10_fm,yerr=a_10_fs,marker='s',linestyle='--',markeredgecolor='black',fmt='black',ecolor='black',label='W10, Fixed')
plt.axhline(y=3.15, color='r', linestyle='-')
plt.ylim(0,6)
plt.xlim(0,4)
plt.legend(loc='upper left')
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/redline.png')

plt.figure()
plt.title('Development of Air Cavity After Impact')
plt.xlabel('Non-Dimensional Time ( Time (s) * Impact Velocity (m/s) / Arm Length (m) )')
plt.ylabel('Estimated Size of Body and Air Cavity')
plt.errorbar(x_axis,t_007_m,yerr=t_007_s,marker='o',linestyle='-',markeredgecolor='mediumorchid',fmt='mediumorchid',ecolor='mediumorchid',label='0.00768Nm')
plt.errorbar(x_axis,t_018_m,yerr=t_018_s,marker='o',linestyle='-',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='0.0180Nm')
plt.errorbar(x_axis,t_015_m,yerr=t_015_s,marker='o',linestyle='-',markeredgecolor='turquoise',fmt='turquoise',ecolor='turquoise',label='0.0153Nm')
plt.errorbar(x_axis,a_22_fm,yerr=a_22_fs,marker='s',linestyle='--',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='Fixed')
plt.ylim(0,6)
plt.xlim(0,4)
plt.legend(loc='upper left')
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/stiffness.png')


plt.figure()
plt.title('Development of Air Cavity After Impact')
plt.xlabel('Non-Dimensional Time ( Time (s) * Impact Velocity (m/s) / Arm Length (m) )')
plt.ylabel('Estimated Size of Body and Air Cavity')
plt.errorbar(x_axis,a_10_fm,yerr=a_10_fs,marker='s',linestyle='--',markeredgecolor='black',fmt='black',ecolor='black',label='10.4-Degree, Fixed')
plt.errorbar(x_axis,a_22_fm,yerr=a_22_fs,marker='s',linestyle='--',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='22.7-Degree, Fixed')
plt.errorbar(x_axis,a_28_fm,yerr=a_28_fs,marker='s',linestyle='--',markeredgecolor='limegreen',fmt='limegreen',ecolor='limegreen',label='28.6-Degree, Fixed')
plt.ylim(0,3)
plt.xlim(0,4)
plt.legend(loc='upper left')
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/fixed.png')



plt.figure()
plt.title('Development of Air Cavity After Impact')
plt.xlabel('Non-Dimensional Time ( Time (s) * Impact Velocity (m/s) / Arm Length (m) )')
plt.ylabel('Estimated Size of Body and Air Cavity')
plt.errorbar(x_axis,a_28_hm,yerr=a_28_hs,marker='o',linestyle='-',markeredgecolor='limegreen',fmt='limegreen',ecolor='limegreen',label='28.6-Degree, Hinge')
plt.errorbar(x_axis,a_10_hm,yerr=a_10_hs,marker='o',linestyle='-',markeredgecolor='black',fmt='black',ecolor='black',label='10.4-Degree, Hinge')
plt.errorbar(x_axis,t_007_m,yerr=t_007_s,marker='o',linestyle='-',markeredgecolor='mediumorchid',fmt='mediumorchid',ecolor='mediumorchid',label='0.00768Nm')
plt.errorbar(x_axis,t_018_m,yerr=t_018_s,marker='o',linestyle='-',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='0.0180Nm')
plt.errorbar(x_axis,t_015_m,yerr=t_015_s,marker='o',linestyle='-',markeredgecolor='turquoise',fmt='turquoise',ecolor='turquoise',label='0.0153Nm')
plt.ylim(0,6)
plt.xlim(0,4)
plt.legend(loc='upper left')
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/hinged.png')


time_to_turn = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/\
time_to_turn_angle.txt')
H28_time_to_turn = time_to_turn[0]
T136_time_to_turn = time_to_turn[1]
H22_time_to_turn = time_to_turn[2]
T153_time_to_turn = time_to_turn[3]

nonD_H28 = x_axis / H28_time_to_turn
nonD_H22 = x_axis / H22_time_to_turn
nonD_T136 = x_axis / T136_time_to_turn
nonD_T153 = x_axis / T153_time_to_turn
# Time to turn was measured in arm lengths

plt.figure()
#plt.title('Development of Air Cavity After Impact')
plt.xlabel('Non-Dimensional Time ( Time (s) / Time to Turn (s) )')
plt.ylabel('Estimated Size of Body and Air Cavity')
plt.errorbar(nonD_H28,a_28_hm,yerr=a_28_hs,marker='o',linestyle='-',markeredgecolor='limegreen',fmt='limegreen',ecolor='limegreen',label='28.6-Degree, Hinge')
#plt.errorbar(nonD_H10,a_10_hm,yerr=a_10_hs,marker='o',linestyle='-',markeredgecolor='black',fmt='black',ecolor='black',label='10.4-Degree, Hinge')
plt.errorbar(nonD_T136,t_007_m,yerr=t_007_s,marker='o',linestyle='-',markeredgecolor='mediumorchid',fmt='mediumorchid',ecolor='mediumorchid',label='0.00768Nm')
plt.errorbar(nonD_H22,t_018_m,yerr=t_018_s,marker='o',linestyle='-',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='0.0180Nm')
plt.errorbar(nonD_T153,t_015_m,yerr=t_015_s,marker='o',linestyle='-',markeredgecolor='turquoise',fmt='turquoise',ecolor='turquoise',label='0.0153Nm')
plt.ylim(0,6)
plt.xlim(0,2)
plt.legend(loc='upper left')
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/\
nonD_angle.png')

time_to_turn = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/\
time_to_turn_depth.txt')
H28_time_to_turn = time_to_turn[0]
T136_time_to_turn = time_to_turn[1]
H22_time_to_turn = time_to_turn[2]
T153_time_to_turn = time_to_turn[3]
H10_time_to_turn = time_to_turn[4]

nonD_H28 = x_axis / H28_time_to_turn
nonD_H22 = x_axis / H22_time_to_turn
nonD_T136 = x_axis / T136_time_to_turn
nonD_T153 = x_axis / T153_time_to_turn
nonD_H10 = x_axis / H10_time_to_turn
# Time to turn was measured in arm lengths

plt.figure()
#plt.title('Development of Air Cavity After Impact')
#plt.xlabel('Non-Dimensional Time ( Time (s) / Time to Turn (s) )')
#plt.ylabel('Estimated Size of Body and Air Cavity')
plt.errorbar(nonD_H28,a_28_hm,yerr=a_28_hs,marker='o',linestyle='-',markeredgecolor='limegreen',fmt='limegreen',ecolor='limegreen',label='W28')
plt.errorbar(nonD_T136,t_007_m,yerr=t_007_s,marker='o',linestyle='-',markeredgecolor='mediumorchid',fmt='mediumorchid',ecolor='mediumorchid',label='W22 S3')
plt.errorbar(nonD_H22,t_018_m,yerr=t_018_s,marker='o',linestyle='-',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='W22 S2')
plt.errorbar(nonD_T153,t_015_m,yerr=t_015_s,marker='o',linestyle='-',markeredgecolor='turquoise',fmt='turquoise',ecolor='turquoise',label='W22 S1')
plt.errorbar(nonD_H10,a_10_hm,yerr=a_10_hs,marker='o',linestyle='-',markeredgecolor='black',fmt='black',ecolor='black',label='W10')
plt.ylim(0,6)
plt.xlim(0,2)
plt.legend(loc='upper left')
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/\
nonD_depth.png')

time_to_turn = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/\
time_to_turn_upturn.txt')
H28_time_to_turn = time_to_turn[0]
T136_time_to_turn = time_to_turn[1]
H22_time_to_turn = time_to_turn[2]
T153_time_to_turn = time_to_turn[3]

nonD_H28 = x_axis / H28_time_to_turn
nonD_H22 = x_axis / H22_time_to_turn
nonD_T136 = x_axis / T136_time_to_turn
nonD_T153 = x_axis / T153_time_to_turn
# Time to turn was measured in arm lengths

plt.figure()
#plt.title('Development of Air Cavity After Impact')
plt.xlabel('Non-Dimensional Time ( Time (s) / Time to Turn (s) )')
plt.ylabel('Estimated Size of Body and Air Cavity')
plt.errorbar(nonD_H28,a_28_hm,yerr=a_28_hs,marker='o',linestyle='-',markeredgecolor='limegreen',fmt='limegreen',ecolor='limegreen',label='28.6-Degree, Hinge')
#plt.errorbar(nonD_H10,a_10_hm,yerr=a_10_hs,marker='o',linestyle='-',markeredgecolor='black',fmt='black',ecolor='black',label='10.4-Degree, Hinge')
plt.errorbar(nonD_T136,t_007_m,yerr=t_007_s,marker='o',linestyle='-',markeredgecolor='mediumorchid',fmt='mediumorchid',ecolor='mediumorchid',label='0.00768Nm')
plt.errorbar(nonD_H22,t_018_m,yerr=t_018_s,marker='o',linestyle='-',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='0.0180Nm')
plt.errorbar(nonD_T153,t_015_m,yerr=t_015_s,marker='o',linestyle='-',markeredgecolor='turquoise',fmt='turquoise',ecolor='turquoise',label='0.0153Nm')
plt.ylim(0,6)
plt.xlim(0,2)
plt.legend(loc='upper left')
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/\
nonD_upturn.png')


pinch_off = np.loadtxt('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/pinch_off/\
pinch_off_depth.txt',skiprows=1)
H10_pinch_off = (pinch_off[0] + fall_bl)/fall_bl
F10_pinch_off = (pinch_off[1] + spring_bl)/spring_bl
T007_pinch_off = (pinch_off[2] + fall_bl )/fall_bl
T018_pinch_off = (pinch_off[3] + fall_bl )/fall_bl
T015_pinch_off = (pinch_off[4] + fall_bl )/fall_bl
F22_pinch_off = (pinch_off[5] + spring_bl )/spring_bl
H28_pinch_off = (pinch_off[6] + fall_bl )/fall_bl
F28_pinch_off = (pinch_off[7] + spring_bl )/spring_bl

# Time to reach pinch off was measured in seconds
nonD_H10 = (x_axis / H10_pinch_off)
nonD_F10 = (x_axis / F10_pinch_off)
nonD_T007 = (x_axis / T007_pinch_off)
nonD_T018 = (x_axis / T018_pinch_off)
nonD_T015 = (x_axis / T015_pinch_off)
nonD_F22 = (x_axis / F22_pinch_off)
nonD_H28 = (x_axis / H28_pinch_off)
nonD_F28 = (x_axis / F28_pinch_off)

# Plot for the STD in Y direction
plt.figure()
#plt.title('Development of Air Cavity After Impact')
#plt.xlabel('Time (s) / Time of Pinch Off (s)')
#plt.ylabel('Estimated Size of Body and Air Cavity')
plt.errorbar(nonD_H28,a_28_hm,yerr=a_28_hs,marker='o',linestyle='-',markeredgecolor='limegreen',fmt='limegreen',ecolor='limegreen',label='W28')
plt.errorbar(nonD_T007,t_007_m,yerr=t_007_s,marker='o',linestyle='-',markeredgecolor='mediumorchid',fmt='mediumorchid',ecolor='mediumorchid',label='W22 S3')
plt.errorbar(nonD_T018,t_018_m,yerr=t_018_s,marker='o',linestyle='-',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='W22 S2')
plt.errorbar(nonD_T015,t_015_m,yerr=t_015_s,marker='o',linestyle='-',markeredgecolor='turquoise',fmt='turquoise',ecolor='turquoise',label='W22 S1')
plt.errorbar(nonD_H10,a_10_hm,yerr=a_10_hs,marker='o',linestyle='-',markeredgecolor='black',fmt='black',ecolor='black',label='W10')
#plt.errorbar(nonD_F28,a_28_fm,yerr=a_28_fs,marker='s',linestyle='--',markeredgecolor='limegreen',fmt='limegreen',ecolor='limegreen',label='28.6-Degree, Fixed')
#plt.errorbar(nonD_F22,a_22_fm,yerr=a_22_fs,marker='s',linestyle='--',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='22.7-Degree, Fixed')
#plt.errorbar(nonD_F10,a_10_fm,yerr=a_10_fs,marker='s',linestyle='--',markeredgecolor='black',fmt='black',ecolor='black',label='10.4-Degree, Fixed')
plt.ylim(0,6)
#plt.xlim(0,4)
#plt.legend(loc='upper left')
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/pinch_off/pinchoff_statistics.png')


print(';)')
