import math
import heapq


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
            if puzzle.isGoal():
                return puzzle.seen
            
            # add into explored list 
            puzzle.seen.append(node)

            # check each child node created by possible actions
            for action in puzzle.expandNode(node):
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

                """
                    Might need to change if implmneted in N_puzzle
                """
                # calculate the child node g value
                child_cost = child.parent.cost

                seen = False
                for pair in puzzle.frontier:
                    if (pair[1].n_puzzle == child.n_puzzle).all():
                        seen = True
                        if child_cost < curr_node_cost:
                            pair[1].cost = child_cost
                            pair[1].parent = node

                # update child node if smaller cost     
                if seen == False:
                    for n in puzzle.seen:
                        if (n.n_puzzle == child.n_puzzle).all():
                            seen = True
                            if child_cost < curr_node_cost:
                                n.cost = child_cost
                                n.parent = node
                                heapq.heappush(puzzle.frontier, ((child_cost + self.heuristic_cost(heuristic_type, child)), n))
                
                # add into frontier if never seen yet
                if seen == False:
                    child.cost = child_cost
                    child.heuristic = self.heuristic_cost(heuristic_type, child)             
                    heapq.heappush(puzzle.frontier, ((child.cost + child.heuristic), n))

            puzzle.seen.append(node)

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
        i = 1
        for row in child_node.n_puzzle:
            for tile in row:
                if i != tile:
                    cost += 1
                i+=1
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

