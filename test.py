import numpy as np
import glob
import os
from dimensional_functions import *

path_for_joining   = '/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/data_to_plot/\
09212021'
path_with_only_csv = '/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/data_to_plot/\
09212021/*.csv'
path_to_constants  = '/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/experiment_constants/\
9212021_constants.txt'
path_to_save       = '/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData'
name_to_save       = \
'09212021_indexList'
name_to_file       = \
'09212021_filesList'

iterate_over_files(path_with_only_csv,path_for_joining,path_to_constants,path_to_save,name_to_save,name_to_file)

