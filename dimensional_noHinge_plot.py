import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from get_t_bar import *
from conversions import *

# Import constants
constants = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/experiment_constants/constants.txt') 
body_length = constants[2]

# Import data from 04/04, no hinge, no hole
data_04 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/04042022_data')
all_04  = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/04042022_allData')
bef_04  = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/04042022_beforeImpact')
# Import data from 04/04, no hinge, hole
data_h04 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/04042022_hole_data')
all_h04  = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/04042022_hole_allData')
bef_h04  = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/04042022_hole_beforeImpact')

# Get all the dimensional values and convert meters to body lengths
time_04 = data_04[:,0]
mean_04 = data_04[:,3]# / body_length
mean_04 = mean_04 - mean_04[0]
mean_04[0] = 0

time_h04 = data_h04[:,0]
mean_h04 = data_h04[:,3]# / body_length
mean_h04 = mean_h04 - mean_h04[1]
mean_h04[0] = 0

bef_time = bef_04[:,0]
bef_mean = bef_04[:,1]# / body_length
bef_mean = bef_mean - bef_mean[0]
bef_mean[0] = 0

beh_time = bef_h04[:,0]
beh_mean = bef_h04[:,1]# / body_length
beh_mean = beh_mean - beh_mean[0]
beh_mean[0] = 0

bef_m, bef_b = np.polyfit(bef_time[0:110],bef_mean[0:110],1)
linearF_bef = get_linearFit(bef_m,bef_time)

beh_m, beh_b = np.polyfit(beh_time[0:110],beh_mean[0:110],1)
linearF_beh = get_linearFit(beh_m,beh_time)

mean_m = np.mean([bef_m, beh_m])
mean_b = np.mean([bef_b, beh_b])
stds_m = np.std([bef_m, beh_m])
stds_b = np.std([bef_b, beh_b])

print(mean_m)

saveData = [mean_m, mean_b]

np.savetxt('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/beforeImpact_noHinge_linearFit.txt',saveData)

plot_fit = np.linspace(-0.05,0,10)
best_fit = get_linearFit(mean_m,plot_fit)
print(len(plot_fit),len(best_fit))

# Plot for the STD in Y direction
plt.figure()
plt.title('Before Impact')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.plot(bef_time[0:110],bef_mean[0:110],color='hotpink',label='no hole')
plt.plot(beh_time[0:110],beh_mean[0:110],color='skyblue',label='hole')
#plt.plot(bef_time,linearF_bef,color='hotpink')
#plt.plot(beh_time,linearF_beh,color='skyblue')
plt.plot(plot_fit,best_fit,color='red',label='best fit')
plt.legend()
#plt.xlim(-0.08,0)
#plt.ylim(0,0.5)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/noHingeBefore.png')

# Plot for the STD in Y direction
plt.figure()
plt.title('After Impact')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.plot(time_04, mean_04, color='hotpink',label='no hole')
plt.plot(time_h04,mean_h04,color='skyblue',label='hole')
plt.legend()
#plt.xlim(-0.08,0)
#plt.ylim(0,0.5)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/noHingeAfter.png')

# Plot for the STD in Y direction
plt.figure()
plt.title('Impact')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.plot(plot_fit,best_fit,color='purple', label='V = 2.4 m/s')
plt.plot(time_04, mean_04, color='hotpink',label='no hole')
plt.plot(time_h04,mean_h04,color='skyblue',label='hole')
plt.legend()
plt.xlim(-0.05,0.05)
plt.ylim(-0.15,0.15)
plt.savefig('/Users/elizabeth/Box Sync/dataAnalysis/plots_switzerland/noHinge.png')

print(';)')
