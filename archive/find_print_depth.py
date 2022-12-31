import numpy as np
import os

# Path to Data Files
save_path = '/Users/elizabeth/Box Sync/dataAnalysis/plots_paper/rough_draft/frame_lists/spring_2022'

# Names of Data Files
name_frame     = 'frame_bl_2.0'
name_depth     = 'depth_bl_2.0'

# Join Paths
depth_path = os.path.join(save_path,name_depth)
frame_path = os.path.join(save_path,name_frame)

# Load Text as Arrays
depth = np.loadtxt(depth_path)
frame = np.loadtxt(frame_path)

print(np.shape(depth),np.shape(frame))

print depth[0,0],frame[0,0]
print depth[1,0],frame[1,0]
print depth[2,0],frame[2,0]
print depth[3,0],frame[3,0]
print depth[4,0],frame[4,0]

