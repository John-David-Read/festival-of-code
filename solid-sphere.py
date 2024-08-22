
import matplotlib.pyplot as pp
import numpy as np

pp.rcParams["figure.figsize"] = [10.00, 10.00]
pp.rcParams["figure.autolayout"] = True
fig = pp.figure()
ax = fig.add_subplot(projection='3d')
r = 0.05
u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:20j]
x = np.cos(u) * np.sin(v)
y = np.sin(u) * np.sin(v)
z = np.cos(v)
pp.rcParams["figure.figsize"] = [10.00, 10.00]
ax.plot_surface(x, y, z, cmap=pp.cm.YlGnBu_r)
pp.show()