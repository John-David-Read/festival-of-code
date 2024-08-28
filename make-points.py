# Distribute a set of points randomly across a sphere, allow them to mutually repel and find equilibrium.
import random
from math import pi, asin, cos, sin, sqrt
import matplotlib.pyplot as pp
import numpy as np

n = 4
points = np.empty((0,3))

for i in range(n):
    theta = random.random() * 2 * pi
    phi = asin(random.random() * 2 - 1)
    points = np.vstack([points,[cos(theta)*cos(phi), sin(theta)*cos(phi), sin(phi)]])

while True:
    # Determine the total force acting on each point.
    forces = []
    for i in range(len(points)):
        p = points[i]
        f = (0,0,0)
        ftotal = 0
        for j in range(len(points)):
            if j == i: 
                continue
            q = points[j]
            dv = (p[0]-q[0], p[1]-q[1], p[2]-q[2])
            dl = sqrt(dv[0]**2 + dv[1]**2 + dv[2]**2)
            dl3 = dl ** 3
            fv = (dv[0]/dl3, dv[1]/dl3, dv[2]/dl3)
            f = (f[0]+fv[0], f[1]+fv[1], f[2]+fv[2])
        forces.append(f)
        ftotal = ftotal + sqrt(f[0]**2 + f[1]**2 + f[2]**2)

    if ftotal > 0.25:
        fscale = 0.25 / ftotal
    else:
        fscale = 1

    dist = 0

    for i in range(len(points)):
        p = points[i]
        f = forces[i]
        p2 = (p[0] + f[0]*fscale, p[1] + f[1]*fscale, p[2] + f[2]*fscale)
        pl = sqrt(p2[0]**2 + p2[1]**2 + p2[2]**2)
        p2 = (p2[0] / pl, p2[1] / pl, p2[2] / pl)
        dv = (p[0]-p2[0], p[1]-p2[1], p[2]-p2[2])
        dl = sqrt(dv[0]**2 + dv[1]**2 + dv[2]**2)
        dist = dist + dl
        points[i] = p2
    if dist < 1e-6:
        break

for x, y, z in points:
    print(x, y, z)

pp.rcParams["figure.figsize"] = [10.00, 10.00]
pp.rcParams["figure.autolayout"] = True
fig = pp.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(points[:,0],points[:,1],points[:,2],"ko")
pp.show()
