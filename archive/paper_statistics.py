import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Import data from 04/04, no hinge, no hole
all_stat = np.loadtxt('/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/air_cavity_statistics.txt',skiprows=2)
#,delimiter=' '
x_axis = [0.1,0.25,0.5,0.75,1,1.25,1.5,1.75,2,2.25,2.5,2.75,3,3.25,3.5,3.75]

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
plt.xlabel('Depth in Arm Lengths')
plt.ylabel('Estimated Size of Body and Air Cavity')
plt.errorbar(x_axis,a_28_hm,yerr=a_28_hs,marker='o',linestyle='-',markeredgecolor='black',fmt='black',ecolor='black',label='Hinge')
plt.errorbar(x_axis,a_28_fm,yerr=a_28_fs,marker='s',linestyle='--',markeredgecolor='black',fmt='black',ecolor='black',label='Fixed')
plt.ylim(0,5)
plt.xlim(0,4)
plt.legend(loc='upper left')
plt.savefig('/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/3minute.png')

# Plot for the STD in Y direction
plt.figure()
plt.title('Development of Air Cavity After Impact')
plt.xlabel('Depth in Arm Lengths')
plt.ylabel('Estimated Size of Body and Air Cavity')
plt.errorbar(x_axis,a_28_hm,yerr=a_28_hs,marker='o',linestyle='-',markeredgecolor='limegreen',fmt='limegreen',ecolor='limegreen',label='28.6-Degree, Hinge')
plt.errorbar(x_axis,t_018_m,yerr=t_018_s,marker='o',linestyle='-',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='22.7-Degree, Hinge')
plt.errorbar(x_axis,a_10_hm,yerr=a_10_hs,marker='o',linestyle='-',markeredgecolor='black',fmt='black',ecolor='black',label='10.4-Degree, Hinge')
plt.errorbar(x_axis,a_28_fm,yerr=a_28_fs,marker='s',linestyle='--',markeredgecolor='limegreen',fmt='limegreen',ecolor='limegreen',label='28.6-Degree, Fixed')
plt.errorbar(x_axis,a_22_fm,yerr=a_22_fs,marker='s',linestyle='--',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='22.7-Degree, Fixed')
plt.errorbar(x_axis,a_10_fm,yerr=a_10_fs,marker='s',linestyle='--',markeredgecolor='black',fmt='black',ecolor='black',label='10.4-Degree, Fixed')
plt.ylim(0,6)
plt.xlim(0,4)
plt.legend(loc='upper left')
plt.savefig('/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/normalized.png')

plt.figure()
plt.title('Development of Air Cavity After Impact')
plt.xlabel('Depth in Arm Lengths')
plt.ylabel('Estimated Size of Body and Air Cavity')
plt.errorbar(x_axis,t_007_m,yerr=t_007_s,marker='o',linestyle='-',markeredgecolor='mediumorchid',fmt='mediumorchid',ecolor='mediumorchid',label='0.00768Nm')
plt.errorbar(x_axis,t_018_m,yerr=t_018_s,marker='o',linestyle='-',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='0.0180Nm')
plt.errorbar(x_axis,t_015_m,yerr=t_015_s,marker='o',linestyle='-',markeredgecolor='turquoise',fmt='turquoise',ecolor='turquoise',label='0.0153Nm')
plt.errorbar(x_axis,a_22_fm,yerr=a_22_fs,marker='s',linestyle='--',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='Fixed')
plt.ylim(0,6)
plt.xlim(0,4)
plt.legend(loc='upper left')
plt.savefig('/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/stiffness.png')


plt.figure()
plt.title('Development of Air Cavity After Impact')
plt.xlabel('Depth in Arm Lengths')
plt.ylabel('Estimated Size of Body and Air Cavity')
plt.errorbar(x_axis,a_10_fm,yerr=a_10_fs,marker='s',linestyle='--',markeredgecolor='black',fmt='black',ecolor='black',label='10.4-Degree, Fixed')
plt.errorbar(x_axis,a_22_fm,yerr=a_22_fs,marker='s',linestyle='--',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='22.7-Degree, Fixed')
plt.errorbar(x_axis,a_28_fm,yerr=a_28_fs,marker='s',linestyle='--',markeredgecolor='limegreen',fmt='limegreen',ecolor='limegreen',label='28.6-Degree, Fixed')
plt.ylim(0,3)
plt.xlim(0,4)
plt.legend(loc='upper left')
plt.savefig('/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/fixed.png')



plt.figure()
plt.title('Development of Air Cavity After Impact')
plt.xlabel('Depth in Arm Lengths')
plt.ylabel('Estimated Size of Body and Air Cavity')
plt.errorbar(x_axis,a_28_hm,yerr=a_28_hs,marker='o',linestyle='-',markeredgecolor='limegreen',fmt='limegreen',ecolor='limegreen',label='28.6-Degree, Hinge')
plt.errorbar(x_axis,a_10_hm,yerr=a_10_hs,marker='o',linestyle='-',markeredgecolor='black',fmt='black',ecolor='black',label='10.4-Degree, Hinge')
plt.errorbar(x_axis,t_007_m,yerr=t_007_s,marker='o',linestyle='-',markeredgecolor='mediumorchid',fmt='mediumorchid',ecolor='mediumorchid',label='0.00768Nm')
plt.errorbar(x_axis,t_018_m,yerr=t_018_s,marker='o',linestyle='-',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='0.0180Nm')
plt.errorbar(x_axis,t_015_m,yerr=t_015_s,marker='o',linestyle='-',markeredgecolor='turquoise',fmt='turquoise',ecolor='turquoise',label='0.0153Nm')
plt.ylim(0,6)
plt.xlim(0,4)
plt.legend(loc='upper left')
plt.savefig('/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/body_and_cavity/hinged.png')


print(';)')
