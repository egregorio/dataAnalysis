import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import glob
import os
from angle_functions import *

# Path to dimensional data
angle_path = '/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/angle_analysis/angle_info/angle_lists/angle_at_every_frame'
# Path to save plots
save_path = '/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/angle_analysis/plots'

# Define constants
fall_bl    = 0.06
impact_v   = 2.5

angle_918 = np.loadtxt(os.path.join(angle_path,'09182021_angles'))
angle_920 = np.loadtxt(os.path.join(angle_path,'09202021_angles'))
angle_921 = np.loadtxt(os.path.join(angle_path,'09212021_angles'))

def plot_angle(angle_list,input_color):
        shape = np.shape(angle_list)
        trials = shape[0]
        rows = shape[1]

        for i in range(0,trials):
		time = ( np.linspace(0,rows,num=rows) * impact_v ) / ( 6000 * fall_bl )
                plt.plot(time, angle_list[i], color = input_color)

plt.figure()
plot_angle(angle_918,'blue')
plot_angle(angle_920,'green')
plot_angle(angle_921,'red')
#plt.xlim(0, 0.6944)
plt.show()




