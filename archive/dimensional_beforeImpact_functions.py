import numpy as np
import glob
import os

def iterate_over_files(csv_path,directory_path,experiment_constants,save_path,save_name):
        # Create the empty lists to use for saving
        y_array = []; y_length = []
        # Create the empty lists to use for saving
        all_y_array = []; all_y_length = []

        # Import the constants for that directory
        constants = np.loadtxt(experiment_constants)
        fps = constants[0] # Frames Per Second
        ppm = constants[1] # Pixels Per Meter

        # Iterate over all the *.csv files in the directory
        for filename in glob.glob(csv_path):
                # Declare the current filename, a *.csv in the path
                current_file = os.path.join(directory_path,filename)
                # Load the current file into a numpy array
                trackingArray = np.loadtxt(current_file,delimiter=',',skiprows=0)
                # Call the function to dimensionalize the data, changes pixels to meters
                y_array, y_length = dimensionalize(trackingArray,fps,ppm)
                # Creates the list of all the position lists
                all_y_array.append(y_array)
                # Creates the list of all the length lists
                all_y_length.append(y_length)

        # Finds the maximum length of a list
        y_max_length = max(all_y_length)
        # Padds the shorter lists with zeros so they are all the same length
        padded_y = create_one(all_y_array, y_max_length)
        # Finds the average position at every time step
        means_y, y_stds = averageF( padded_y, y_max_length)

        # Converts the frames to seconds
        timeStamp = frames_to_sec(means_y,fps)

        # Creates and saves an array that has all the values in their own row
        save_array = zip(timeStamp, means_y, y_stds)

        please_save = os.path.join(save_path,save_name)
        np.savetxt(please_save,save_array)        

        print('done! :)')
        return

def dimensionalize(data_file,frames_per_second,pixels_per_m):
        y_list = []

        cutoff = 700 # The shortest height we care about
        height_of_impact = 900
        length = len(data_file) # Finds the length of the current data file

        for i in range(0,length): # Iterates over every row of the data file
                current_y = float(data_file[i,0]) # This rows y coordinate

                if current_y > 700: # Uses the y coordinates to find the range we care about
                        if current_y < 900: # Only heights between impact and hitting bumpers
                                y_list = np.append(y_list, ( current_y - height_of_impact) / pixels_per_m )
                i = i + 1

        # Finds the length of the lists created 
        length_y = len(y_list)

        # Returns the x and y coordinate litsts and their lengths
        return y_list, length_y

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





