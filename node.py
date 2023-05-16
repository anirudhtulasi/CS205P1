# File: node.py
import numpy as np

class Node:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        if parent is not None:
            self.path_cost = parent.path_cost + path_cost
            self.depth = parent.depth + 1  # Increment depth from parent node
        else:
            self.path_cost = path_cost
            self.depth = 0  # Root node depth is 0

    def __eq__(self, other):
        return isinstance(other, Node) and np.array_equal(self.state, other.state)

    def __lt__(self, other):
        return self.path_cost < other.path_cost
