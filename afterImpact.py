import numpy as np
import glob
import os
from dimensional_functions import *

path_for_joining   = '/Users/elizabeth/Box Sync/dataAnalysis/08032022'
path_with_only_csv = '/Users/elizabeth/Box Sync/dataAnalysis/08032022/*.csv'
path_to_constants  = '/Users/elizabeth/Box Sync/dataAnalysis/experiment_constants/08032022_constants.txt'
path_to_save       = '/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData'
name_to_save       = '08032022_allData'

iterate_over_files(path_with_only_csv,path_for_joining,path_to_constants,path_to_save,name_to_save)

