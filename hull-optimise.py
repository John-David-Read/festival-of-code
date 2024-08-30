import numpy as np
import random
from math import pi, sin, cos, asin, acos, sqrt
import scipy.spatial as sp
import scipy.optimize as op

# Function to calculate the volume of a polyhedron given its vertices
def polyhedron_volume(vertices):
    hull = sp.ConvexHull(vertices)
    return hull.volume

# Constraint to ensure vertices lie on the unit sphere
def constraint(vertices):
    return np.sum(vertices**2, axis=1) - 1

# Initial guess for the vertices (random points on the unit sphere)
n = 8  # Number of vertices
vert = np.empty((0,3))

for i in range(n):
    theta = random.random() * 2 * pi
    phi = asin(random.random() * 2 - 1)
    vert = np.vstack([vert,[cos(theta)*cos(phi), sin(theta)*cos(phi), sin(phi)]])

# Define the constraints and bounds
constraints = {'type': 'eq', 'fun': constraint}
bounds = [(-1, 1)] * len(vert)

print(vert)
print(len(vert))
print(polyhedron_volume(vert))

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

print(vm)
print(len(vm))
print(polyhedron_volume(vm))

# Optimize the volume
#result = op.minimize(lambda x: -polyhedron_volume(x.reshape(-1, 3)), vert, constraints=constraints, bounds=bounds)

# Get the optimized vertices
#optimized_vertices = result.x.reshape(-1, 3)

#print("Optimized vertices:")
#print(optimized_vertices)
#print("Maximized volume:", -result.fun)
