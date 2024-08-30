import numpy as np
import random
from math import pi, sin, cos, asin, acos, sqrt
import scipy.spatial as sp
import scipy.optimize as op
import matplotlib.pyplot as pp

# Function to calculate the volume of a polyhedron given its vertices
def polyhedron_volume(vertices):
    hull = sp.ConvexHull(vertices)
    return hull.volume

# Function to calculate a vertices matrix from a list of angles
def angle_vertices(angle):
    vert = np.empty((0,3))
    for i in range(int(len(angle)/2)):
        vert = np.vstack([vert,[cos(angle[2*i])*cos(angle[2*i+1]), sin(angle[2*i])*cos(angle[2*i+1]), sin(angle[2*i+1])]])
    return(vert)

# function to create n pairs of random angles from 0 - 2 pi
def angle_random(n):
    angle = []
    for i in range(n):
        theta = random.random() * 2 * pi
        phi = asin(random.random() * 2 - 1)
        angle.append(theta)
        angle.append(phi)
    return(angle)

# function to return the polyhedron volume given the angles
def volume(angle):
    return (polyhedron_volume(angle_vertices(angle)))

# function to plot the shape
def plot(vert,hull):
    pp.rcParams["figure.figsize"] = [10.00, 10.00]
    pp.rcParams["figure.autolayout"] = True
    fig = pp.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot(vert[:,0],vert[:,1],vert[:,2],"ko")
    for sx in hull.simplices:
        sx = np.append(sx,sx[0])
        pp.plot(vert[sx,0],vert[sx,1],vert[sx,2],'k-')
    pp.show()

vm = np.empty((0,3))
phi = acos(sqrt((15+sqrt(145))/40))
vm = np.vstack([vm,[sin(3*phi),0,cos(3*phi)]])
vm = np.vstack([vm,[sin(phi),0,cos(phi)]])
vm = np.vstack([vm,[-sin(phi),0,cos(phi)]])
vm = np.vstack([vm,[-sin(3*phi),0,cos(3*phi)]])
vm = np.vstack([vm,[0,-sin(3*phi),-cos(3*phi)]])
vm = np.vstack([vm,[0,-sin(phi),-cos(phi)]])
vm = np.vstack([vm,[0,sin(phi),-cos(phi)]])
vm = np.vstack([vm,[0,sin(3*phi),-cos(3*phi)]])

# print the exact volume for the known 8 vertex shape
 print(round(polyhedron_volume(vm),12))

for n in range(4,8):

     Initial guess for the vertices (random points on the unit sphere)
    angle = angle_random(n)

    # Define the bounds for the string of angles
    bounds = []
    bounds = [(0, 2*pi),(-pi/2,pi/2)] * n

    # Optimize the volume
    result = op.minimize(lambda x: -volume(x), angle, bounds=bounds,tol=0.000000000000000001)
    
    # Get the optimized angles
    optimized_angles = result.x

    # Print the optimized angle volume
    print(n,"|",round(volume(optimized_angles),12))

# Plot the shape
# plot(angle_vertices(optimized_angles),sp.ConvexHull(angle_vertices(optimized_angles)))