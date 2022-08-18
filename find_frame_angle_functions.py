import numpy as np
import glob
import os

def iterate_over_files(depth_path,angle_path,angle_files,save_path,save_files,save_frame,save_depth,save_angle,search_for):

        # Create the empty lists to use for saving
        working_array = [];
        # Create the empty lists to use for saving
	angle_list = [];
	depth_list = [];
	frame_list = [];
	file_list = [];
	index_list = [];
	trial_list = [];

	# Constant
	constants = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/experiment_constants/constants.txt')
#	body_length = constants[1] # fall 2021
	body_length = constants[2] # spring 2022
	imp_vel = constants[3]

        # Iterate over all the *.csv files in the directory
        for filename in glob.glob(angle_files):
                # Declare the current filename, a *.csv in the path
                find_angle_file = os.path.join(angle_path,filename)
                find_depth_file = os.path.join(depth_path,filename)
                # Load the current file into a numpy array
                angleArray = np.loadtxt(find_angle_file)
                depthArray = np.loadtxt(find_depth_file)
                # Call the function to dimensionalize the data, changes pixels to meters
                angle, depth, frame, trials = find_the_frame(angleArray,depthArray,search_for,body_length)

                # Creates the list of all the parameters
		angle_list.append(angle)
		depth_list.append(depth)
		frame_list.append(frame)
		trial_list.append(trials)
                file_list.append(filename)

	max_trial = max(trial_list)
        angle_array = create_one(angle_list, max_trial)
        depth_array = create_one(depth_list, max_trial)
        frame_array = create_one(frame_list, max_trial)

        # Creates and saves an array that has all the values in their own row
#        save_array = zip(depth_array, frame_array)#, file_list)
        please_files = os.path.join(save_path,save_files)
        please_frame = os.path.join(save_path,save_frame)
        please_depth = os.path.join(save_path,save_depth)
        please_angle = os.path.join(save_path,save_angle)
        np.savetxt(please_files,file_list,fmt="%s")
        np.savetxt(please_frame,frame_array)
        np.savetxt(please_depth,depth_array)
        np.savetxt(please_angle,angle_array)

        print('done! :)')
        return

def find_the_frame(angle_file,depth_file,search_for,body_length):
	desired_angle = []
	desired_depth = []
	desired_frame = []

	shape = np.shape(angle_file)
	rows = shape[0] # trial number
	colm = shape[1] # frame number

        for i in range(0,rows): # loop over trials
		diff_list = []
		deep_list = []
		angl_list = []

		for j in range(0,colm): # loop over frames
	                current_x = float(angle_file[i,j]) / body_length
			current_x = current_x - float(angle_file[i,0])
			if j == 0:
				current_x = 0
			current_a = np.arcsin(current_x) * (180 / np.pi) * -1
			current_h = float(depth_file[i,j])
	                nonD_deep = current_h / body_length

			diff = abs( current_a - search_for )

                	diff_list.append(diff) 
			deep_list.append(nonD_deep)
			angl_list.append(current_a)

			j = j + 1

		frame = diff_list.index(min(diff_list))
		depth = deep_list[frame]
		angle = angl_list[frame]

		desired_angle.append(angle)
		desired_depth.append(depth)
		desired_frame.append(frame)
		
		i = i + 1

        # Returns the lists
        return desired_angle, desired_depth, desired_frame, rows

# This function padds the arrays with zeros so they're all the same length
def padding(sample, max_length):
    if len(sample)<max_length:
        zero_ar = [0]*(max_length-len(sample))
        sample = np.append(sample,zero_ar)
    return sample

# This function combines all the padded arrays into one array
def create_one(input_ar, max_length):
    for i in range(0, len(input_ar)):
        input_ar[i] = padding(input_ar[i], max_length)
    return input_ar


