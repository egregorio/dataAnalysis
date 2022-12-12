import numpy as np


#depths = [3.0, 3.05, 3.1, 3.15, 3.2, 3.25, 3.3, 3.35, 3.4, 3.45, 3.5, 3.55, 3.6, 3.65, 3.7, 3.75, 3.8, 3.85, 3.9, 3.95, 4.0 ]
#depths = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0]
depths = [1.25,1.75,2.25]
frame_list = []
depth_list = []

# for 6000 fps and 0.06 arm length
fps = 6000
arm = 0.06
vel = 2.5
# for 5000 fps and 0.07 arm length
#fps = 5000
#arm = 0.07
#vel = 3.0

for i in range(0,len(depths)):
#	search_for = depths[i]
	diff_list = []
	nonD_list = []
	for j in range(1,900): # loop over frames
		search_for = depths[i]
		nonD_deep = j * vel * ( 1 / arm )
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



