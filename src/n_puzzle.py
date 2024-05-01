import numpy as np
import heapq

class Node:
    #Constructor for puzzle node
    def __init__(self, dim = 3, n_puzzle = None) -> None:
        if dim == 3 and n_puzzle == None or dim > 3 and n_puzzle == None:
            self.dim = dim
            self.n_puzzle = np.arange(self.dim * self.dim)
            np.random.shuffle(self.n_puzzle)
            self.n_puzzle = np.asmatrix(self.n_puzzle).reshape(self.dim, self.dim)
        elif dim >= 3 and n_puzzle != None:
            self.dim = dim
            self.n_puzzle = n_puzzle
        elif dim < 3:
            raise ValueError("n_puzzle dimensions must be greater than 2")
        
        self.parent = None #For A* star algorithm to keep trace of past heuristic values
        self.heuristic = 0
        self.cost = 0 
        self.totalCost = self.heuristic + self.cost  
        #self.dim = dim 
            
    ##Prints the puzzle at the current state
    def printPuzzle(self):
        print(np.asmatrix(self.n_puzzle))

    ##Gets the index of the "blank" (for us 0) puzzle piece
    def getInitialStateIndex(self):
        return [[int(item) for array in np.where(self.n_puzzle == 0) for item in array.flatten()][1], [int(item) for array in np.where(self.n_puzzle == 0) for item in array.flatten()][0]] if np.where(self.n_puzzle == 0) else ValueError("Misconfigured puzzle")
        #I know this is bad, you don't have to tell me



class puzzleProblem:
    #contains the details of the problem
    #initialize frontier with the first initial state node
    def __init__(self, root) -> None:
        #the puzzle should know its initial and goal states
        self.root = root
        self.goalState = self.createGoalState(root.dim)
        self.frontier = []
        # a list of visited nodes 
        self.seen = []
        #self.dimension = root.dim
   

    def expandNode(self,node):
        # this function will figure out a list of all the valid next states that we can get
        # and order them by cost to add into frontier
        #n = Node(self.dimension, node)
        dimension= node.dim
        listOfActions = []
        index = node.getInitialStateIndex()
        print(type(index))
        print(index[0]) # is col number
        print(index[1]) # is row 
        if index[0]!=(dimension-1):
            #if not right most column, you can go right
            listOfActions.append("right")
        if index[0]!=0:
            #if not leftmost col, you can go left
            listOfActions.append("left")
        if index[1]!=0:
            #if not topmost row, you can go up
            listOfActions.append("up")
        if index[1]!=(dimension-1):
            #if not bottommost row, you can go down
            listOfActions.append("down")
        
        print(index)
        print(listOfActions)

    def isGoal(self) -> bool:
        return self.root == self.goalState

    def createGoalState(self, dim) -> np.matrix:
        return np.asmatrix(np.arange(dim * dim).reshape(dim, dim))
    
    def printGoalState(self):
        print(self.goalState)

    
    