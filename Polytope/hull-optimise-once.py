#import libraries 
import numpy as np # numpy to stack vectors in matrices
import random # random to generate random numbers
from math import pi, sin, cos, asin # maths functions used
import scipy.spatial as sp # sci py algorithms for calculating convex hulls , spatial transformation etc. 
import scipy.optimize as op # sci py algorithms for optimising on several variables
import matplotlib.pyplot as pp # mathplot lib to plot shapes including polyhedra

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
    ax.set_aspect('equal')
    for sx in hull.simplices:
        sx = np.append(sx,sx[0])
        pp.plot(vert[sx,0],vert[sx,1],vert[sx,2],'k-')
    ax.set_axis_off()
    pp.show()

#function to compare volume against list of local maxima already found to see if this one is larger
def compare(this_volume,local_maxima):
    if local_maxima == []:
        return True
    for i in range(len(local_maxima)):
        how_close = abs(local_maxima[i]-this_volume)
        if (how_close <= 0.0000001):
            return False
    return True

#run for n vertices and collect succesive maximum volumes listing the local maxima found
n = 8
local_maxima = []

for i in range(1,100):
    angle = angle_random(n)
    bounds = []
    bounds = [(0, 2*pi),(-pi/2,pi/2)] * n
    result = op.minimize(lambda x: -volume(x), angle, bounds=bounds,tol=0.00000000000000000001)
    this_volume = volume(result.x)
    if compare(this_volume,local_maxima):
        local_maxima.append(this_volume)
    if this_volume == max(local_maxima):
        result_max = result

optimised_angles = result_max.x
optimised_vertices = angle_vertices(optimised_angles)

# output the angles , vertices and volume for the maxium volume polyhedron found
print(optimised_angles)
print()
print(optimised_vertices)
print()
print(volume(optimised_angles))
print()
print(local_maxima)
                           
# Plot the shape
plot(optimised_vertices,sp.ConvexHull(optimised_vertices))

