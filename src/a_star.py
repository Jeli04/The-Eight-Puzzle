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
            
            
            node = pair[1]  # contains the actual node object 
            curr_node_cost = node.cost    # contrains the numerical cost from start to curr (g value)

            # calculate the g(n) + h(n) cost
            node.totalCost = node.cost + node.heuristic

            # check if node is a goal state 
            print("check before solution: ", node.n_puzzle)
            print("goal state: ", puzzle.goalState)
            print(puzzle.isGoal(node))
            if puzzle.isGoal(node):
                return puzzle.seen
            
            # add into explored list 
            puzzle.seen[puzzle.toString(node)] = node

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
                child_cost = child.parent.cost
                            
                seen = False

                # update child node if smaller cost     
                puzzleString = puzzle.toString(child)
                if seen == False and puzzleString in puzzle.seen and child_cost < curr_node_cost:
                    seen = True
                    seenNode = puzzle.seen[puzzleString]
                    seenNode.cost = child_cost
                    seenNode.parent = node
                    heapq.heappush(puzzle.frontier, ((child_cost + self.heuristic_cost(heuristic_type, child)), seenNode))
                    print("Before delete ", len(puzzle.seen))
                    del puzzle.seen[puzzleString]
                    print("After delete ", len(puzzle.seen))
                else:
                    for pair in puzzle.frontier:
                        # if len(puzzle.frontier) > 5: return
                        if np.array_equal(pair[1].n_puzzle, child.n_puzzle):
                            seen = True
                            if child_cost < curr_node_cost:
                                pair[1].cost = child_cost
                                pair[1].parent = node
                                break

                # update child node if smaller cost     
                # if seen == False:
                #     for n in puzzle.seen:
                #         # if len(puzzle.frontier) > 3: return
                #         print(np.array_equal(n.n_puzzle, child.n_puzzle))
                #         print(n.n_puzzle)
                #         print(child.n_puzzle)
                #         if np.array_equal(n.n_puzzle, child.n_puzzle):
                #             seen = True
                #             if child_cost < curr_node_cost:
                #                 print("REACHED")
                #                 n.cost = child_cost
                #                 n.parent = node
                #                 heapq.heappush(puzzle.frontier, ((child_cost + self.heuristic_cost(heuristic_type, child)), n))
                #                 break

                # add into frontier if never seen yet
                if seen == False:
                    # print("push into heap")
                    # print(puzzle.frontier)
                    child.cost = child_cost
                    child.heuristic = self.heuristic_cost(heuristic_type, child)             
                    heapq.heappush(puzzle.frontier, (child.cost + child.heuristic, child))

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
                if child_node.n_puzzle[i,j] != tracker:
                    cost += 1
                tracker+=1

        return cost

    """
        Function: return the heuristic cost with euclidean distance for each tile
        Parameters: A possible child node
        Return: Heuristic cost of child node
    """
    def _euclidean_distance_heuristic(child_node):

        cost = 0
        curr_row = 0
        curr_column = 0
        dimensionality = len(child_node.n_puzzle[0])
        correct_val = 1 #meant to indicate what the correct tile at that location in the grid is
        for row in child_node.n_puzzle:
            for tile in row:
                if(correct_val != child_node[row][tile]):
                    goal_row = correct_val / dimensionality
                    goal_column = (correct_val % dimensionality) - 1

                    euclidean_distance = math.sqrt(((goal_column - curr_column) ** 2) + ((goal_row - curr_row) ** 2))
                    cost += euclidean_distance
                    curr_column += 1

                correct_val += 1
                curr_row += 1
                curr_column = 0
        return cost

