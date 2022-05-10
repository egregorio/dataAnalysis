import numpy as np
import glob
import os
from dimensional_functions import *

path_for_joining   = '/Users/elizabeth/Box Sync/dataAnalysis/data_to_plot/09182021'
path_with_only_csv = '/Users/elizabeth/Box Sync/dataAnalysis/data_to_plot/09182021/*.csv'
path_to_constants  = '/Users/elizabeth/Box Sync/dataAnalysis/experiment_constants/9182021_constants.txt'
path_to_save       = '/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData'
name_to_save       = '9182021_data'

iterate_over_files(path_with_only_csv,path_for_joining,path_to_constants,path_to_save,name_to_save)

