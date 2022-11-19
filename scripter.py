# DO NOT RUN ON EV3
# This script is for generating the robot script.
 
from pathfinding import dijkstra_algorithm
from pathfinding import Graph
from pathfinding import distancizer

from qof import board_formatter


BOARD_LEN = 93  # Inches
BOARD_WIDTH = 45  # Inches

BOARD = \
"""\
~ X ~
~ X ~
~ X ~
A ~ B
A ~ B
A ~ B
~ C ~
~ C ~
~ C ~\
"""
BOARD = board_formatter(BOARD)
START_NODE = "X"

graph = Graph(nodes=BOARD, init_graph=distancizer(BOARD, 5))  # nodes is the list of nodes in a 1d array, and init graph is a dictionary containing the distances between nodes
previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=START_NODE)