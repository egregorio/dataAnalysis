import numpy as np
import glob
import os

# Path to Data Files
files = '/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/index_lists/*'
path = '/Users/elizabeth/Box Sync/dataAnalysis/dimensionalData/index_lists/'

for filename in glob.glob(files):
	use_this = os.path.join(path,filename)
	index_list = np.loadtxt(use_this)
	print index_list[0]
	print filename

