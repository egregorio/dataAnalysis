import numpy as np

def get_t_bar(meanArray):
    t_bar_list = []
    length = len(meanArray)
    frame_list = np.linspace(0,length,length)
    for i in range(0, length):
        current_time = frame_list[i] / 5000
        # t_bar =       time * v / L
        t_bar = current_time * 2 / (( 135.601280856614  / 55.228133 ) * ( 1 / 39.37 ))
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

def get_linearFit(velocity,t_bar_list):
    velocityCurve = []
    for i in range(0,len(t_bar_list)):
        currentV = velocity * t_bar_list[i]
        velocityCurve.append(currentV)
    return velocityCurve

def get_velocity(velocity,t_bar_list):
    velocityCurve = []
    nonD_velocity = velocity * (( 135.601280856614  / ( 55.228133 * 39.37 )) / 2 ) 
    for i in range(0,len(t_bar_list)):
        currentV = nonD_velocity * t_bar_list[i]
        velocityCurve.append(currentV)
    return velocityCurve



