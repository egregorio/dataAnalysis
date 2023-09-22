# import libraries
import numpy as np
import missingno as msno
import matplotlib.pyplot as plt
import pandas as pd
import csv
import os
import glob
from mpl_toolkits import mplot3d

density_ratio = 997 / 1.23
SA = 0.176

# name the files you want to import
P = '/Users/elizabeth/Desktop/parts';

con = '/W22_80points/';

conFiles = glob.glob(P + con + 'parts.*');
conTime = glob.glob(P + con + 'time.txt');
conTimeList = np.loadtxt(conTime[0])
conTauList = (conTimeList - 1)*2

var = '/W22_varVel/';

varFiles = glob.glob(P + var + 'parts.*');
varTime = glob.glob(P + var + 'time.txt');
varTimeList = np.loadtxt(varTime[0])
varTauList = (varTimeList - 1)*2


parts_file = glob.glob(P + '/parts_names.txt')
with open(parts_file[0], 'r') as file:
    data = file.read().splitlines()


conCp = []
varCp = []
conCl = []
varCl = []
conCd = []
varCd = []
conDrag = []
varDrag = []

''' START: Pressure Coefficient
for i in range(0,len(conFiles)):
    current_file = np.loadtxt(glob.glob(P + con + data[i])[0],skiprows=2)
    netPressure = sum(current_file[:,6]) * density_ratio 
    C_p = netPressure / 0.5
    conCp.append(C_p)
#    net_force_xz = sum(current_file[:,7]) + sum(current_file[:,9])
#    C_l = ( net_force_xz + netPressure ) / ( ( 1 / density_ratio ) * SA )
#    conCl.append(C_l)
    
for i in range(0,len(varFiles)):
    current_file = np.loadtxt(glob.glob(P + var + data[i])[0],skiprows=2)
    netPressure = sum(current_file[:,6]) * density_ratio 
    C_p = netPressure / 0.5
    varCp.append(C_p)
#    net_force_xz = sum(current_file[:,7]) + sum(current_file[:,9])
#    C_l = ( net_force_xz + netPressure ) / ( ( 1 / density_ratio ) * SA )
#    varCl.append(C_l)


plt.figure()
plt.plot(conTauList[1:],conCp,color='mediumturquoise',label='Constant Velocity')
plt.plot(varTauList[1:-120],varCp,color='goldenrod',label='Decreasing Velocity')
plt.legend(loc='lower left')
plt.xlim(-1,3)
#plt.ylim(0,2500)
#plt.show()
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/dissertation plots/\
pressureCoefficent.png')

END: Pressure Coefficient
'''

'''
plt.figure()
plt.plot(conTauList[1:],conCl,color='mediumturquoise',label='Constant Velocity')
plt.plot(varTauList[1:-120],varCl,color='goldenrod',label='Decreasing Velocity')
plt.xlim(-1,3)
#plt.ylim(0,2500)
#plt.show()
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/dissertation plots/\
liftCoefficent.png')

plt.figure()
plt.plot(conTauList[1:],conDrag,color='mediumturquoise',label='Constant Velocity')
plt.plot(varTauList[1:-120],varDrag,color='goldenrod',label='Decreasing Velocity')
plt.xlim(-1,3)
#plt.ylim(0,2500)
#plt.show()
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/dissertation plots/\
dragCoefficent.png')
'''

force_frames = [100,125,150,175,200,225]
force_100_con = []
force_125_con = []
force_150_con = []
force_175_con = []
force_200_con = []
force_225_con = []
force_100_var = []
force_125_var = []
force_150_var = []
force_175_var = []
force_200_var = []
force_225_var = []


for i in range(0,len(force_frames)):
    current_file = np.loadtxt(glob.glob(P + con + data[force_frames[i]])[0],skiprows=2)
    netPressure = sum(current_file[:,6]) * density_ratio 
    force_array = []
    for j in range(0,len(current_file[:,0])):
        force_y = current_file[i,8]
        C_d = 2 * ( force_y + netPressure ) / ( ( 1 / density_ratio ) * SA )
        conDrag = C_d * 0.5 * ( 1 / density_ratio ) * SA
        force_array.append(conDrag)
    if (force_frames[i] == 100):
        force_100_con = force_array
    if (force_frames[i] == 125):
        force_125_con = force_array
    if (force_frames[i] == 150):
        force_150_con = force_array
    if (force_frames[i] == 175):
        force_175_con = force_array
    if (force_frames[i] == 200):
        force_200_con = force_array
    if (force_frames[i] == 225):
        force_225_con = force_array

