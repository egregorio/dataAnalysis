import numpy as np
import os

# Path to Data Files
#save_path = '/Users/elizabeth/Box Sync/dataAnalysis/plots_paper/rough_draft/angle_lists'
fall_path = '/Users/elizabeth/Box Sync/dataAnalysis/plots_paper/rough_draft/frame_lists/fall_2021'
spring_path = '/Users/elizabeth/Box Sync/dataAnalysis/plots_paper/rough_draft/frame_lists/spring_2022'
august_path = '/Users/elizabeth/Box Sync/dataAnalysis/plots_paper/rough_draft/frame_lists/august_2022'

# Names of Data Files
#name_frame     = 'frame_d_0.0'
#name_depth     = 'depth_d_0.0'
#name_angle     = 'angle_d_0.0'
name_frame     = 'frame_bl_0.0'
name_depth     = 'depth_bl_0.0'
name_file      = 'files_bl_0.0'

# Join Paths
#angle_path = os.path.join(save_path,name_angle)
#depth_path = os.path.join(save_path,name_depth)
#frame_path = os.path.join(save_path,name_frame)
depth_fall = os.path.join(fall_path,name_depth)
depth_spring = os.path.join(spring_path,name_depth)
depth_august = os.path.join(august_path,name_depth)
frame_fall = os.path.join(fall_path,name_frame)
frame_spring = os.path.join(spring_path,name_frame)
frame_august = os.path.join(august_path,name_frame)
file_fall = os.path.join(fall_path,name_file)
file_spring = os.path.join(spring_path,name_file)
file_august = os.path.join(august_path,name_file)

# Load Text as Arrays
#angle = np.loadtxt(angle_path)
#depth = np.loadtxt(depth_path)
#frame = np.loadtxt(frame_path)
deptf = np.loadtxt(depth_fall)
depts = np.loadtxt(depth_spring)
depta = np.loadtxt(depth_august)
framf = np.loadtxt(frame_fall)
frams = np.loadtxt(frame_spring)
frama = np.loadtxt(frame_august)
filef = np.loadtxt(file_fall,dtype='str')
files = np.loadtxt(file_spring,dtype='str')
filea = np.loadtxt(file_august,dtype='str')

print(np.shape(deptf),np.shape(framf))
print(np.shape(depts),np.shape(frams))
print(np.shape(depta),np.shape(frama))

#print angle[0,0],depth[0,0],frame[0,0]
#print angle[1,0],depth[1,0],frame[1,0]
#print angle[2,0],depth[2,0],frame[2,0]
#print angle[3,0],depth[3,0],frame[3,0]
#print angle[4,0],depth[4,0],frame[4,0]

print deptf[0,0],framf[0,0]
print deptf[1,0],framf[1,0]
print deptf[2,0],framf[2,0]
print deptf[3,0],framf[3,0]
print deptf[4,0],framf[4,0]
print ''
print filef[0,1]
print filef[1,1]
print filef[2,1]
print filef[3,1]
print filef[4,1]
print ''
print depts[0,0],frams[0,0]
print depts[1,0],frams[1,0]
print depts[2,0],frams[2,0]
print depts[3,0],frams[3,0]
print ''
print files[0,1]
print files[1,1]
print files[2,1]
print files[3,1]
print ''
print depta[0,0],frama[0,0]
print depta[1,0],frama[1,0]
print depta[2,0],frama[2,0]
print depta[3,0],frama[3,0]
print ''
print filea[0,1]
print filea[1,1]
print filea[2,1]
print filea[3,1]

