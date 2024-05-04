import math

class a_star:
    # def __init__(self) -> None:
    #     self.frontier = []
    #     self.explored = []


    '''
        Function: calls A* with a heuristic
        Parameters: the intial game board, and the heuristic name as a string
        Return: Intial state if no solution, A child node if solution exists 
    '''
    def call_a_star(self, game, heuristic):
        game.frontier.append((game, 0))
        while game.frontier.empty()!= True:
            pair = game.frontier.pop(0)
            node = pair[0]
            curr_node_cost = pair[1]

            # check if node is a goal state 
            if node.is_goal():
                return node
            
            # add into explored list 
            game.seen.append(pair)

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
                if heuristic == "misplaced": heuristic_cost = game._misplaced_tile_heuristic(child)
                if heuristic == "euclidean": heuristic_cost = game._euclidean_distance_heuristic(child)
                child_cost = node.start_to_curr_cost + heuristic_cost

                # add into frontier if never seen yet
                if child not in game.frontier or child not in game.seen:
                    game.frontier.append((child, heuristic_cost))

                # update child node if smaller cost
                elif child_cost < curr_node_cost and child in game.seen:
                    child.start_to_curr_cost = child_cost
                    child.parent = node
                    # remove the child node from explored 

                elif child_cost < curr_node_cost and child in game.frontier:
                    child.start_to_curr_cost = child_cost
                    child.parent = node

            game.seen.append((node, curr_node_cost))


        return game
        
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

