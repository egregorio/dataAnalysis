import numpy as np
import glob
import os
from dimensional_functions import *

path_for_joining   = '/Users/elizabeth/Box Sync/dataAnalysis/data_to_plot/04042022'
path_with_only_csv = '/Users/elizabeth/Box Sync/dataAnalysis/data_to_plot/04042022/*.csv'
path_to_constants  = '/Users/elizabeth/Box Sync/dataAnalysis/experiment_constants/04042022_constants.txt'
path_to_save       = '/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData'
name_to_save       = '04042022_allData_X'
name_to_file       = '04042022_filesList'

iterate_over_files(path_with_only_csv,path_for_joining,path_to_constants,path_to_save,name_to_save,name_to_file)

