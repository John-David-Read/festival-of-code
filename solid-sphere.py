
import matplotlib.pyplot as pp
from numpy import mgrid, cos, sin, pi

pp.rcParams["figure.figsize"] = [10.00, 10.00]
pp.rcParams["figure.autolayout"] = True
fig = pp.figure()
ax = fig.add_subplot(projection='3d')
r = 0.05
u, v = mgrid[0:2 * pi:30j, 0:pi:20j]
x = cos(u) * sin(v)
y = sin(u) * sin(v)
z = cos(v)
pp.rcParams["figure.figsize"] = [10.00, 10.00]
ax.plot_surface(x, y, z, cmap=pp.cm.YlGnBu_r)
pp.show()