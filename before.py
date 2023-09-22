import numpy as np
import glob
import os
from before_impact import *

path_for_joining   = '/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/data_to_plot/\
08172022'
path_with_only_csv = '/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/data_to_plot/\
08172022/*.csv'
path_to_constants  = '/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/experiment_constants/\
08172022_constants.txt'
path_to_save       = '/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData'
name_to_save       = \
'08172022_before'
name_to_file       = \
'08172022_filesList'
name_of_index      = '/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/dataAnalysis/dimensionalData/index_lists/'\
'08172022_indexList'

iterate_over_files(path_with_only_csv,path_for_joining,path_to_constants,path_to_save,name_to_save,name_to_file,name_of_index)

