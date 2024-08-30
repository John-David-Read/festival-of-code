import numpy as np
import random
from math import pi, sin, cos, asin, acos, sqrt
import scipy.spatial as sp
import scipy.optimize as op

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
     
# Initial guess for the vertices (random points on the unit sphere)
n = 8  # Number of vertices
angle = angle_random(n)
print(volume(angle))

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

#print(vm)
#print(len(vm))
#print(polyhedron_volume(vm))

# Define the constraints and bounds
#bounds = [(-1, 1)] * len(vert)

# Optimize the volume
#result = op.minimize(lambda x: -polyhedron_volume(x.reshape(-1, 3)), vert, constraints=constraints, bounds=bounds)

# Get the optimized vertices
#optimized_vertices = result.x.reshape(-1, 3)

#print("Optimized vertices:")
#print(optimized_vertices)
#print("Maximized volume:", -result.fun)
