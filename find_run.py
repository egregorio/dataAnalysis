import numpy as np
import glob
import os
from find_frame_functions import *

directory_path  = '/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/\
find_bl/spring_2022'
directory_files  = '/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/\
find_bl/spring_2022/*'
path_to_save     = '/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/plots_paper/rough_draft/frame_lists'
name_files     = 'files_bl_0.0'
name_frame     = 'frame_bl_0.0'
name_depth     = 'depth_bl_0.0'

search_for = 0.0

iterate_over_files(directory_path,directory_files,path_to_save,name_files,name_frame,name_depth,search_for)

