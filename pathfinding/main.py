import pathlib
import os

import pyglet
from pyglet import image
from pyglet.gl import *
from grid import Grid


grid = Grid(start=(7, 4))


glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
window = pyglet.window.Window(width=1000, height=459)

# print(pathlib.Path.cwd())
image = image.load(os.path.join(pathlib.Path.cwd(), "pathfinding", 'PAIN.png'))

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)
pyglet.app.run()