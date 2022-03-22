import numpy as np

def get_t_bar(meanArray,impactVelocity,lengthScale):
    t_bar_list = []
    length = len(meanArray)
    frame_list = np.linspace(0,length,length)
    for i in range(0, length):
        current_time = frame_list[i] / 5000
        t_bar = current_time * ( impactVelocity * lengthScale / 55.228133 )
        t_bar = t_bar * -1
        t_bar_list.append(t_bar)
    return t_bar_list

def get_time(meanArray):
    time_list = []
    length = len(meanArray)
    frame_list = np.linspace(0,length,length)
    for i in range(0, length):
        current_time = frame_list[i] / 5000
        time_list.append(current_time)
    return time_list






