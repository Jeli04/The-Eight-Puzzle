import numpy as np

class Node:
    #Constructor for puzzle node
    def __init__(self, dim = 3, n_puzzle = None) -> None:
        if dim == 3 and n_puzzle == None or dim > 3 and n_puzzle == None:
            self.dim = dim
            self.n_puzzle = np.arange(self.dim * self.dim)
            np.random.shuffle(self.n_puzzle)
            self.n_puzzle = np.asmatrix(self.n_puzzle).reshape(self.dim, self.dim)
        elif dim > 3 and n_puzzle != None:
            self.dim = dim
            self.n_puzzle = n_puzzle
        elif dim < 3:
            raise ValueError("n_puzzle dimensions must be greater than 2")
        
        self.parent = None
        self.heuristic = 0
        self.cost = 0 
        self.totalCost = self.heuristic + self.cost
        
            
    ##Prints the puzzle at the current state
    def printPuzzle(self):
        print(self.n_puzzle)

    ##Gets the index of the "blank" (for us 0) puzzle piece
    def getInitialStateIndex(self):
        return [[int(item) for array in np.where(self.n_puzzle == 0) for item in array.flatten()][1], [int(item) for array in np.where(self.n_puzzle == 0) for item in array.flatten()][0]] if np.where(self.n_puzzle == 0) else ValueError("Misconfigured puzzle")
        #I know this is bad, you don't have to tell me



class puzzleProblem:
    #contains the details of the problem
    #initialize frontier with the first initial state node
    def __init__(self, initialState, dim) -> None:
        #the puzzle should know its initial and goal states
        self.initialState = Node(initialState)
        self.dim = dim
        self.goalState = self.createGoalState(dim)
        self.frontier = {}
        # a list of visited nodes 
        self.seen = {}
   

    def expandNode(node):
        #this function will figure out a list of all the valid next states that we can get
        # and order them by cost to add into frontier
        pass
    def isGoal(node):
        #compare node to goal
        pass
    def createGoalState(self, dim):
    #make a goal state n puzzle based on dimension.
        self.goalState = 2 # this is not implemented yet....!
        pass
