# This routine was written to check if all of the pixel to meter measurements were
# negligably different between different experimental trials.

import numpy as np
import glob
import os
from dimensional_functions import *

path_to_constants = '/Users/elizabeth/Box Sync/dataAnalysis/experiment_constants/'
path_to_txt       = '/Users/elizabeth/Box Sync/dataAnalysis/experiment_constants/*.txt'

ppm_list = []

for filename in glob.glob(path_to_txt):
       # Declare the current filename, a *.csv in the path
       current_file = os.path.join(path_to_constants,filename)
       experiment_constants = np.loadtxt(current_file)
       constants = np.loadtxt(experiment_constants)
       ppm = constants[1] # Pixels Per Meter
       ppm_list.append(ppm)

number = len(ppm_list)
sum_all = sum(ppm_list)
average = sum_all / number

print('average = ',average)

stdv = np.sqrt(((ppm_list[0] - average)**2 + (ppm_list[1] - average)**2 + \
                (ppm_list[2] - average)**2 + (ppm_list[3] - average)**2 + \
                (ppm_list[4] - average)**2 + (ppm_list[5] - average)**2 ) / number )

print('stdv = ',stdv)




