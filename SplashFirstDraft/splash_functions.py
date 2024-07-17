# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import os
import glob

def splashAnalysis(experiment):
	# Name the files you want to import
	P = '/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Summer-2023-Diver-Experiments/';
	R = 'raw_data/';
	J = 'jet_data/';
	D = experiment;
	T = '/Tracking';
	A = 'analysis/';
	F = '/files.txt';

	# Put together the file names
	vel = glob.glob(P + R + D + T + "/*.csv")
	jet = glob.glob(P + J + D + T + "/*.csv")

	vfiles = glob.glob(P + R + D + T + '/' + F)
	jfiles = glob.glob(P + J + D + T + '/' + F)
	vel_files = np.loadtxt(vfiles[0],dtype='str')
	jet_files = np.loadtxt(jfiles[0],dtype='str')

	vel_path = glob.glob(P + R + D + T + '/')
	jet_path = glob.glob(P + J + D + T + '/')

	# Initialize empty lists for constants
	waterlines = []; ppm_air = []; ppm_water = []; impact_time = []

	# Find the constants (water level and pixels per meter in air and water) for this file
	waterlines, ppm_air, ppm_water, impact_time = findConstants(vel, vel_path, vel_files)

	# Find the impact velocity
	impact1, impact2, entry1, entry2, entry3, entry4, len_impact1, len_impact2, len_entry1, len_entry2 = \
		findImpactVelocity(vel, vel_path, vel_files, ppm_air, ppm_water, impact_time, waterlines)

	# Find the depth of pinch off and splash height
	pinch1, pinch2, splash, splash_time, pinch_time, len_pinch1, len_pinch2, len_splash = \
		findSplash(jet, jet_path, jet_files, waterlines, ppm_air, ppm_water)

	# Save a file that lists: file name, impact velocity, pinch off depth 1 & 2, splash height
	scalar_array = zip(impact1, impact2, entry1, entry2, entry3, entry4, pinch1, pinch2, pinch_time, splash, splash_time)
	scalar_path  = os.path.join( P, A, D + '_scalars.csv' )
	with open(scalar_path, 'w', newline='') as f:
		writer = csv.writer(f)#, fieldnames=scalar_header)
		writer.writerows(scalar_array)

	#print(impact1)
	#print(entry1)

	# Create empty arrays that will hold the velocity profiles
	impact1_vel, impact2_vel, entry1_vel, entry2_vel, impact1_t, impact2_t, entry1_t, entry2_t,\
                pinch1_vel, pinch2_vel, pinch1_t, pinch2_t, splash_vel, splash_pos, splash_t = \
		createEmptyArrays(len_impact1, len_impact2, len_entry1, len_entry2, len_pinch1, \
			len_pinch2, len_splash)

	# Find the impact and entry velocity profiles
	findEntryVelocityArrays(vel, vel_path, vel_files, waterlines, ppm_air, ppm_water, impact_time, impact1_vel, impact2_vel, \
		entry1_vel, entry2_vel, impact1_t, impact2_t, entry1_t, entry2_t)

	# Save each to their own file
	impact1_array = np.array(impact1_vel)
	impact1_path = os.path.join(P, A, D + '_impact1.csv' )
	with open(impact1_path, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(impact1_array)
	impact1_time = np.array(impact1_t)
	impact1_path = os.path.join(P, A, D + '_impact1_time.csv' )
	with open(impact1_path, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(impact1_time)
	impact2_array = np.array(impact2_vel)
	impact2_path = os.path.join(P, A, D + '_impact2.csv' )
	with open(impact2_path, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(impact2_array)
	impact2_array = np.array(impact2_t)
	impact2_path = os.path.join(P, A, D + '_impact2_time.csv' )
	with open(impact2_path, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(impact2_array)

	entry1_array = np.array(entry1_vel)
	entry1_path  = os.path.join(P, A, D + '_entry1.csv' )
	with open(entry1_path, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(entry1_array)
	entry1_array = np.array(entry1_t)
	entry1_path  = os.path.join(P, A, D + '_entry1_time.csv' )
	with open(entry1_path, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(entry1_array)
	entry2_array = np.array(entry2_vel)
	entry2_path  = os.path.join(P, A, D + '_entry2.csv' )
	with open(entry2_path, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(entry2_array)
	entry2_array = np.array(entry2_t)
	entry2_path  = os.path.join(P, A, D + '_entry2_time.csv' )
	with open(entry2_path, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(entry2_array)


	# Find the pinch off and splash velocity profiles
	findSplashVelocityArrays(jet, jet_path, jet_files, waterlines, ppm_air, ppm_water, impact_time, pinch_time, pinch1_vel, pinch2_vel, \
		 pinch1_t, pinch2_t, splash_vel, splash_pos, splash_t)

	# Save each to their own file
	pinch1_array = np.array(pinch1_vel)
	pinch1_path = os.path.join(P, A, D + '_pinch1.csv' )
	with open(pinch1_path, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(pinch1_array)
	pinch1_array = np.array(pinch1_t)
	pinch1_path = os.path.join(P, A, D + '_pinch1_time.csv' )
	with open(pinch1_path, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(pinch1_array)
	pinch2_array = np.array(pinch2_vel)
	pinch2_path = os.path.join(P, A, D + '_pinch2.csv' )
	with open(pinch2_path, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(pinch2_array)
	pinch2_array = np.array(pinch2_t)
	pinch2_path = os.path.join(P, A, D + '_pinch2_time.csv' )
	with open(pinch2_path, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(pinch2_array)

	splash_array = np.array(splash_vel)
	splash_path = os.path.join(P, A, D + '_splash.csv' )
	with open(splash_path, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(splash_array)
	splash_array = np.array(splash_pos)
	splash_path = os.path.join(P, A, D + '_splash_pos.csv' )
	with open(splash_path, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(splash_array)
	splash_array = np.array(splash_t)
	splash_path = os.path.join(P, A, D + '_splash_time.csv' )
	with open(splash_path, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(splash_array)

	print( experiment, ' done! :)')
	return


def findConstants(velocity_file, vel_path, vel_file_names):
	# Initialize empty lists for constants
	all_waterlines = []
	all_ppm_air = []
	all_ppm_water = []
	all_impact_time = []

	# Loop through all vel files to find constants
	for i in range(0,len(velocity_file)):
		currentFile = glob.glob(vel_path[0] + vel_file_names[i] + ".csv")
		# Load file as a numpy array
		vel0 = np.loadtxt(currentFile[0],delimiter=',',skiprows=0)

		# Initialize empty lists
		impact1 = []; impact2 = [];
		impact1_time = []; impact2_time = []
		ppm1 = []; ppm2 = []
    
		# Loop to find waterline
		for j in range(0,len(vel0)):
			if vel0[j][0] != 0:
				impact1.append(vel0[j][0])
				impact1_time.append(i)
			if vel0[j][2] != 0:
				impact2.append(vel0[j][2])
				impact2_time.append(i)
    
		# Loop for ppm conversions
		for j in range(0,len(vel0)):
			if vel0[j][5] != 0:
#				ppm1.append(vel0[j][5])
				ppm1.append(j)
			if vel0[j][7] != 0:
#				ppm2.append(vel0[j][7])
				ppm2.append(j)

		# Calculate where the waterline is and what the 
		# pixel per meter is in the air and in water
		waterline = (impact1[-1] + impact2[-1]) / 2
		air_index = max(ppm1[0],ppm2[0]); water_index = min(ppm1[-1],ppm2[-1])
		ppm_air   = abs( vel0[air_index][5]   - vel0[air_index][7] ) * 39.4
		ppm_water = abs( vel0[water_index][5] - vel0[water_index][7]) * 39.4
    
		# Find the Impact time
		impact_time = max(impact1_time[-1],impact2_time[-1])
    
		# Save the values to be used later
		all_waterlines.append(waterline)
		all_ppm_air.append(ppm_air)
		all_ppm_water.append(ppm_water)
		all_impact_time.append(impact_time)

	return all_waterlines, all_ppm_air, all_ppm_water, all_impact_time

def findImpactVelocity(velocity_file, vel_path, vel_file_names, all_ppm_air, all_ppm_water, all_impact_time, all_waterlines):
	# Create empty lists to save scalars to
	all_impact1 = []; all_impact2 = []
	all_entry1 = []; all_entry2 = []
	all_entry3 = []; all_entry4 = []
	# Length of non-zero sections, will be used to initialize arrays
	len_impact1 = []; len_impact2 = []
	len_entry1 = []; len_entry2 = []
	len_entry3 = []; len_entry4 = []

	# Loop through all velocity files
	for i in range(0,len(velocity_file)):
		currentFile = glob.glob(vel_path[0] + vel_file_names[i] + ".csv")
		# Load file as a numpy array
		vel0 = np.loadtxt(currentFile[0],delimiter=',',skiprows=0)
		# Initialize empty lists
		impact1 = []; impact2 = []
		entry1 = []; entry2 = []
		impact1_time = []; impact2_time = []
		entry1_time = []; entry2_time = []
		# Loop through each row in one vel file
		for j in range(0,len(vel0)):
			# Find impact velocity
			if vel0[j][0] != 0:
				# find dimensional position then save to array
				position = vel0[j][0] / all_ppm_air[i]
				impact1.append(position)
				# find and shift the time then save to array
				time1 = j - all_impact_time[i]
				impact1_time.append(time1 / 5150)
			if vel0[j][2] != 0:
				# find dimensional position then save to array
				position = vel0[j][2] / all_ppm_air[i]
				impact2.append(position)
				# find and shift the time then save to array
				time2 = j - all_impact_time[i]
				impact2_time.append(time2 / 5150)
			# Find length of entry velocity profile
			if vel0[j][4] != 0:
				# find dimensional position then save to array
				position = vel0[j][4] - all_waterlines[i]
				if position > all_waterlines[i]:
					position = position / all_ppm_air[i]
				if position <= all_waterlines[i]:
					position = position / all_ppm_water[i]
				entry1.append(position)
				# find and shift the time then save to array
				time3 = j - all_impact_time[i]
				entry1_time.append(time3 / 5150)
			if vel0[j][6] != 0:
				# find dimensional position then save to array
				position = vel0[j][6] - all_waterlines[i]
				if position > all_waterlines[i]:
					position = position / all_ppm_air[i]
				if position <= all_waterlines[i]:
					position = position / all_ppm_water[i]
				entry2.append(position)
				# find and shift the time then save to array
				time3 = j - all_impact_time[i]
				entry2_time.append(time3 / 5150)
		# Find the linear fit for the last 50 points before impact, was -20
		point1_a, point1_b = np.polyfit(impact1_time[-20:],impact1[-20:],1)
		point2_a, point2_b = np.polyfit(impact2_time[-20:],impact2[-20:],1)
		# Find the linear fit for the last 50 points recorded during the entry
		point1_c, point1_d = np.polyfit(entry1_time[:40],entry1[:40],1)
		point2_c, point2_d = np.polyfit(entry2_time[:40],entry2[:40],1)
		# Find the linear fit for the last 50 points recorded during the entry, was 40
		point1_e, point1_f = np.polyfit(entry1_time[-40:],entry1[-40:],1)
		point2_e, point2_f = np.polyfit(entry2_time[-40:],entry2[-40:],1)
#		print(len(impact1_time[-10:]),len(entry1_time[:10]),len(entry1_time[-10:]))
		# Save the impact velocity
		all_impact1.append(point1_a)
		all_impact2.append(point2_a)
		# Save the entry velocity
		all_entry1.append(point1_c)
		all_entry2.append(point2_c)
		# Save the entry velocity
		all_entry3.append(point1_e)
		all_entry4.append(point2_e)
		# Save the lengths
		len_impact1.append(len(impact1_time))
		len_impact2.append(len(impact2_time))
		len_entry1.append(len(entry1_time))
		len_entry2.append(len(entry2_time))

	return  all_impact1, all_impact2, all_entry1, all_entry2, all_entry3, all_entry4,\
		len_impact1, len_impact2, len_entry1, len_entry2

def findSplash(jet_file, jet_path, jet_file_names, all_waterlines, all_ppm_air, all_ppm_water):
	# Create empty lists to save scalars to
	all_pinch1 = []; all_pinch2 = []
	all_splash = []; all_splash_time = []
	pinch_list = []
	# Length of non-zero sections, will be used to initialize arrays
	len_pinch1 = []; len_pinch2 = []
	len_splash = []
	
	# Loop through all jet files
	for i in range(0,len(jet_file)):
		currentFile = glob.glob(jet_path[0] + jet_file_names[i] + ".csv")
		# Load file as a numpy array
		jet0 = np.loadtxt(currentFile[0],delimiter=',',skiprows=0)
		# Initialize empty lists
		pinch1 = []; pinch2 = []; splash = []
		pinch1_time = []; pinch2_time = []; splash_time = []
		for j in range(len(jet0)):
			if jet0[j][0] != 0:
				# find the distance to the waterline and save
				depth = jet0[j][0] - all_waterlines[i]
				pinch1.append(depth / all_ppm_water[i])
				# save time
				pinch1_time.append(j / 5150)
			if jet0[j][2] != 0:
				# find the distance to the waterline and save
				depth = jet0[j][2] - all_waterlines[i]
				pinch2.append(depth / all_ppm_water[i])
				# save time
				pinch2_time.append(j / 5150)
			if jet0[j][4] != 0:
				height = abs(jet0[j][4] - all_waterlines[i])
				splash.append(height / all_ppm_air[i])
				# save time
				splash_time.append(j / 5150)
		# Calculate time of splash measurement
		pinch_time = min(pinch1_time[0],pinch2_time[0])
		pinch_list.append(pinch_time)
		splash_time[-1] = splash_time[-1] - pinch_time
		# Save the depth of pinch off, splash height, and time of splash measurement
		all_pinch1.append(pinch1[0])
		all_pinch2.append(pinch2[0])
		all_splash.append(max(splash))
		findindex = splash.index(max(splash))
		all_splash_time.append(splash_time[findindex])
		# Save the lengths
		len_pinch1.append(len(pinch1))
		len_pinch2.append(len(pinch2))
		len_splash.append(len(splash))

	return all_pinch1, all_pinch2, all_splash, all_splash_time, pinch_list, len_pinch1, len_pinch2, len_splash

def createEmptyArrays(len_impact1, len_impact2, len_entry1, len_entry2, len_pinch1, len_pinch2, len_splash):
	# Create empty arrays the right size to save all the velocity profiles
	impact1_vel = np.zeros((len(len_impact1),max(len_impact1)))
	impact2_vel = np.zeros((len(len_impact2),max(len_impact2)))
	entry1_vel  = np.zeros(( len(len_entry1), max(len_entry1)))
	entry2_vel  = np.zeros(( len(len_entry2), max(len_entry2)))
	impact1_t = np.zeros((len(len_impact1),max(len_impact1)))
	impact2_t = np.zeros((len(len_impact2),max(len_impact2)))
	entry1_t  = np.zeros(( len(len_entry1), max(len_entry1)))
	entry2_t  = np.zeros(( len(len_entry2), max(len_entry2)))
	pinch1_vel  = np.zeros(( len(len_pinch1), max(len_pinch1)))
	pinch2_vel  = np.zeros(( len(len_pinch2), max(len_pinch2)))
	pinch1_t  = np.zeros(( len(len_pinch1), max(len_pinch1)))
	pinch2_t  = np.zeros(( len(len_pinch2), max(len_pinch2)))
	splash_vel  = np.zeros(( len(len_splash), max(len_splash)))
	splash_pos  = np.zeros(( len(len_splash), max(len_splash)))
	splash_t  = np.zeros(( len(len_splash), max(len_splash)))

	return impact1_vel, impact2_vel, entry1_vel, entry2_vel, impact1_t, impact2_t, entry1_t, entry2_t, \
		pinch1_vel, pinch2_vel, pinch1_t, pinch2_t, splash_vel, splash_pos, splash_t

def findEntryVelocityArrays(velocity_file, vel_path, vel_file_names, all_waterlines, all_ppm_air, all_ppm_water, all_impact_time, impact1_vel, \
		 impact2_vel, entry1_vel, entry2_vel, impact1_t, impact2_t, entry1_t, entry2_t):

# Loop through to save all the velocity arrays from vel
	for i in range(0,len(velocity_file)):
		currentFile = glob.glob(vel_path[0] + vel_file_names[i] + ".csv")
		# Load file as a numpy array
		vel0 = np.loadtxt(currentFile[0],delimiter=',',skiprows=0)
		l = 0; m = 0; n = 0; o = 0
		for j in range(0,len(vel0)):
			if vel0[j][0] != 0:
				# find dimensional position then save to array
				position = ( vel0[j][0] - all_waterlines[i] ) / all_ppm_air[i]
				impact1_vel[i][l] = position
				# find and shift the time then save to array
				time1 = ( j - all_impact_time[i] ) / 5150
				impact1_t[i][l] = time1
				l = l + 1
			if vel0[j][2] != 0:
				# find dimensional position then save to array
				position = ( vel0[j][2] - all_waterlines[i] ) / all_ppm_air[i]
				impact2_vel[i][m] = position
				# find and shift the time then save to array
				time2 = ( j - all_impact_time[i] ) / 5150
				impact2_t[i][m] = time2
				m = m + 1
			if vel0[j][4] != 0:
				# find dimensional position then save to array
				position = vel0[j][4] - all_waterlines[i]
				if position > all_waterlines[i]:
					position = position / all_ppm_air[i]
				if position <= all_waterlines[i]:
					position = position / all_ppm_water[i]
				entry1_vel[i][n] = position
				# find and shift the time then save to array
				time1 = ( j - all_impact_time[i] ) / 5150
				entry1_t[i][n] = time1
				n = n + 1
			if vel0[j][6] != 0:
				# find dimensional position then save to array
				position = vel0[j][6] - all_waterlines[i]
				if position > all_waterlines[i]:
					position = position / all_ppm_air[i]
				if position <= all_waterlines[i]:
					position = position / all_ppm_water[i]
				entry2_vel[i][o] = position
				# find and shift the time then save to array
				time2 = ( j - all_impact_time[i] ) / 5150
				entry2_t[i][o] = time2
				o = o + 1
	return

def findSplashVelocityArrays(jet_file, jet_path, jet_file_names, all_waterlines, all_ppm_air, all_ppm_water, all_impact_time, pinch_list, \
		 pinch1_vel, pinch2_vel, pinch1_t, pinch2_t, splash_vel, splash_pos, splash_t):

# Loop through to save all the velocity arrays from jet
	for i in range(0,len(jet_file)):
		currentFile = glob.glob(jet_path[0] + jet_file_names[i] + ".csv")
		# Load file as a numpy array
		jet0 = np.loadtxt(currentFile[0],delimiter=',',skiprows=0)
		# Initialize empty lists
		pinch1_time = []; pinch2_time = []; splash_time = []
		l = 0; m = 0; n = 0
		for j in range(len(jet0)):
			if jet0[j][0] != 0:
				# find the distance to the waterline and save
				depth = jet0[j][0] - all_waterlines[i]
				depth = depth / all_ppm_water[i]
				pinch1_vel[i][l] = depth
				# save time
				time1 = ( j - pinch_list[i] ) / 5150
				pinch1_t[i][l] = time1
				l = l + 1
			if jet0[j][2] != 0:
				# find the distance to the waterline and save
				depth = jet0[j][2] - all_waterlines[i]
				depth = depth / all_ppm_water[i]
				pinch2_vel[i][m] = depth
				# save time
				time2 = (j - pinch_list[i]) / 5150
				pinch2_t[i][m] = time2
				m = m + 1
			if jet0[j][4] != 0:
				# find the distance to the waterline and save
				height = jet0[j][4] - all_waterlines[i]
				x_pos = jet0[j][5] / all_ppm_air[i]
				height = height / all_ppm_air[i]
				splash_vel[i][n] = height
				splash_pos[i][n] = x_pos
				# save time
				time3 = (j - pinch_list[i]) / 5150
				splash_t[i][n] = time3
				n = n + 1
	return




