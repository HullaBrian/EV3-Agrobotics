import pathlib
import os

import pyglet
from pyglet import image

from loguru import logger

from grid import Grid
from entities import Robot

grid = Grid(start=(7, 4))

window = pyglet.window.Window(width=1000, height=459, caption="Robot Pathfinding")

# Get board
image = image.load(os.path.join(pathlib.Path.cwd(), 'PAIN.png'))

# Init robot
robot = Robot(50, 50)
robot.set_center(grid.hex_to_px(grid.grid[1][12]))
logger.info(f"Set robot on tile {grid.grid[1][12]}hex -> ({robot.x},{robot.y})px")

"""
Each hexagon on the 1000x459 grid is 70px tall 82px wide
"""

@window.event
def on_draw():
    window.clear()

    image.blit(0, 0)
    robot.draw()


pyglet.app.run()
