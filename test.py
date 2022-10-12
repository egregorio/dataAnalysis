import numpy as np
import glob
import os
from dimensional_functions import *

path_for_joining   = '/Users/elizabeth/Box Sync/dataAnalysis/data_to_plot/08172022_asym_n2'
path_with_only_csv = '/Users/elizabeth/Box Sync/dataAnalysis/data_to_plot/08172022_asym_n2/*.csv'
path_to_constants  = '/Users/elizabeth/Box Sync/dataAnalysis/experiment_constants/08032022_constants.txt'
path_to_save       = '/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/for moment - fall 2021/dimensional data'
name_to_save       = '08172022_asym_n2_allData_X'
name_to_file       = '08172022_asym_n2_filesList'

iterate_over_files(path_with_only_csv,path_for_joining,path_to_constants,path_to_save,name_to_save,name_to_file)

