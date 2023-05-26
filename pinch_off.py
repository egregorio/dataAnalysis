import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors



# Plot for the STD in Y direction
fig = plt.figure()
plt.title('Depth of Pinch Off (cm)')
ax = fig.add_axes([0,0,1,1])
labels = [ '10.4-Degree, Hinge', '10.4-Degree, Fixed', \
	   '22.7-Degree, 0.0077Nm', '22.7-Degree, 0.0180', \
	   '22.7-Degree, 0.0153Nm', '22.7-Degree, Fixed', \
	   '28.6-Degree, Hinge', '28.6-Degree, Fixed']
depths = [ 3.602181818, 4.457959184, \
	   4.618181818, 4.849090908, \
	   5.911272726, 5.702040817, \
	   4.987636363, 6.790612246]
ax.bar(labels,depths)
plt.savefig('/Users/elizabeth/egregorio@gwmail.gwu.edu - Google Drive/My Drive/Box Sync/air cavity analysis/paper_cavity_visualization/pinch_off/pinch_off_bar.png')#_error.png')


