import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from get_t_bar import *
from conversions import *

# Import data from 04/04, no hinge, no hole
data_1 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/no_hinge/04052022_a1_Y')
data_2 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/no_hinge/04042022_a2_Y')
data_3 = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/no_hinge/04052022_a3_Y')

# Import and assign constants
exp_const = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/experiment_constants/constants.txt')
mass_diver = exp_const[0]
fall_bl    = exp_const[1]
spring_bl  = exp_const[2]
impact_v   = exp_const[3]

spring_shape = impact_v / spring_bl

# Get all the dimensional values and convert meters to body lengths
all_1 = data_1 / spring_bl
all_2 = data_2 / spring_bl
all_3 = data_3 / spring_bl

print(spring_bl)

# Plot for the STD in Y direction
plt.figure()
plt.title('Movement of Arms in Y Direction After Impact')
plt.xlabel('Non-Dimensional Time ( t * v / l )')
plt.ylabel('Depth (Arm Lengths)')
plt.plot(all_1[0], color='hotpink',label='10.4-deg')
plt.plot(all_1[1], color='hotpink',label='10.4-deg')
#plt.plot(all_1[2], color='hotpink',label='10.4-deg')
#plt.plot(all_1[3], color='hotpink',label='10.4-deg')
plt.plot(all_2[0], color='springgreen',label='22.7-deg')
plt.plot(all_2[1], color='springgreen',label='22.7-deg')
#plt.plot(all_2[2], color='springgreen',label='22.7-deg')
#plt.plot(all_2[3], color='springgreen',label='22.7-deg')
plt.plot(all_3[0], color='mediumpurple',label='28.6-deg')
plt.plot(all_3[1], color='mediumpurple',label='28.6-deg')
#plt.plot(all_3[2], color='mediumpurple',label='28.6-deg')
#plt.plot(all_3[3], color='mediumpurple',label='28.6-deg')
#plt.legend()
plt.savefig('/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/all_trials/noHinge.png')

print(';)')
