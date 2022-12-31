import numpy as np

# Converts the frame number to the current time in seconds
def frames_to_sec(position_list):
    time_list = []
    length = len(position_list)
    frame_list = np.linspace(0,length,length)
    for i in range(0, length):
        current_time = frame_list[i] / 5000
        time_list.append(current_time)
    return time_list

# Converts distances from pixels to meters
def pixel_to_m(position_list,pixel_in):
    dimensional = []
    for i in range(0,len(position_list)):
        position_m = position_list[i] * ( 1 / pixel_in ) * ( 1 / 39.37 )
        dimensional.append(position_m)
    return dimensional

# Convert Standard Length from pixels to meters
def pixel_to_m_bodyLength(bodyLength,pixel_in):
    standardLength = bodyLength * ( 1 / pixel_in ) * ( 1 / 39.37 )
    return standardLength

# Converts distances from pixels to body lengths in pixels
def pixel_to_bl(position_list,pixel_bl):
    body_lengths = []
    for i in range(0,len(position_list)):
        position_b = position_list[i] / pixel_bl
        body_lengths.append(position_b)
    return body_lengths

# Converts dimensional time in seconds to non dimensional time t_bar
def frames_to_t_bar(position_list,velocity_m_s,bodyLength):
    t_bar = []
    length = len(position_list)
    frame_list = np.linspace(0,length,length)
    m_bl = pixel_to_m_bodyLength(bodyLength, 55.228133)
    for i in range(0, length):
        current_time = frame_list[i] / 5000
        current_t_bar = -1 * ( current_time * velocity_m_s ) / m_bl
        t_bar.append(current_t_bar)
    return t_bar

def get_linearFit(velocity,t_bar_list):
    velocityCurve = []
    for i in range(0,len(t_bar_list)):
        currentV = velocity * t_bar_list[i]
        velocityCurve.append(currentV)
    return velocityCurve

def beforePlateau(data_file,wherePlateau):
        a_list = []
        length = len(data_file) # Finds the length of the current data file

        for i in range(0,length): # Iterates over every row of the data file
                current_angle = float(data_file[i]) # This rows y coordinate

                if current_angle < wherePlateau: # Uses the y coordinates to find the range we care about
                        a_list = np.append( a_list, current_angle)
                i = i + 1

        # Finds the length of the lists created 
        length_a = len(a_list)

        # Returns the x and y coordinate lists and their lengths
        return a_list, length_a

def beforeMin(data_file,wherePlateau):
        a_list = []
        length = len(data_file) # Finds the length of the current data file

        for i in range(0,length): # Iterates over every row of the data file
                current_angle = float(data_file[i]) # This rows y coordinate

                if current_angle > wherePlateau: # Uses the y coordinates to find the range we care about
                        a_list = np.append( a_list, current_angle)
                i = i + 1

        # Finds the length of the lists created 
        length_a = len(a_list)

        # Returns the x and y coordinate lists and their lengths
        return a_list, length_a

def beforeBL1(data_file,nonD_time):
        t_list = []
        length = len(data_file) # Finds the length of the current data file

        for i in range(0,length): # Iterates over every row of the data file
                current_time = float(data_file[i]) # This rows y coordinate

                if current_time <= nonD_time: # Uses the y coordinates to find the range we care about
                        t_list = np.append( t_list, current_time)
                i = i + 1

        # Finds the length of the lists created 
        length_t = len(t_list)

        # Returns the x and y coordinate lists and their lengths
        return t_list, length_t








