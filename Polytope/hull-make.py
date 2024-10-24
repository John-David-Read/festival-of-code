import random
import numpy as np
from math import pi, asin, acos, cos, sin, sqrt
import scipy.spatial as sp
import matplotlib.pyplot as pp

def triangle_area(a, b, c):
    ab = np.array(b) - np.array(a)
    ac = np.array(c) - np.array(a)
    cross_product = np.cross(ab, ac)
    return np.linalg.norm(cross_product) / 2

def polyhedron_surface_area(vertices, faces):
    surface_area = 0
    for face in faces:
        for i in range(1, len(face) - 1):
            surface_area += triangle_area(vertices[face[0]], vertices[face[i]], vertices[face[i + 1]])
    return surface_area

def tetrahedron_volume(a, b, c, d):
    matrix = np.array([
        [a[0] - d[0], a[1] - d[1], a[2] - d[2]],
        [b[0] - d[0], b[1] - d[1], b[2] - d[2]],
        [c[0] - d[0], c[1] - d[1], c[2] - d[2]]
    ])
    return abs(np.linalg.det(matrix)) / 6

def polyhedron_volume(vertices, faces):
    volume = 0.0
    for face in faces:
        for i in range(1, len(face) - 1):
            volume += tetrahedron_volume(vertices[face[0]], vertices[face[i]], vertices[face[i + 1]], vertices[0])
    return volume

def repel(n):
    vert = np.empty((0,3))

    for i in range(n):
        theta = random.random() * 2 * pi
        phi = asin(random.random() * 2 - 1)
        vert = np.vstack([vert,[cos(theta)*cos(phi), sin(theta)*cos(phi), sin(phi)]])

    while True:
        forces = []
        for i in range(len(vert)):
            p = vert[i]
            f = (0,0,0)
            ftotal = 0
            for j in range(len(vert)):
                if j == i: 
                    continue
                q = vert[j]
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
        for i in range(len(vert)):
            p = vert[i]
            f = forces[i]
            p2 = (p[0] + f[0]*fscale, p[1] + f[1]*fscale, p[2] + f[2]*fscale)
            pl = sqrt(p2[0]**2 + p2[1]**2 + p2[2]**2)
            p2 = (p2[0] / pl, p2[1] / pl, p2[2] / pl)
            dv = (p[0]-p2[0], p[1]-p2[1], p[2]-p2[2])
            dl = sqrt(dv[0]**2 + dv[1]**2 + dv[2]**2)
            dist = dist + dl
            vert[i] = p2
        if dist < 1e-10:
            break
    return(vert)

def shape(pts):
    vert = repel(pts)
    hull = sp.ConvexHull(vert)
    face = np.empty((0,3))
    for f in hull.simplices:
        face = np.vstack([face,f])
    face = face.astype(int)
    return (vert,hull,face)

def vlist(pts,vert,face):
    v_shape = polyhedron_volume(vert, face)
    sa_shape = polyhedron_surface_area(vert, face)
    print("vertices:",pts,"Volume:",v_shape,"Surface Area:",sa_shape)

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

p = 9

for n in range (4,p+1):
    v, h, f = shape(n)
    vlist(n,v,f)

v, h, f = shape(5)
vlist(len(v),v,f)

v2, h2, f2 = minshapeeight()
vlist(len(v2),v2,f2)

plot(v,h)
