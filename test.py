import numpy as np
import glob
import os
from dimensional_functions import *

path_for_joining   = '/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/data_to_plot/\
10262021'
path_with_only_csv = '/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/data_to_plot/\
10262021/*.csv'
path_to_constants  = '/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/experiment_constants/\
10262021_constants.txt'
path_to_save       = '/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData'
name_to_save       = \
'10262021_hips'
name_to_file       = \
'10262021_filesList'

iterate_over_files(path_with_only_csv,path_for_joining,path_to_constants,path_to_save,name_to_save,name_to_file)

