import math

class a_star:
    def __init__(self) -> None:
        # DELETE LATER not sets since we cant hash objects 
        self.frontier = []  # should sort by ascending f cost
        self.explored = []

    '''
        Function: calls A* with a heuristic
        Parameters: the intial game board, and the heuristic name as a string
        Return: Intial state if no solution, A child node if solution exists 
    '''
    def call_a_star(self, initial_game_board, heuristic_type):
        self.frontier.append((initial_game_board, 0))
        while self.frontier.empty()!= True:
            pair = self.frontier.pop(0)
            node = pair[0]  # contains the actual object 
            curr_node_cost = pair[1]    # contrains the numerical cost from start to curr

            # calculate the g(n) + h(n) cost
            node.totalCost = node.cost + node.heuristic

            # check if node is a goal state 
            if node.is_goal():
                return self.explored
            
            # add into explored list 
            self.explored.append(pair)

            # check each child node created by possible actions
            for action in node.get_actions():
                # spawn the child node based on the action
                child = None
                if action == "right":
                    child = node.go_right()
                elif action == "left":
                    child = node.go_left()
                elif action == "top":
                    child = node.go_top()
                elif action == "bottom":
                    child = node.go_bottom()

                # calculate the child node g value
                child_cost = (child.parent.cost + 1) 

                seen = False
                for pair in self.frontier:
                    if pair[0].get_board() == child.get_board():
                        seen = True
                        if child_cost < curr_node_cost:
                            pair[0].cost = child_cost
                            pair[0].parent = node

                # update child node if smaller cost     
                for n in self.explored:
                    if n.get_board() == child.get_board():
                        seen = True
                        if child_cost < curr_node_cost:
                            n.cost = child_cost
                            n.parent = node
                            self.frontier.append((n, child_cost + self.heuristic_cost(heuristic_type, child)))

                # add into frontier if never seen yet
                if seen == False:
                    child.cost = child_cost
                    child.heuristic = self.heuristic_cost(heuristic_type, child)             
                    self.frontier.append((child, child.cost + child.heuristic))

            self.explored.append(node)

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
        for row in child_node.get_board():
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
        dimensionality = len(child_node.get_board()[0])
        correct_val = 1 #meant to indicate what the correct tile at that location in the grid is
        for row in child_node.get_board():
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

