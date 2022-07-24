import numpy as np
import glob
import os
from find_frame_functions import *

directory_path  = '/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/find_bl/fps_6000'
#directory_path  = '/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/find_bl/fps_5000'
directory_files  = '/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/find_bl/fps_6000/*'
#directory_files  = '/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/find_bl/fps_5000/*'
path_to_save     = '/Users/elizabeth/Box Sync/dataAnalysis/plots_paper/rough_draft/frame_lists'
name_to_save     = 'fall_bodylength_0_5'

search_for = 0.5

iterate_over_files(directory_path,directory_files,path_to_save,name_to_save,search_for)

