import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Import data from 04/04, no hinge, no hole
all_stif = np.loadtxt('/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/all_trials/stiffness.txt')
all_stat = np.loadtxt('/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/all_trials/statistics.txt')
all_size = np.loadtxt('/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/all_trials/normalized.txt')

x_axis = [0.1,0.25,0.5,0.75,1,1.25,1.5,1.75,2,2.25,2.5,2.75,3,3.25,3.5,3.75,4]

tor_136_m = all_stif[:,0] # 9/18
tor_136_s = all_stif[:,1] # 9/18
tor_153_m = all_stif[:,4] # 9/21
tor_153_s = all_stif[:,5] # 9/21
tor_154_m = all_stif[:,2] # 9/20
tor_154_s = all_stif[:,3] # 9/20
tor_avg_m = all_stif[:,6] # average
tor_avg_s = all_stif[:,7] # average
tor_fix_m = all_stif[:,8] # fixed
tor_fix_s = all_stif[:,9] # fixed

#hinge_10_m = all_stat[:,0]
#hinge_10_s = all_stat[:,1]
#block_10_m = all_stat[:,2]
#block_10_s = all_stat[:,3]
#hinge_22_m = all_stat[:,4]
#hinge_22_s = all_stat[:,5]
#block_22_m = all_stat[:,6]
#block_22_s = all_stat[:,7]
#hinge_28_m = all_stat[:,8]
#hinge_28_s = all_stat[:,9]
#block_28_m = all_stat[:,10]
#block_28_s = all_stat[:,11]

hinge_10_m = all_size[:,0]
hinge_10_s = all_size[:,1]
block_10_m = all_size[:,2]
block_10_s = all_size[:,3]
hinge_22_m = all_size[:,4]
hinge_22_s = all_size[:,5]
block_22_m = all_size[:,6]
block_22_s = all_size[:,7]
hinge_28_m = all_size[:,8]
hinge_28_s = all_size[:,9]
block_28_m = all_size[:,10]
block_28_s = all_size[:,11]


# Plot for the STD in Y direction
plt.figure()
#plt.title('Development of Air Cavity After Impact')
plt.xlabel('Depth in Arm Lengths')
plt.ylabel('Estimated Size of Body and Air Cavity')
plt.errorbar(x_axis,hinge_28_m,yerr=hinge_28_s,marker='o',linestyle='-',markeredgecolor='limegreen',fmt='limegreen',ecolor='limegreen',label='28.6-Degree, Hinge')
plt.errorbar(x_axis,hinge_22_m,yerr=hinge_22_s,marker='o',linestyle='-',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='22.7-Degree, Hinge')
plt.errorbar(x_axis,hinge_10_m,yerr=hinge_10_s,marker='o',linestyle='-',markeredgecolor='black',fmt='black',ecolor='black',label='10.4-Degree, Hinge')
plt.errorbar(x_axis,block_28_m,yerr=block_28_s,marker='s',linestyle='--',markeredgecolor='limegreen',fmt='limegreen',ecolor='limegreen',label='28.6-Degree, Fixed')
plt.errorbar(x_axis,block_22_m,yerr=block_22_s,marker='s',linestyle='--',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='22.7-Degree, Fixed')
plt.errorbar(x_axis,block_10_m,yerr=block_10_s,marker='s',linestyle='--',markeredgecolor='black',fmt='black',ecolor='black',label='10.4-Degree, Fixed')
#plt.axhline(y = 3, color = 'r', linestyle = '-')
plt.ylim(0,7)
plt.xlim(0,4)
plt.legend(loc='upper left')
#plt.savefig('/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/all_trials/statistics.png')
plt.savefig('/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/all_trials/normalized.png')

plt.figure()
plt.title('Development of Air Cavity After Impact')
plt.xlabel('Depth in Arm Lengths')
plt.ylabel('Estimated Size of Body and Air Cavity')
plt.errorbar(x_axis,tor_136_m,yerr=tor_136_s,marker='o',linestyle='-',markeredgecolor='mediumorchid',fmt='mediumorchid',ecolor='mediumorchid',label='0.0768Nm')
plt.errorbar(x_axis,tor_154_m,yerr=tor_154_s,marker='o',linestyle='-',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='0.0180Nm')
plt.errorbar(x_axis,tor_153_m,yerr=tor_153_s,marker='o',linestyle='-',markeredgecolor='turquoise',fmt='turquoise',ecolor='turquoise',label='0.0153Nm')
plt.errorbar(x_axis,block_22_m,yerr=block_22_s,marker='s',linestyle='--',markeredgecolor='royalblue',fmt='royalblue',ecolor='royalblue',label='Fixed')
plt.ylim(0,7)
plt.xlim(0,4)
plt.axhline(y = 3.15, color = 'r', linestyle = '-')
plt.legend(loc='upper left')
plt.savefig('/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/all_trials/stiffness_line.png')


print(';)')
