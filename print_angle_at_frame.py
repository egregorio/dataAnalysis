import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import glob
import os

directory_path = '/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/angle_analysis/angle_info/angle_lists'
angle_directory = 'angle_at_frame_list'
frame_directory = 'frame_list' 
csv_path = '/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/angle_analysis/angle_info/angle_lists/angle_at_every_frame/*' 

filename_918 = '09182021'; filename_920 = '09202021'; filename_921 = '09212021'; filename_1021 = '10212021'
filename_1026 = '10262021'; filename_817_a1 = '08172022_n1'; filename_817_a2 = '08172022_n2';

filenames = [filename_918, filename_920, filename_921, filename_1021, filename_1026, filename_817_a1, filename_817_a2]
video_num = [26, 14, 1, 9, 9, 9, 19]


for i in range(0,len(filenames)):
	angle_name = filenames[i] + '_a_atFrame'
	frame_name = filenames[i] + '_frameList'
	angle_path = os.path.join(directory_path,angle_directory,angle_name)
	frame_path = os.path.join(directory_path,frame_directory,frame_name)
	angle_file = np.loadtxt(angle_path)
	frame_file = np.loadtxt(frame_path)

	angle_list = []
	frame_list = []
	for j in range(0,13):
		vid_num = video_num[i] - 1
		
		angle_list.append(angle_file[j,i])
		frame_list.append(frame_file[j,i])

	print(filenames[i])
	print(angle_list)
	print(frame_list)








""" # for future where I want all of them :)
file_list = []
all_angle_list = []
loop_frame = len(frame_list)
for filename in glob.glob(csv_path):
	current_file = os.path.join(directory_path,filename)
	angle_file = np.loadtxt(current_file)
	shape = np.shape(angle_file)
	loop_trials = shape[0]
#	file_list.append(filename)
	print(filename)
	angle_list = []
	for j in range(0,loop_trials):
		for i in range(0,loop_frame):
			current_a = angle_file[j,frame_list[i]]
			angle_list.append(current_a)
		print(angle_list)
#	all_angle_list.append(angle_list)
"""



