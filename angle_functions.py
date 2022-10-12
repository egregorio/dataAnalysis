import numpy as np


def convertAngle(x_array,arm_length):
        shape = np.shape(x_array)
        num_trials = shape[0]
        num_rows   = shape[1]
        this_day_array = []
        for j in range(0,num_trials):
                this_trial_array = []
                for k in range(0,num_rows):
                        angle = np.arcsin(x_array[j,k] / arm_length) * (180 / np.pi) * -1
                        this_trial_array.append(angle)
                zero_value = this_trial_array[0]
                this_trial_array = this_trial_array - zero_value
                this_trial_array[0] = 0
                this_day_array.append(this_trial_array)

        return this_day_array

def find_the_frame(angle_list,search_for):
        closest_angle_list = []
        desired_frame = []

        shape = np.shape(angle_list)
        num_trials = shape[0] # trial number
        num_rows   = shape[1] # frame number

        for i in range(0,num_trials): # loop over trials
                diff_list  = []
                current_a_list = []
                for j in range(0,num_rows): # loop over frames
                        current_a = angle_list[i][j]
                        diff = abs( current_a - search_for )

                        diff_list.append(diff)
                        current_a_list.append(current_a)

                frame = diff_list.index(min(diff_list))
                angle  = current_a_list[frame]

                closest_angle_list.append(angle)
                desired_frame.append(frame)

        # Returns the lists
        return closest_angle_list, desired_frame

def search_for_a_bunch(angle_list,search_for_list):
        num_angles = len(search_for_list)
        all_angles = []
        all_frames = []
        for i in range(0,num_angles):
                this_angle = search_for_list[i]
                closest_angle_list, desired_frame = find_the_frame(angle_list,this_angle)
                all_angles.append(closest_angle_list)
                all_frames.append(desired_frame)
        return all_angles, all_frames


