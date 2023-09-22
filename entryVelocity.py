import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from scipy.interpolate import CubicSpline
import scipy
from dimensional_functions import *
from get_t_bar import *

current_file = '/Users/elizabeth/Downloads/impact velocity/AfterImpact.csv'

# Import data from 7/29
data = np.loadtxt(current_file,delimiter=',',skiprows=0)

waterLevel = 337.8128945

hands1_y = []
hands1_x = []
hands2_y = []
hands2_x = []
legs1_y = []
legs1_x = []
legs2_y = []
legs2_x = []

jIndex_hands1 = []
jIndex_hands2 = []
jIndex_legs1 = []
jIndex_legs2 = []

for i in range(0,len(data[:,0])):
	check_hands1_y = data[:,0]
	check_legs1_y = data[:,4]
	check_hands2_y = data[:,2]
	check_legs2_y = data[:,6]
	if(check_hands1_y[i] != 0):
		hands1_y.append(data[i,0] - waterLevel)
		hands1_x.append(data[i,1])
		jIndex_hands1.append(i)
	if(check_hands2_y[i] != 0):
		hands2_y.append(data[i,2] - waterLevel)
		hands2_x.append(data[i,3])
		jIndex_hands2.append(i)
	if(check_legs1_y[i] != 0):
		legs1_y.append(data[i,4] - waterLevel)
		legs1_x.append(data[i,5])
		jIndex_legs1.append(i)
	if(check_legs2_y[i] != 0):
		legs2_y.append(data[i,6] - waterLevel)
		legs2_x.append(data[i,7])
		jIndex_legs2.append(i)

hands1_start = jIndex_hands1[0]
hands2_start = jIndex_hands2[0]
legs1_start = jIndex_legs1[0] / 5150
legs2_start = jIndex_legs2[0] / 5150

point_x1 = legs1_x[0]
point_y1 = legs1_y[0]
point_x2 = legs2_x[0]
point_y2 = legs2_y[0]

point_x3 = legs1_x[-1]
point_y3 = legs1_y[-1]
point_x4 = legs2_x[-1]
point_y4 = legs2_y[-1]



distance_above = np.sqrt((point_x1 - point_x2)**2 + (point_y1 - point_y2)**2)
distance_below = np.sqrt((point_x3 - point_x4)**2 + (point_y3 - point_y4)**2)
ppm_above = distance_above / 0.0254
ppm_below = distance_below / 0.0254

x_arrays = [ hands1_x, hands2_x, legs1_x, legs2_x]
y_arrays = [ hands1_y, hands2_y, legs1_y, legs2_y]

for i in range(0,4):
	x_array = x_arrays[i]
	y_array = y_arrays[i]
	for j in range(0,len(y_array)):
		if (y_array[j] >= 0):
			x_array[j] = x_array[j] / ppm_above
			y_array[j] = y_array[j] / ppm_above
		if (y_array[j] < 0):
			x_array[j] = x_array[j] / ppm_below
			y_array[j] = y_array[j] / ppm_below

hands1_above = list(filter( lambda e: e>= 0, hands1_y ))
hands2_above = list(filter( lambda e: e>= 0, hands2_y ))

legs1_above = list(filter( lambda e: e>= 0, legs1_y ))
legs2_above = list(filter( lambda e: e>= 0, legs2_y ))
legs1_below = list(filter( lambda e: e< 0, legs1_y ))
legs2_below = list(filter( lambda e: e< 0, legs2_y ))

hands1_time = frames_to_sec(hands1_above,5150)
hands2_time = frames_to_sec(hands2_above,5150)
legs1_time = frames_to_sec(legs1_y,5150)
legs2_time = frames_to_sec(legs2_y,5150)
legs1_time_above = frames_to_sec(legs1_above,5150)
legs2_time_above = frames_to_sec(legs2_above,5150)
legs1_time_below = frames_to_sec(legs1_below,5150)
legs2_time_below = frames_to_sec(legs2_below,5150)


legs1_time_below = legs1_time_below - hands1_time[-1] + legs1_time_above[-1] + legs1_start
legs2_time_below = legs2_time_below - hands2_time[-1] + legs2_time_above[-1] + legs2_start
legs1_time = legs1_time - hands1_time[-1] + legs1_start
legs2_time = legs2_time - hands2_time[-1] + legs2_start
legs1_time_above = legs1_time_above - hands1_time[-1] + legs1_start
legs2_time_above = legs2_time_above - hands2_time[-1] + legs2_start
hands1_time = hands1_time - hands1_time[-1]
hands2_time = hands2_time - hands2_time[-1]
#print(hands1_time[-1])

# Hands Intertolation Above the Free Surface, Tracking Stopped After Impact
hands1_a, hands1_b = np.polyfit(hands1_time,hands1_above,1)
hands1_linear = get_linearFit_withB(hands1_a, hands1_time, hands1_b)
hands2_a, hands2_b = np.polyfit(hands2_time,hands2_above,1)
hands2_linear = get_linearFit_withB(hands2_a, hands2_time, hands2_b)

# Legs Interpolation Above the Free Surface
legs1_above_a, legs1_above_b = np.polyfit(legs1_time_above,legs1_above,1)
legs1_above_linear           = get_linearFit_withB(legs1_above_a, legs1_time_above, legs1_above_b)
legs2_above_a, legs2_above_b = np.polyfit(legs2_time_above,legs2_above,1)
legs2_above_linear           = get_linearFit_withB(legs2_above_a, legs2_time_above, legs2_above_b)
# Legs Interpolation Below the Free Surface
legs1_below_a, legs1_below_b = np.polyfit(legs1_time_below,legs1_below,1)
legs1_below_linear           = get_linearFit_withB(legs1_below_a, legs1_time_below, legs1_below_b)
legs2_below_a, legs2_below_b = np.polyfit(legs2_time_below,legs2_below,1)
legs2_below_linear           = get_linearFit_withB(legs2_below_a, legs2_time_below, legs2_below_b)
#print(legs1_a,legs1_b)
print(hands1_a,legs1_above_a,legs1_below_a)
print(hands2_a,legs2_above_a,legs2_below_a)

legs1_scaled = legs1_above + legs1_below
legs2_scaled = legs2_above + legs2_below

legs1_spline = CubicSpline(legs1_time, legs1_scaled)
legs2_spline = CubicSpline(legs2_time, legs2_scaled)

plt.figure()
plt.xlabel('Time (s)')
plt.ylabel('Distance from Interface (m)')
plt.plot(legs1_time[::15],legs1_y[::15],'o',color='mediumseagreen',label='Legs Position')
plt.plot(hands1_time[::15],hands1_y[::15],'o',color='mediumseagreen',label='Hands Position')
plt.plot(hands1_time, hands1_linear,'--',color='blue',label='Linear Interpolation')
plt.plot(legs1_time_above, legs1_above_linear,'--',color='blue',label='Linear Interpolation')
plt.plot(legs1_time_below, legs1_below_linear,'--',color='blue',label='Linear Interpolation')
plt.plot(legs1_time, legs1_spline(legs1_time),color='red',label='Cubic Interpolation')
#plt.plot(legs2_time, legs2_spline(legs2_time),color='red',label='Cubic Interpolation')
plt.legend()
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/dissertation plots/\
W10_PositionInterpolation')


print(';)')

