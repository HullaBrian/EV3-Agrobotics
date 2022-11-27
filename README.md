# EV3-Agrobotics
## The plan

The first step is to modify the game board in the scripts to reflect the layout of the competition board state.

The idea is to run 'scripter.py' on the local machine, generate the script, then upload out/main.py to the EV3 robot

Of course, this is still a work in progresss

Useful links:
 - [Board layout](https://texas4-h.tamu.edu/wp-content/uploads/robotics_agrobotics_game_mat_2022_2023.pdf)
 - [ev3 Micropython documentation](https://pybricks.com/ev3-micropython/startbrick.html)


## Pathfinding
In pathfinding.py, implementing pathfinding is very simple.

To get pathfinding to work:
1. Create a start point for the robot using a tuple
2. Initialize a grid using the width, height, and start point
    - The width and height, and start are optional, but recommended
3. Call ```GRID.pathfind(END_POINT)``` where GRID is the Grid object and END_POINT is the end coordinates (in a tuple)

Below is an example:
```
start = (7, 4)
grid = Grid(start=start)
for node in grid.pathfind((0, 12)):
    print(node)
```