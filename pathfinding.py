# DO NOT RUN ON EV3
# For generating the shortest path between two nodes
import math


class Hexagon(object):
    def __init__(self, coords: tuple):
        self.q = coords[0]
        self.r = coords[1]

        # self.s = -1 * (self.r + self.q)
    
    def __str__(self):
        return f"({self.q},{self.r})"


def print_grid():
    for row in grid:
        for hx in row:
            print(hx, end=" ")
        print()


grid = [[None] * 16 for i in range(14)]

num = 0

for q in range(16):
    for i in range(6):
        num += 1
        r = i + (8 - math.ceil(q / 2))

        if q >= 6 or q <= 8:
            if f"{q},{r}" in ["6,10", "7,9", "8,9"]:
                break

        grid[r][q] = Hexagon((q, r))


print_grid()