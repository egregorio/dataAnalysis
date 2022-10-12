import numpy as np


depths = [ 0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0 ]
frame_list = []
depth_list = []

# for 6000 fps and 0.06 arm length
fps = 6000
arm = 0.06
# for 5000 fps and 0.07 arm length
#fps = 5000
#arm = 0.07

for i in range(0,len(depths)):
#	search_for = depths[i]
	diff_list = []
	nonD_list = []
	for j in range(1,500): # loop over frames
		search_for = depths[i]
		nonD_deep = j * 2.5 * ( 1 / arm )
		nonD_deep = nonD_deep / fps

		diff = abs( nonD_deep - search_for )

		diff_list.append(diff)
		nonD_list.append(nonD_deep)
		j = j + 1

	frame_number = diff_list.index(min(diff_list))
        frame_list.append(frame_number)
        depth_list.append(nonD_list[frame_number])

	i = i + 1


print(depths)
print(frame_list)
print(depth_list)



