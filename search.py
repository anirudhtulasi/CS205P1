# File: search.py
import heapq
import numpy as np
from eight_puzzle import EightPuzzle
from node import Node
import time

def general_search(problem, heuristic=None):
    node = Node(problem.initial_state, None, None, 0)
    if problem.goal_test(node.state):
        return problem.solution(node), 0, 1  # Start the max queue size from 1

    frontier = []
    frontier_set = set()  # A set to keep track of states in the frontier
    heapq.heappush(frontier, (node.path_cost + (problem.h(node.state, heuristic) if heuristic else 0), node))
    frontier_set.add(tuple(map(tuple, node.state.tolist())))  # Add the node's state to frontier_set
    explored = set()
    nodes_expanded = 0
    max_queue_size = 1  # Initialize the max queue size

    while frontier:
        _, node = heapq.heappop(frontier)
        frontier_set.remove(tuple(map(tuple, node.state.tolist())))  # Remove the node's state from frontier_set
        if problem.goal_test(node.state):
            return problem.solution(node), nodes_expanded, max_queue_size

        explored.add(tuple(map(tuple, node.state.tolist())))  # convert np.array to tuple for hashing
        nodes_expanded += 1

        for action in problem.actions(node.state):
            child = problem.child_node(node, action)
            child_tuple = tuple(map(tuple, child.state.tolist()))

            if child_tuple not in explored and child_tuple not in frontier_set:
                heapq.heappush(frontier, (child.path_cost + (problem.h(child.state, heuristic) if heuristic else 0), child))
                frontier_set.add(child_tuple)  # Add the child's state to frontier_set

                # If the current size of the queue is larger than the max queue size, update the max queue size
                if len(frontier) > max_queue_size:
                    max_queue_size = len(frontier)

    return None, nodes_expanded, max_queue_size

def print_solution(solution):
    for i, node in enumerate(solution):
        print(f"Step {i}:")
        print(node.state)

def get_state_from_user():
    state = []
    for i in range(1, 4):
        row = list(map(int, input(f"Enter the {i} row: ").split()))
        state.append(row)
    return np.array(state)

def main():
    print("Welcome to my 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own.")
    choice = input()

    if choice == '1':
        initial_state = np.array([[8, 6, 7], [2, 5, 4], [3, 0, 1]])
        goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    elif choice == '2':
        print("Enter your puzzle, using a zero to represent the blank. Please only enter valid 8-puzzles. Enter the puzzle demilimiting the numbers with a space. Type RETURN only when finished.")
        print("Example for Input : Three Numbers per line as shown below")
        print("8 6 7")
        print("2 5 4")
        print("3 0 1")
        initial_state = get_state_from_user()
        goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    else:
        print("Invalid choice.")
        return

    problem = EightPuzzle(initial_state, goal_state)

    print("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, or (3) the Manhattan Distance Heuristic.")
    algo_choice = input()
    
    if algo_choice == '1':
        print("Uniform Cost Search Solution:")
        start_time = time.time()
        solution, expanded_nodes, max_queue_size = general_search(problem)
    elif algo_choice == '2':
        print("A* with Misplaced Tile heuristic Solution:")
        start_time = time.time()
        solution, expanded_nodes, max_queue_size = general_search(problem, "misplaced_tiles")
    elif algo_choice == '3':
        print("A* with Manhattan Distance heuristic Solution:")
        start_time = time.time()
        solution, expanded_nodes, max_queue_size = general_search(problem, "manhattan_distance")
    else:
        print("Invalid choice.")
        return

    end_time = time.time()

    if solution is not None:
        print_solution(solution)
        print(f"Depth of solution: {solution[-1].depth}")
        print(f"Path cost: {solution[-1].path_cost}")
        print(f"Number of nodes expanded: {expanded_nodes}")
        print(f"Max queue size: {max_queue_size}")
    else:
        print("No solution found.")
    
    print(f"Time taken: {(end_time - start_time) * 1000} ms")  # Multiply by 1000 to get time in milliseconds

if __name__ == "__main__":
    main()
