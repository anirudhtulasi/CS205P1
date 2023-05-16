# File: eight_puzzle.py
import numpy as np
from copy import deepcopy
from node import Node

class EightPuzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions_list = ["UP", "DOWN", "LEFT", "RIGHT"]

    def actions(self, state):
        possible_actions = []
        zero_index = np.where(np.array(state) == 0)

        if zero_index[1] > 0:  # LEFT action possible
            possible_actions.append("LEFT")
        if zero_index[1] < 2:  # RIGHT action possible
            possible_actions.append("RIGHT")
        if zero_index[0] > 0:  # UP action possible
            possible_actions.append("UP")
        if zero_index[0] < 2:  # DOWN action possible
            possible_actions.append("DOWN")

        return possible_actions

    def result(self, state, action):
        new_state = deepcopy(state)
        zero_index = np.where(np.array(state) == 0)

        if action == "UP":
            new_state[zero_index[0][0]][zero_index[1][0]], new_state[zero_index[0][0] - 1][zero_index[1][0]] = new_state[zero_index[0][0] - 1][zero_index[1][0]], new_state[zero_index[0][0]][zero_index[1][0]]
        elif action == "DOWN":
            new_state[zero_index[0][0]][zero_index[1][0]], new_state[zero_index[0][0] + 1][zero_index[1][0]] = new_state[zero_index[0][0] + 1][zero_index[1][0]], new_state[zero_index[0][0]][zero_index[1][0]]
        elif action == "LEFT":
            new_state[zero_index[0][0]][zero_index[1][0]], new_state[zero_index[0][0]][zero_index[1][0] - 1] = new_state[zero_index[0][0]][zero_index[1][0] - 1], new_state[zero_index[0][0]][zero_index[1][0]]
        elif action == "RIGHT":
            new_state[zero_index[0][0]][zero_index[1][0]], new_state[zero_index[0][0]][zero_index[1][0] + 1] = new_state[zero_index[0][0]][zero_index[1][0] + 1], new_state[zero_index[0][0]][zero_index[1][0]]

        return new_state

    def goal_test(self, state):
        return np.array_equal(state, self.goal_state)

    def step_cost(self, parent_state, action):
    # Assuming each action has a cost of 1
        return 1

    def child_node(self, parent, action):
        child_state = self.result(parent.state, action)
        return Node(child_state, parent, action, self.step_cost(parent.state, action))


    def h(self, state, heuristic):
        distance = 0
        if heuristic == "misplaced_tiles":
            return np.sum(state != self.goal_state) - 1  # subtract 1 because we don't count the blank space
        elif heuristic == "manhattan_distance":
            distance = 0
            for i in range(1, 9):  # 1-8 for 8-puzzle
                actual_position = np.array(np.where(state == i))
                goal_position = np.array(np.where(self.goal_state == i))
                distance += np.sum(np.abs(actual_position - goal_position))
        return distance

    def solution(self, node):
        path = []
        while node is not None:
            path.append(node)
            node = node.parent
        return path[::-1]  # reverse
