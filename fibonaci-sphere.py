import matplotlib.pyplot as pp
import numpy as np
import scipy.spatial as sp
from math import pi , cos , sin , sqrt

def fibonacci_sphere(samples=200):
    points = np.empty((0,3))
    phi = pi * (sqrt(5.) - 1.)                  # golden angle in radians
    for i in range(samples):
        y = 1 - (i / float(samples - 1)) * 2    # y goes from 1 to -1
        radius = sqrt(1 - y * y)                # radius at y
        theta = phi * i                         # golden angle increment
        x = cos(theta) * radius
        z = sin(theta) * radius
        points = np.vstack([points,[x,y,z]])
    return points

s_a = fibonacci_sphere()
hull = sp.ConvexHull(s_a)

pp.rcParams["figure.figsize"] = [10.00, 10.00]
pp.rcParams["figure.autolayout"] = True
fig = pp.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(s_a[:,0],s_a[:,1],s_a[:,2],"ko")
for sx in hull.simplices:
    sx = np.append(sx,sx[0])
    pp.plot(s_a[sx,0],s_a[sx,1],s_a[sx,2],'k-')
pp.show()