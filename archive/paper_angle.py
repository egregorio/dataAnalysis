import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import glob
import os
from angle_functions import *

# Path to dimensional data
dimensional_path = '/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/angle_analysis/angle_info/x_data'
save_path = '/Users/elizabeth/Box Sync/air cavity analysis/paper_cavity_visualization/angle_analysis/angle_info'

data_918    = np.loadtxt(os.path.join(dimensional_path,'09182021_allData_X'))
data_920    = np.loadtxt(os.path.join(dimensional_path,'09202021_allData_X'))
data_921    = np.loadtxt(os.path.join(dimensional_path,'09212021_allData_X'))
data_1021   = np.loadtxt(os.path.join(dimensional_path,'10212021_allData_X'))
data_1026   = np.loadtxt(os.path.join(dimensional_path,'10262021_allData_X'))
data_817_n1 = np.loadtxt(os.path.join(dimensional_path,'08172022_n1_allData_X'))
data_817_n2 = np.loadtxt(os.path.join(dimensional_path,'08172022_n2_allData_X'))

save_a_918    = os.path.join(save_path,'09182021_angles');    save_f_918    = os.path.join(save_path,'09182021_frameList');    save_aa_918    = os.path.join(save_path,'09182021_a_atFrame')
save_a_920    = os.path.join(save_path,'09202021_angles');    save_f_920    = os.path.join(save_path,'09202021_frameList');    save_aa_920    = os.path.join(save_path,'09202021_a_atFrame')
save_a_921    = os.path.join(save_path,'09212021_angles');    save_f_921    = os.path.join(save_path,'09212021_frameList');    save_aa_921    = os.path.join(save_path,'09212021_a_atFrame')
save_a_1021   = os.path.join(save_path,'10212021_angles');    save_f_1021   = os.path.join(save_path,'10212021_frameList');    save_aa_1021   = os.path.join(save_path,'10212021_a_atFrame')
save_a_1026   = os.path.join(save_path,'10262021_angles');    save_f_1026   = os.path.join(save_path,'10262021_frameList');    save_aa_1026   = os.path.join(save_path,'10262021_a_atFrame')
save_a_817_n1 = os.path.join(save_path,'08172022_n1_angles'); save_f_817_n1 = os.path.join(save_path,'08172022_n1_frameList'); save_aa_817_n1 = os.path.join(save_path,'08172022_n1_a_atFrame')
save_a_817_n2 = os.path.join(save_path,'08172022_n2_angles'); save_f_817_n2 = os.path.join(save_path,'08172022_n2_frameList'); save_aa_817_n2 = os.path.join(save_path,'08172022_n2_a_atFrame')

num_day = 7

# Import and assign constants
exp_const = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/experiment_constants/constants.txt')
mass_diver = exp_const[0]
fall_bl    = exp_const[1]
spring_bl  = exp_const[2]
impact_v   = exp_const[3]

search_for = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

angle_918    = convertAngle(data_918,fall_bl)
angle_920    = convertAngle(data_920,fall_bl)
angle_921    = convertAngle(data_921,fall_bl)
angle_1021   = convertAngle(data_1021,fall_bl)
angle_1026   = convertAngle(data_1026,fall_bl)
angle_817_n1 = convertAngle(data_817_n1,fall_bl)
angle_817_n2 = convertAngle(data_817_n2,fall_bl)

all_angles_918,    all_frames_918    = search_for_a_bunch(angle_918, search_for)
all_angles_920,    all_frames_920    = search_for_a_bunch(angle_920, search_for)
all_angles_921,    all_frames_921    = search_for_a_bunch(angle_921, search_for)
all_angles_1021,   all_frames_1021   = search_for_a_bunch(angle_1021, search_for)
all_angles_1026,   all_frames_1026   = search_for_a_bunch(angle_1026, search_for)
all_angles_817_n1, all_frames_817_n1 = search_for_a_bunch(angle_817_n1, search_for)
all_angles_817_n2, all_frames_817_n2 = search_for_a_bunch(angle_817_n2, search_for)

np.savetxt(    save_a_918,    angle_918); np.savetxt(    save_f_918,    all_frames_918); np.savetxt(    save_aa_918,    all_angles_918)
np.savetxt(    save_a_920,    angle_920); np.savetxt(    save_f_920,    all_frames_920); np.savetxt(    save_aa_920,    all_angles_920)
np.savetxt(    save_a_921,    angle_921); np.savetxt(    save_f_921,    all_frames_921); np.savetxt(    save_aa_921,    all_angles_921)
np.savetxt(   save_a_1021,   angle_1021); np.savetxt(   save_f_1021,   all_frames_1021); np.savetxt(   save_aa_1021,   all_angles_1021)
np.savetxt(   save_a_1026,   angle_1026); np.savetxt(   save_f_1026,   all_frames_1026); np.savetxt(   save_aa_1026,   all_angles_1026)
np.savetxt( save_a_817_n1, angle_817_n1); np.savetxt( save_f_817_n1, all_frames_817_n1); np.savetxt( save_aa_817_n1, all_angles_817_n1)
np.savetxt( save_a_817_n2, angle_817_n2); np.savetxt( save_f_817_n2, all_frames_817_n2); np.savetxt( save_aa_817_n2, all_angles_817_n2)

print(';)')
