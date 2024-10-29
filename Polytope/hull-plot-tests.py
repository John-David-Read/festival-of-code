import random
import numpy as np
from math import pi, asin, acos, cos, sin, sqrt
import scipy.spatial as sp
import matplotlib.pyplot as pp

def plot(vert,hull):
    pp.rcParams["figure.figsize"] = [10.00, 10.00]
    pp.rcParams["figure.autolayout"] = True
    fig = pp.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot(vert[:,0],vert[:,1],vert[:,2],"mo")
    ax.set_aspect('equal')
    for sx in hull.simplices:
        sx = np.append(sx,sx[0])
        pp.plot(vert[sx,0],vert[sx,1],vert[sx,2],'m-')
    ax.set_axis_off()
    pp.show()
    
def minshapeeight():
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
    hm = sp.ConvexHull(vm)
    fm = np.empty((0,3))
    for f in hm.simplices:
        fm = np.vstack([fm,f])
    fm = fm.astype(int)
    return vm, hm, fm

v, h, f = minshapeeight()

print(v,f)
plot(v,h)
