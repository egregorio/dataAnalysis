import numpy as np
import matplotlib.pyplot as plt
import scipy
from functions import *

raw001 = np.loadtxt('001data.csv',delimiter=',',skiprows=0)
raw002 = np.loadtxt('002data.csv',delimiter=',',skiprows=0)
raw003 = np.loadtxt('003data.csv',delimiter=',',skiprows=0)
raw004 = np.loadtxt('004data.csv',delimiter=',',skiprows=0)
raw006 = np.loadtxt('006data.csv',delimiter=',',skiprows=0)
raw007 = np.loadtxt('007data.csv',delimiter=',',skiprows=0)
raw008 = np.loadtxt('008data.csv',delimiter=',',skiprows=0)
raw009 = np.loadtxt('009data.csv',delimiter=',',skiprows=0)
raw010 = np.loadtxt('010data.csv',delimiter=',',skiprows=0)
raw011 = np.loadtxt('011data.csv',delimiter=',',skiprows=0)


x01, y01, x01_length, y01_length = getArms(raw001)
x02, y02, x02_length, y02_length = getArms(raw002)
x03, y03, x03_length, y03_length = getArms(raw003)
x04, y04, x04_length, y04_length = getArms(raw004)
x06, y06, x06_length, y06_length = getArms(raw006)
x07, y07, x07_length, y07_length = getArms(raw007)
x08, y08, x08_length, y08_length = getArms(raw008)
x09, y09, x09_length, y09_length = getArms(raw009)
x10, y10, x10_length, y10_length = getArms(raw010)
x11, y11, x11_length, y11_length = getArms(raw011)


input_x = [ x01, x02, x03, x04, x06, 
            x07, x08, x09, x10, x11 ]

input_y = [ y01, y02, y03, y04, y06, 
            y07, y08, y09, y10, y11 ]

x_lengths = [x01_length, x02_length, x03_length, x04_length, x06_length,
             x07_length, x08_length, x09_length, x10_length, x11_length]

y_lengths = [y01_length, y02_length, y03_length, y04_length, y06_length,
             y07_length, y08_length, y09_length, y10_length, y11_length]

x_max_length = max(x_lengths)
y_max_length = max(y_lengths)

padded_x = create_one(input_x, x_max_length)
padded_y = create_one(input_y, y_max_length)

means_x, x_stds = averageF( padded_x, x_max_length)
means_y, y_stds = averageF( padded_y, y_max_length)

plot_x = np.linspace(0,1,350)#x_max_length)

# Plot for the Means in Y direction
plt.figure()
plt.title('Y Coordinates / Height v. Time')
plt.xlabel('Non-Dimensional Time')
plt.ylabel('Height in Body Lengths')
plt.plot(plot_x,means_x[0:350])
#plt.xlim(0,1)
plt.ylim(1.6,2.6)
plt.savefig('plots/yMean.png')

# Plot for the Means in X direction
plt.figure()
plt.title('X Coordinates v. Time')
plt.xlabel('Non-Dimensional Time')
plt.ylabel('Horizonal Position in Body Lengths')
plt.plot(plot_x,means_y[0:350])
plt.xlim(0,1)
plt.ylim(0.2,0.8)
plt.savefig('plots/xMean.png')

# Plot for the STD in Y direction
plt.figure()
plt.title('Y Coordinates / Height v. Time')
plt.xlabel('Non-Dimensional Time')
plt.ylabel('Height in Body Lengths')
plt.errorbar(plot_x,means_x[0:350],yerr=x_stds[0:350],fmt='k',ecolor='c')
plt.xlim(0,1)
plt.ylim(1.6,2.6)
plt.savefig('plots/yStd.png')

# Plot for the STD in X direction
plt.figure()
plt.title('X Coordinates v. Time')
plt.xlabel('Non-Dimensional Time')
plt.ylabel('Horizonal Position in Body Lengths')
plt.errorbar(plot_x,means_y[0:350],yerr=y_stds[0:350],fmt='k',ecolor='c')
plt.xlim(0,1)
plt.ylim(0.2,0.8)
plt.savefig('plots/xStd.png')

print('youre amazing!!')
