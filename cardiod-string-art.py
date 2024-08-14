from generativepy.drawing import make_image,setup
from generativepy.color import Color
from generativepy.geometry import Line
from PIL import Image
import math

N = 200

def draw(ctx, width, height, frame_no, frame_count):

    setup(ctx, width, height, startx=-1.1, starty=-1.1,
          width=2.2, background=Color(0.25))

    points = [(math.cos(i*2*math.pi/N), math.sin(i*2*math.pi/N))
                  for i in range(N)]
    color = Color(0.6, 0.6, 1, 0.25)

    for i in range(N):
        j = (i*2) % N
        Line(ctx).of_start_end(points[i], points[j]).stroke(color, .005)

make_image(r"Resource/cardioid.png", draw, 1200, 1200)

image = Image.open('Resource/cardioid.png')
image.show()
