import numpy as np
import glob
import os

def iterate_over_files(csv_path,directory_path,experiment_constants,save_path,save_name):
        # Create the empty lists to use for saving
        x_array = []; y_array = []; x_length = []; y_length = []
        # Create the empty lists to use for saving
        all_x_array  = []; all_y_array  = []
        all_x_length = []; all_y_length = []

        # Import the constants for that directory
        constants = np.loadtxt(experiment_constants)
        fps = constants[0] # Frames Per Second
        ppm = constants[1] # Pixels Per Meter
        hoi = constants[2] # Height Of Impact
        xoi = constants[3] # X coordinate of Impact

        for filename in glob.glob(csv_path):
                current_file = os.path.join(directory_path,filename)
                trackingArray = np.loadtxt(current_file,delimiter=',',skiprows=0)
                x_array, y_array, x_length, y_length = dimensionalize(trackingArray,fps,ppm,hoi,xoi)

                all_x_array.append(x_array)
                all_y_array.append(y_array)

                all_x_length.append(x_length)
                all_y_length.append(y_length)

        x_max_length = max(all_x_length)
        y_max_length = max(all_y_length)

        padded_x = create_one(all_x_array, x_max_length)
        padded_y = create_one(all_y_array, y_max_length)

        means_x, x_stds = averageF( padded_x, x_max_length)
        means_y, y_stds = averageF( padded_y, y_max_length)

        timeStamp = frames_to_sec(means_x)

        save_array = zip(timeStamp, means_x, x_stds, means_y, y_stds)
        please_save = os.path.join(save_path,save_name)
        np.savetxt(please_save,save_array)        

        print('done! :)')
        return

def dimensionalize(data_file,frames_per_second,pixels_per_m,height_of_impact,x_of_impact):
        x_list = []
        y_list = []

        cutoff = 250

        length = len(data_file)

        for i in range(0,length):
                current_x = float(data_file[i,1])
                current_y = float(data_file[i,0])

                if current_y > cutoff:
                        if current_y < height_of_impact:
                                x_list = np.append(x_list, (current_x - x_of_impact) / pixels_per_m)
                                y_list = np.append(y_list, (current_y - height_of_impact) / pixels_per_m )
                        
                i = i + 1
        
        length_x = len(x_list)
        length_y = len(y_list)

        return x_list, y_list, length_x, length_y

def padding(sample, max_length):
    if len(sample)<max_length:
        zero_ar = [0]*(max_length-len(sample))
        sample = np.append(sample,zero_ar)
    return sample

def create_one(input_ar, max_length):
    for i in range(0, len(input_ar)):
        input_ar[i] = padding(input_ar[i], max_length)
    return input_ar

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

def frames_to_sec(position_list):
    time_list = []
    length = len(position_list)
    frame_list = np.linspace(0,length,length)
    for i in range(0, length):
        current_time = frame_list[i] / 5000
        time_list.append(current_time)
    return time_list





