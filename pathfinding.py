# DO NOT RUN ON EV3
# For generating the shortest path between two nodes
import math


class Hexagon(object):
    def __init__(self, coords: tuple):
        self.q = coords[0] # Coordinate corresponding to column
        self.r = coords[1] # Coordinate corresponding to negative diagonal

        #s coordinate is calculated from r and q and is used for some calculations
        self.s = -1 * (self.r + self.q) # Coordinate corresponding to positive diagonal
    
    def __str__(self):
        return f"({self.q},{self.r})"


def print_grid():
    for row in grid:
        for hex in row:
            print(hex, end=" ")
        print()

#Initiating map as 2-D array with all values set to "None"
grid = [[None] * 16 for i in range(14)]

#Defining all existing hexes
for q in range(16):
    for i in range(6):
        r = i + (8 - math.ceil(q / 2))

        #Ignore hexes that are not printed on the moon base
        if q >= 6 or q <= 8:
            if f"{q},{r}" in ["6,10", "7,9", "8,9"]:
                break

        grid[r][q] = Hexagon((q, r))


print_grid()