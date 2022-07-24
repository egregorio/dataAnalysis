import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import scipy
import os

# Path to Data Files
save_path = '/Users/elizabeth/Box Sync/dataAnalysis/plots_paper/rough_draft/frame_lists'

# Names of Data Files
name_frame     = 'frame_bl_1.5'
name_depth     = 'depth_bl_1.5'

# Join Paths
depth_path = os.path.join(save_path,name_depth)
frame_path = os.path.join(save_path,name_frame)

# Load Text as Arrays
depth = np.loadtxt(depth_path)
frame = np.loadtxt(frame_path)

print(np.shape(depth),np.shape(frame))

import pandas as pd
table = [[1, 2222, 30, 500], [4, 55, 6777, 1]]
df = pd.DataFrame(table, columns = ['a', 'b', 'c', 'd'], index=['row_1', 'row_2'])
print(df)
