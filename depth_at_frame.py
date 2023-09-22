import numpy as np


#depths = [ 3.3, 3.35, 3.4, 3.45, 3.5, 3.55, 3.6, 3.65, 3.7, 3.75, 3.8, 3.85, 3.9]#, 3.95, 4.0 ]
depths = [0.1, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6]
#depths = [3, 3.05, 3.1, 3.15, 3.2, 3.25, 3.3, 3.35, 3.4, 3.45, 3.5, 3.55, 3.6, 3.65, 3.7, 3.75, 3.8, 3.85, 3.9, 3.95,
#	  4, 4.05, 4.1, 4.15, 4.2, 4.25, 4.3, 4.35, 4.4, 4.45, 4.5, 4.55, 4.6, 4.65, 4.7, 4.75, 4.8, 4.85, 4.9, 4.95,
#	  5, 5.05, 5.1, 5.15, 5.2, 5.25, 5.3, 5.35, 5.4, 5.45, 5.5, 5.55, 5.6, 5.65, 5.7, 5.75, 5.8, 5.85, 5.9, 5.95,
#	  6, 6.05, 6.1, 6.15, 6.2, 6.25, 6.3, 6.35, 6.4, 6.45, 6.5, 6.55, 6.6, 6.65, 6.7, 6.75, 6.8, 6.85, 6.9, 6.95, 7]
#depths = [1.25,1.75,2.25]
#depths = [1.5,2]
#depths = [0,1,2,3]
frame_list = []
depth_list = []

# for 6000 fps and 0.06 arm length
#fps = 6000
#arm = 0.0744#6
#vel = 3.1#2.5
# for 5000 fps and 0.07 arm length
#fps = 5000
#arm = 0.07
#vel = 3.0
fps = 5150
arm = 0.0744#6
#arm = 0.072#6
vel = 3.1#2.5

for i in range(0,len(depths)):
#	search_for = depths[i]
	diff_list = []
	nonD_list = []
	time_list = []
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


