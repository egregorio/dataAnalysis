import numpy as np
import matplotlib.pyplot as plt

points = np.loadtxt('/Users/elizabeth/Box Sync/dataAnalysis/plots_fall_2021/bestFitLine_yStd.txt')

x_points = points[:,0]
y_points = points[:,1]

interpp = np.linspace(0,1,100)

linearFit = -1.3915*interpp + 0.005


plt.figure()
plt.plot(x_points,y_points,'o')
plt.plot(interpp,linearFit)
plt.show()


