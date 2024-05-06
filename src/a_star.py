import math
import heapq
import numpy as np
import sys

sys.setrecursionlimit(1000000000)

class a_star:
    def __init__(self) -> None:
        pass

    '''
        Function: calls A* with a heuristic
        Parameters: the intial game board, and the heuristic name as a string
        Return: Intial state if no solution, A child node if solution exists 
    '''
    def call_a_star(self, puzzle, heuristic_type):
        heapq.heappush(puzzle.frontier, (0, puzzle.root))
        while len(puzzle.frontier) > 0:
            pair = heapq.heappop(puzzle.frontier)
            puzzle.numOfExpandedNodes+=1
            
            node = pair[1]  # contains the actual node object 
            curr_node_cost = node.cost    # contrains the numerical cost from start to curr (g value)

            # calculate the g(n) + h(n) cost
            node.totalCost = node.cost + node.heuristic

            # print(puzzle.frontier)

            # add into explored list 
            puzzle.seen[puzzle.toString(node)] = node

            if puzzle.isGoal(node):
                print("Goal is found!")
                print(node.printPuzzle())
                print("Number of Expanded Nodes: ", puzzle.numOfExpandedNodes)
                return puzzle.seen
            
            print(puzzle.numOfExpandedNodes)

            # check each child node created by possible actions
            for action in puzzle.expandNode(node):
                # print(len(puzzle.frontier))
        
                # spawn the child node based on the action
                child = None
                if action == "right":
                    child = puzzle.operator_go_right(node)
                elif action == "left":
                    child = puzzle.operator_go_left(node)
                elif action == "up":
                    child = puzzle.operator_go_up(node)
                elif action == "down":
                    child = puzzle.operator_go_down(node)

                # calculate the child node g value
                child_cost = child.parent.cost + 1
                            
                # update child node if smaller cost     
                puzzleString = puzzle.toString(child)
                if puzzleString in puzzle.seen: continue

                for pair in puzzle.frontier:
                    if np.array_equal(pair[1].n_puzzle, child.n_puzzle) and child_cost > curr_node_cost:
                        continue

                if puzzleString not in puzzle.seen or child.cost < puzzle.seen[puzzleString].cost:
                    child.cost = child_cost
                    child.heuristic = self.heuristic_cost(heuristic_type, child)
                    child.total_cost = child.cost + child.heuristic
                    child.parent = node

                    heapq.heappush(puzzle.frontier, (child.cost + child.heuristic, child))
                    puzzle.seen[puzzleString] = child
                    puzzle.maxQueueSize = max(puzzle.maxQueueSize, len(puzzle.frontier))

            puzzle.seen[puzzle.toString(node)] = node

        return None

    # helper function
    def heuristic_cost(self, heuristic, child):
        heuristic_cost = 0
        if heuristic == "misplaced": heuristic_cost = self._misplaced_tile_heuristic(child)
        if heuristic == "euclidean": heuristic_cost = self._euclidean_distance_heuristic(child)
        return heuristic_cost
        

    """
        Function: returns the heuristic cost of misplaced tile
        Parameters: A possible child node
        Return: Heuristic cost of child node
    """
    def _misplaced_tile_heuristic(self, child_node):
        cost = 0
        tracker = 1

        for i in range(child_node.n_puzzle.shape[0]):
            for j in range(child_node.n_puzzle.shape[1]):
                if child_node.n_puzzle[i,j] != tracker and child_node.n_puzzle[i,j] != 0:
                    cost += 1
                tracker+=1

        return cost

    """
        Function: return the heuristic cost with euclidean distance for each tile
        Parameters: A possible child node
        Return: Heuristic cost of child node
    """
    '''def _euclidean_distance_heuristic(self, child_node):

        cost = 0
        curr_row = 0
        curr_column = 0
        dimensionality = child_node.n_puzzle.shape[1]
        correct_val = 1 #meant to indicate what the correct tile at that location in the grid is
        for i in range(child_node.n_puzzle.shape[0]):
            for j in range(child_node.n_puzzle.shape[1]):
                if((correct_val != child_node.n_puzzle[i, j]) and (child_node.n_puzzle[i,j] != 0) and(i*j != dimensionality ** 2)):
                    goal_row = correct_val / dimensionality
                    goal_column = (correct_val % dimensionality) - 1

                    euclidean_distance = math.sqrt(((goal_column - curr_column) ** 2) + ((goal_row - curr_row) ** 2))
                    cost += euclidean_distance

                curr_column += 1
                correct_val += 1
            
            curr_row += 1
            curr_column = 0
            
        return cost'''
    
    def _euclidean_distance_heuristic(game_board):
        cost = 0
        curr_row = 0
        curr_column = 0
        dimensionality = len(game_board.get_board()[0])
        correct_val = 1 #meant to indicate what the correct tile at that location in the grid is
        for row in game_board.get_board():
            for tile in row:
                if(correct_val != game_board[row][tile]):
                    goal_row = correct_val / dimensionality
                    goal_column = (correct_val % dimensionality) - 1

                    euclidean_distance = math.sqrt(((goal_column - curr_column) ** 2) + ((goal_row - curr_row) ** 2))
                    cost += euclidean_distance
                    curr_column += 1

                correct_val += 1
                curr_row += 1
                curr_column = 0
        return cost


