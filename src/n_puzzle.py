import numpy as np

class n_puzzle:
    def __init__(self, dim, initState, goalState) -> None:
        self.dim = dim
        self.initState = initState #make these matrices later 
        self.goalState = goalState
    
class Node:
    def __init__(self, num, cost, heuristic):
        self.num = num  # Number of the tile
        self.cost = cost
        self.heuristic = heuristic
        self.parent = parent
         
       