import numpy as np
import os

# Path to Data Files
save_path = '/Users/elizabeth/Box Sync/dataAnalysis/plots_paper/rough_draft/angle_lists'

# Names of Data Files
name_frame     = 'frame_d_0.0'
name_depth     = 'depth_d_0.0'
name_angle     = 'angle_d_0.0'

# Join Paths
angle_path = os.path.join(save_path,name_angle)
depth_path = os.path.join(save_path,name_depth)
frame_path = os.path.join(save_path,name_frame)

# Load Text as Arrays
angle = np.loadtxt(angle_path)
depth = np.loadtxt(depth_path)
frame = np.loadtxt(frame_path)

print(np.shape(depth),np.shape(frame))

print angle[0,0],depth[0,0],frame[0,0]
print angle[1,0],depth[1,0],frame[1,0]
print angle[2,0],depth[2,0],frame[2,0]
print angle[3,0],depth[3,0],frame[3,0]
print angle[4,0],depth[4,0],frame[4,0]

