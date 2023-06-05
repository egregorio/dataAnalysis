import numpy as np
import glob
import os

def iterate_over_files(csv_path,directory_path,experiment_constants,save_path,save_name,save_file):
        # Create the empty lists to use for saving
        x_array = []; y_array = []; x_length = []; y_length = []
        # Create the empty lists to use for saving
        all_x_array  = []; all_y_array  = []
        all_x_length = []; all_y_length = []

        first_index_list = [];
        file_name_list = [];
        # Import the constants for that directory
        constants = np.loadtxt(experiment_constants)
        fps = constants[0] # Frames Per Second
        ppm = constants[2] # Pixels Per Meter
        hoi = constants[3] # Height Of Impact
        xoi = constants[4] # X coordinate of Impact

        # Iterate over all the *.csv files in the directory
        for filename in glob.glob(csv_path):
                # Declare the current filename, a *.csv in the path
                current_file = os.path.join(directory_path,filename)
                # Load the current file into a numpy array
                trackingArray = np.loadtxt(current_file,delimiter=',',skiprows=0)
                # Call the function to dimensionalize the data, changes pixels to meters
                x_array, y_array, x_length, y_length, index = dimensionalize(trackingArray,fps,ppm,hoi,xoi)

                # Creates the list of all the position lists
                all_x_array.append(x_array)
                all_y_array.append(y_array)

                # Creates the list of all the length lists
                all_x_length.append(x_length)
                all_y_length.append(y_length)

                first_index_list.append(index[0])
                file_name_list.append(filename)

        # Finds the maximum length of a list
        x_max_length = max(all_x_length)
        y_max_length = max(all_y_length)

        # Padds the shorter lists with zeros so they are all the same length
        padded_x = create_one(all_x_array, x_max_length)
        padded_y = create_one(all_y_array, y_max_length)

        # Finds the average position at every time step
        means_x, x_stds = averageF( padded_x, x_max_length)
        means_y, y_stds = averageF( padded_y, y_max_length)

        # Converts the frames to seconds
        timeStamp = frames_to_sec(means_x,fps)

        # Creates and saves an array that has all the values in their own row
        save_array = zip(timeStamp, means_x, x_stds, means_y, y_stds)
#        save_array = padded_y
#        save_array = padded_x
#	save_array = first_index_list
        please_save = os.path.join(save_path,save_name)
        np.savetxt(please_save,save_array)        
	save_files = file_name_list
        please_save_file = os.path.join(save_path,save_file)
	np.savetxt(please_save_file,save_files,fmt="%s")

        print(len(means_y))
        print(first_index_list)
        print(file_name_list)

        print('done! :)')
        return

def dimensionalize(data_file,frames_per_second,pixels_per_m,height_of_impact,x_of_impact):
        x_list = []
        y_list = []
        index_list = []

        cutoff = 365 # The shortest height we care about

        length = len(data_file) # Finds the length of the current data file

        for i in range(0,length): # Iterates over every row of the data file
                current_x = float(data_file[i,1]) # This rows x coordinate # changed to get hip dot -- hinge dot
                current_y = float(data_file[i,0]) # This rows y coordinate

                if current_y > cutoff: # Uses the y coordinates to find the range we care about
                        if current_y < height_of_impact: # Only heights between impact and hitting bumpers
		                x_list = np.append(x_list, ( current_x - x_of_impact) / pixels_per_m )
        		        y_list = np.append(y_list, ( current_y - height_of_impact) / pixels_per_m )
                		index_list = np.append(index_list, i)
                i = i + 1

        # Finds the length of the lists created 
        length_x = len(x_list)
        length_y = len(y_list)

        # Returns the x and y coordinate litsts and their lengths
        return x_list, y_list, length_x, length_y, index_list

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

# This function finds the average x,y coordinate at every time
def averageF(all_samples, max_length):
    mean_list =[]
    stdv_list =[]
    for i in range(0, max_length):
        summ=[]
        for j in range(0, len(all_samples)):
            if all_samples[j][i]!=0:
                summ.append(all_samples[j][i])
        mean_at_specific_x = np.mean(summ)
        stdv_at_specific_x = np.std(summ)
        mean_list.append(mean_at_specific_x)
        stdv_list.append(stdv_at_specific_x)
    return mean_list,stdv_list

# This function converts the frame list to a time list
def frames_to_sec(position_list,frames_per_second):
    time_list = []
    length = len(position_list)
    frame_list = np.linspace(0,length,length)
    for i in range(0, length):
        current_time = frame_list[i] / frames_per_second
        time_list.append(current_time)
    return time_list





