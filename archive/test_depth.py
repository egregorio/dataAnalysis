import numpy as np
import math


depths = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
frame_list = []
depth_list = []

diff_list = []
nonD_list = []

search_for = 1.0

for j in range(1,400): # loop over frames
#	search_for = depths[i]
	nonD_deep = j * 2.5 * ( 1 / 0.06)
	nonD_deep = nonD_deep / 6000

	diff = abs( nonD_deep - search_for )

	diff_list.append(diff)
	nonD_list.append(nonD_deep)
	print(nonD_deep)	
#	j = j + 1


#print(diff_list)
#print(nonD_list)



