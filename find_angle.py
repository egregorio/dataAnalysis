import numpy as np
import glob
import os
from find_frame_angle_functions import *

depth_path  = '/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/find_angle/fall_2021'
angle_path  = '/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/find_angle'
angle_files  = '/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/find_angle/*'
path_to_save     = '/Users/elizabeth/Box Sync/dataAnalysis/plots_paper/rough_draft/angle_lists'
name_files     = 'files_d_0.0'
name_frame     = 'frame_d_0.0'
name_depth     = 'depth_d_0.0'
name_angle     = 'angle_d_0.0'

search_for = 0.0

iterate_over_files(depth_path,angle_path,angle_files,path_to_save,name_files,name_frame,name_depth,name_angle,search_for)