for i in range(0,len(force_frames)):
    current_file = np.loadtxt(glob.glob(P + var + data[force_frames[i]])[0],skiprows=2)
    netPressure = sum(current_file[:,6]) * density_ratio 
    force_array = []
    for j in range(0,len(current_file[:,0])):
        force_y = current_file[i,8]
        C_d = 2 * ( force_y + netPressure ) / ( ( 1 / density_ratio ) * SA )
        varDrag = C_d * 0.5 * ( 1 / density_ratio ) * SA
        force_array.append(conDrag)
    if (force_frames[i] == 100):
        force_100_var = force_array
    if (force_frames[i] == 125):
        force_125_var = force_array
    if (force_frames[i] == 150):
        force_150_var = force_array
    if (force_frames[i] == 175):
        force_175_var = force_array
    if (force_frames[i] == 200):
        force_200_var = force_array
    if (force_frames[i] == 225):
        force_225_var = force_array


con_X_100 = np.loadtxt(glob.glob(P + var + data[100])[0],skiprows=2)[:,0]
con_Y_100 = np.loadtxt(glob.glob(P + var + data[100])[0],skiprows=2)[:,1]
con_Z_100 = np.loadtxt(glob.glob(P + var + data[100])[0],skiprows=2)[:,2]

con_X_125 = np.loadtxt(glob.glob(P + var + data[125])[0],skiprows=2)[:,0]
con_Y_125 = np.loadtxt(glob.glob(P + var + data[125])[0],skiprows=2)[:,1]
con_Z_125 = np.loadtxt(glob.glob(P + var + data[125])[0],skiprows=2)[:,2]

con_X_150 = np.loadtxt(glob.glob(P + var + data[150])[0],skiprows=2)[:,0]
con_Y_150 = np.loadtxt(glob.glob(P + var + data[150])[0],skiprows=2)[:,1]
con_Z_150 = np.loadtxt(glob.glob(P + var + data[150])[0],skiprows=2)[:,2]

con_X_175 = np.loadtxt(glob.glob(P + var + data[175])[0],skiprows=2)[:,0]
con_Y_175 = np.loadtxt(glob.glob(P + var + data[175])[0],skiprows=2)[:,1]
con_Z_175 = np.loadtxt(glob.glob(P + var + data[175])[0],skiprows=2)[:,2]

con_X_200 = np.loadtxt(glob.glob(P + var + data[200])[0],skiprows=2)[:,0]
con_Y_200 = np.loadtxt(glob.glob(P + var + data[200])[0],skiprows=2)[:,1]
con_Z_200 = np.loadtxt(glob.glob(P + var + data[200])[0],skiprows=2)[:,2]

con_X_225 = np.loadtxt(glob.glob(P + var + data[225])[0],skiprows=2)[:,0]
con_Y_225 = np.loadtxt(glob.glob(P + var + data[225])[0],skiprows=2)[:,1]
con_Z_225 = np.loadtxt(glob.glob(P + var + data[225])[0],skiprows=2)[:,2]


fig = plt.figure()
ax = plt.axes(projection='3d')
surf = ax.scatter3D(con_X_100, con_Z_100, con_Y_100, c=force_100_con, cmap='Greens');
ax.view_init(elev=0, azim=180)
ax.set_box_aspect((1,1,5))
ax.set_axis_off()
fig.colorbar(surf, shrink=0.5, aspect=5,vmin=-1, vmax=-.85)
fig.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/dissertation plots/\
dragForce_con100.png')

fig = plt.figure()
ax = plt.axes(projection='3d')
surf = ax.scatter3D(con_X_125, con_Z_125, con_Y_125, c=force_125_con, cmap='Greens');
ax.view_init(elev=0, azim=180)
ax.set_box_aspect((1,1,5))
ax.set_axis_off()
fig.colorbar(surf, shrink=0.5, aspect=5,vmin=-1, vmax=-.85)
fig.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/dissertation plots/\
dragForce_con125.png')

fig = plt.figure()
ax = plt.axes(projection='3d')
surf = ax.scatter3D(con_X_150, con_Z_150, con_Y_150, c=force_150_con, cmap='Greens');
ax.view_init(elev=0, azim=180)
ax.set_box_aspect((1,1,5))
ax.set_axis_off()
fig.colorbar(surf, shrink=0.5, aspect=5,vmin=-1, vmax=-.85)
fig.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/dissertation plots/\
dragForce_con150.png')

fig = plt.figure()
ax = plt.axes(projection='3d')
surf = ax.scatter3D(con_X_175, con_Z_175, con_Y_175, c=force_125_con, cmap='Greens');
ax.view_init(elev=0, azim=180)
ax.set_box_aspect((1,1,5))
ax.set_axis_off()
fig.colorbar(surf, shrink=0.5, aspect=5,vmin=-1, vmax=-.85)
fig.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/dissertation plots/\
dragForce_con175.png')




