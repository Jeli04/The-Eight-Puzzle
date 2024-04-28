class a_star:
    def __init__(self) -> None:
        pass

    def call_misplaced_tile(game_board):
        # calls call_a_starwith the misplaced_tile_heuristic
        pass

    def call_euclidean_distance(game_board):
        # calls call_a_starwith the euclidean_distance_heuristic
        pass

    def call_a_star(game_board, heuristic):
        pass

    def _misplaced_tile_heuristic(game_board):
        pass

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

