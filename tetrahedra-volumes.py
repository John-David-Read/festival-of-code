import numpy as np
import scipy.spatial as sp

def triangle_area(a, b, c):
    # Calculate the area of a triangle using the cross product
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

vertices_tetra = np.array([
    [0.000, 0.000, 1.000],
    [0.943, 0.000, -0.333],
    [-0.471, 0.816, -0.333],
    [-0.471, -0.816, -0.333]
])

faces_tetra = np.array([
    [0, 1, 2],
    [0, 1, 3],
    [0, 2, 3],
    [1, 2, 3]
])

print("Volume of the polyhedron:", polyhedron_volume(vertices_tetra, faces_tetra))

r = 1
v_sphere = 4/3 * np.pi * r ** 3
theta = 2/3 * np.pi
phi = np.arccos(-1/3)

vertex_1 = [0,0,r]
vertex_2 = [r*np.sin(phi)*np.cos(0),r*np.sin(phi)*np.sin(0),r*np.cos(phi)]
vertex_3 = [r*np.sin(phi)*np.cos(theta),r*np.sin(phi)*np.sin(theta),r*np.cos(phi)]
vertex_4 = [r*np.sin(phi)*np.cos(-theta),r*np.sin(phi)*np.sin(-theta),r*np.cos(phi)]

vertices_tetra = np.array([vertex_1,
                  vertex_2,
                  vertex_3,
                  vertex_4
])

print("Volume of unit sphere",round(v_sphere,3))
v_shape = polyhedron_volume(vertices_tetra, faces_tetra)
print("Volume of the polyhedron:",v_shape,", ratio of volume of sphere",v_shape/v_sphere)
print("Surface area of the polyhedron:", polyhedron_surface_area(vertices_tetra, faces_tetra))