import numpy as np
import matplotlib.pyplot as plt


point1 = [0, -1]
point2 = [1, -1]
point3 = [2.5, -0.46]

x_array = [point1[0], point2[0], point3[0]]
y_array = [point1[1], point2[1], point3[1]]

velocity = np.poly1d( np.polyfit(x_array, y_array, 2) )
x = np.linspace(0,2.5,30)

position = np.polyint(velocity)
acceleration = np.polyder(velocity)

print(position)
print(velocity)
print(acceleration)

plt.figure()
plt.plot(point1[0],point1[1],'^',color='k',label='Impact Velocity')
plt.plot(point2[0],point2[1],'^',color='k')
plt.plot(point3[0],point3[1],'o',color='k',label='Reduced Entry Velocity')
plt.plot(x,velocity(x),'-',label='Velocity Curve')
plt.plot(x,position(x),'-',label='Trajectory Curve')
plt.plot(x,acceleration(x),'-',label='Acceleration Curve')
plt.xlabel('Simulation Time')
plt.ylim(-3,1)
plt.legend(loc='lower left')
#plt.show()
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/dissertation plots/simulationVelocityCurve.png')


