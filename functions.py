import numpy as np


def getArmsJuly(trackingArray):
        x_list = []
        y_list = []

        length = len(trackingArray[:,:1])

        for i in range(0,length):
                current_y = float(trackingArray[i,1])# / 251.7792923
                current_x = float(trackingArray[i,0])# / 251.7792923

                if current_x > 327.3131:
                        if current_x < 625:
                                y_list = np.append(y_list, (current_y / 251.7792923)-0.66511158649)
                                x_list = np.append(x_list, (current_x / 251.7792923)-2.47695700123)

                i = i + 1

        length_x = len(x_list)
        length_y = len(y_list)

        return x_list, y_list, length_x, length_y

def getArms920(trackingArray):
        x_list = []
        y_list = []

        length = len(trackingArray[:,:1])

        for i in range(0,length):
                current_y = float(trackingArray[i,1])# / 251.7792923
                current_x = float(trackingArray[i,0])# / 251.7792923

                if current_x > 250.0:
                        if current_x < 629.4482:
                                y_list = np.append(y_list, (current_y / 251.7792923)-0.75)
                                x_list = np.append(x_list, (current_x / 251.7792923)-2.5)

                i = i + 1

        length_x = len(x_list)
        length_y = len(y_list)

        return x_list, y_list, length_x, length_y

def getArms918(trackingArray):
        x_list = []
        y_list = []

        length = len(trackingArray[:,:1])

        for i in range(0,length):
                current_y = float(trackingArray[i,1])# / 251.7792923
                current_x = float(trackingArray[i,0])# / 251.7792923

                if current_x > 250.0:
                        if current_x < 634.4838:
                                y_list = np.append(y_list, (current_y / 251.7792923)-0.75691482365)
                                x_list = np.append(x_list, (current_x / 251.7792923)-2.51738071804)

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

