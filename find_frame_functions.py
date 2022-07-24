import numpy as np
import glob
import os

def iterate_over_files(directory_path,directory_files,save_path,save_name,search_for):
	print('starting')

        # Create the empty lists to use for saving
        working_array = [];
        # Create the empty lists to use for saving
	depth_list = [];
	frame_list = [];
	file_list = [];
	index_list = [];
	trial_list = [];

	print('empty lists')
	# Constant
	constants = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/experiment_constants/constants.txt')
	body_length = constants[1] # fall 2021
#	body_length = constants[2] # spring 2022
	imp_vel = constants[3]
	fps = constants[4] # 6000fps, fall 2021 fps
#	fps = constants[5] # 5000fps, spring 2022 fps

	print('constants')
        # Iterate over all the *.csv files in the directory
        for filename in glob.glob(directory_files):
		print('working on it!')
                # Declare the current filename, a *.csv in the path
                current_file = os.path.join(directory_path,filename)
		print('loaded file')
                # Load the current file into a numpy array
                trackingArray = np.loadtxt(current_file)#,delimiter=',',skiprows=0)
		print('loaded array')
                # Call the function to dimensionalize the data, changes pixels to meters
                depth, frame, trials = find_the_frame(trackingArray,search_for,body_length,fps,imp_vel)

                # Creates the list of all the parameters
		depth_list.append(depth)
		frame_list.append(frame)
		trial_list.append(trials)
                file_list.append(filename)

	max_trial = max(trial_list)
        depth_array = create_one(depth_list, max_trial)
        frame_array = create_one(frame_list, max_trial)

	print(np.shape(depth_array),np.shape(frame_array))
	print(depth_list)
	print(frame_list)

        # Creates and saves an array that has all the values in their own row
#        save_array = zip(depth_array, frame_array)#, file_list)
#	save_array = height_array
#        please_save = os.path.join(save_path,save_name)
#        np.savetxt(please_save,save_array)        

        print('done! :)')
        return

def find_the_frame(data_file,search_for,body_length,fps,imp_vel):
	desired_depth = []
	desired_frame = []
	depth = []
	frame = []

	search_for = search_for
	
	shape = np.shape(data_file)
	rows = shape[0] # trial number
	colm = shape[1] # frame number

        for i in range(0,rows): # loop over trials
		for j in range(0,colm): # loop over frames
        	        current_f = j + 1 # This rows y coordinate
			current_t = current_f / fps
			nonD_time = current_t * imp_vel / body_length
	                current_h = float(data_file[i,j])
	                nonD_deep = current_h / body_length

                        if current_h % body_length <= 5:
                		depth.append(nonD_deep)
				frame.append(current_f)
			j = j + 1

		desired_depth.append(depth[-1])
		desired_frame.append(frame[-1])

		i = i + 1

        # Returns the lists
        return desired_depth, desired_frame, rows

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


