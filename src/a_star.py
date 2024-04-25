class a_star:
    def __init__(self) -> None:
        self.frontier = []
        self.explored = []


    '''
        Function: calls A* with a heuristic
        Parameters: the intial game board, and the heuristic name as a string
        Return: Intial state if no solution, A child node if solution exists 
    '''
    def call_a_star(self, initial_game_board, heuristic):
        self.frontier.append((initial_game_board, 0))
        while self.frontier.empty()!= True:
            pair = self.frontier.pop()
            node = pair[0]
            curr_node_cost = pair[1]

            # check if node is a goal state 
            if node.is_goal():
                return node
            
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

                # calculate the g(n) + h(n) cost
                heuristic_cost = 0
                if heuristic == "misplaced": heuristic_cost = self._misplaced_tile_heuristic(child)
                if heuristic == "euclidean": heuristic_cost = self._euclidean_distance_heuristic(child)
                child_cost = node.start_to_curr_cost + heuristic_cost

                # add into frontier if never seen yet
                if child not in self.frontier or child not in self.explored:
                    self.frontier.append((child, heuristic_cost))

                # update child node if smaller cost
                elif child_cost < curr_node_cost and child in self.explored:
                    child.start_to_curr_cost = child_cost
                    child.parent = node
                    # remove the child node from explored 

                elif child_cost < curr_node_cost and child in self.frontier:
                    child.start_to_curr_cost = child_cost
                    child.parent = node

            self.explored.append((node, curr_node_cost))


        return initial_game_board
        
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

    def _euclidean_distance_heuristic(self, game_board):
        pass

