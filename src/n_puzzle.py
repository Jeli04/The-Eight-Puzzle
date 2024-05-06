import numpy as np
import heapq
import copy

class Node:
    #Constructor for puzzle node
    def __init__(self, dim = 3, n_puzzle = None, parent = None) -> None:
        if dim == 3 and n_puzzle is None or dim > 3:
            self.dim = dim
            self.n_puzzle = np.arange(self.dim * self.dim)
            np.random.shuffle(self.n_puzzle)

            #Checks to see if the given puzzle is solvable
            while (self.Solvable() == False):
                print("This is invalid puzzle, generating a valid one.")
                self.n_puzzle = np.arange(self.dim * self.dim)
                np.random.shuffle(self.n_puzzle)

            #Sets array to matrix type
            self.n_puzzle = np.asmatrix(self.n_puzzle.reshape(self.dim, self.dim))

        elif n_puzzle is not None and dim >= 3:
            self.dim = dim
            self.n_puzzle = n_puzzle
        elif dim < 3:
            raise ValueError("n_puzzle dimensions must be greater than 2")
        else:
            pass
        
        self.parent = parent #For A* star algorithm to keep trace of past heuristic values
        self.heuristic = 0
        self.cost = 0 
        self.totalCost = self.heuristic + self.cost  

    def Solvable(self) -> bool:
        inversions = 0

        #flattening matrix into a list and removing the blank
        flatten_board = self.n_puzzle.flatten()
        flatten_board = flatten_board[flatten_board != 0]
        total_size = len(flatten_board)

        #finding the amount of inversions
        for i in range(total_size):
            for j in range(i + 1, total_size):
                if flatten_board[i] > flatten_board[j]:
                    inversions += 1

    
        if(((self.dim) % 2) == 1) and ((inversions % 2) == 0):
            return True
        
        if((((self.dim) % 2) == 0) and (((self.getInitialStateIndex()[0]) % 2) == 0) and ((inversions % 2) == 1)):
            return True
        
        if((((self.dim) % 2) == 0) and (((self.getInitialStateIndex()[0]) % 2) == 1) and ((inversions % 2) == 0)):
            return True
        
        return False
    

    def __lt__(self, other) -> bool:
        # Compare based on total cost as the primary criterion
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    # Optionally, implement other comparison methods
    def __eq__(self, other) -> bool:
        return (self.cost + self.heuristic) == (other.cost + other.heuristic) 
            
    ##Prints the puzzle at the current state
    def printPuzzle(self):
        print(self.n_puzzle)

    ##Gets the index of the "blank" (for us 0) puzzle piece
    def getInitialStateIndex(self) -> list[int]:
        return [np.where(self.n_puzzle == 0)[0][0], np.where(self.n_puzzle == 0)[1][0]]




class puzzleProblem:
    #contains the details of the problem
    #initialize frontier with the first initial state node
    def __init__(self, root) -> None:
        #the puzzle should know its initial and goal states
        self.root = root
        self.goalState = self.createGoalState(root.dim)
        self.frontier = []
        # a list of visited nodes 
        self.seen = {}
        self.numOfExpandedNodes = 0
        self.maxQueueSize = 0
  
    #Creates frontier of nodes (i.e. computes node expansions)
    def expandNode(self,node):

        # this function will figure out a list of all the valid next states that we can get
        dimension= node.dim
        listOfActions = []
        index = node.getInitialStateIndex()

        if index[1]!=(dimension-1):
            #if not right most column, you can go right
            listOfActions.append("right")
        if index[1]!=0:
            #if not leftmost col, you can go left
            listOfActions.append("left")
        if index[0]!=0:
            #if not topmost row, you can go up
            listOfActions.append("up")
        if index[0]!=(dimension-1):
            #if not bottommost row, you can go down
            listOfActions.append("down")

        return listOfActions

    # returns the numbers in the puzzle as a string
    def toString(self, node):
        return ''.join(str(n) for row in node.n_puzzle.tolist() for n in row)

    # Checks whether the current puzzle 
    def isGoal(self, node) -> bool:
        return np.array_equal(node.n_puzzle, self.goalState)

    def createGoalState(self, dim) -> np.matrix:
        matrix = np.arange(dim * dim).reshape(dim, dim)
        matrix += 1
        matrix[dim - 1, dim - 1] = 0
        return np.asmatrix(matrix)
    
    def printGoalState(self):
        print(self.goalState)

    #Operators to change 0 -> left of the matrix
    def operator_go_left(self, currNode) -> Node:
        new_node = copy.deepcopy(currNode)

        access_node = currNode

        currIndex_col = new_node.getInitialStateIndex()[0]
        currIndex_row = new_node.getInitialStateIndex()[1]

        new_node.n_puzzle[currIndex_col, currIndex_row], new_node.n_puzzle[currIndex_col, currIndex_row - 1] = new_node.n_puzzle[currIndex_col, currIndex_row - 1], new_node.n_puzzle[currIndex_col, currIndex_row]
        new_node.parent = access_node

        new_node.cost += 1

        # print(f'After left operation:\n{new_node.n_puzzle}')

        # print("currNode:", currNode)
        # print("deep copy:", new_node)
        return new_node

            
    #Moves 0 -> right in the matrix
    def operator_go_right(self, currNode) -> Node:
        new_node = copy.deepcopy(currNode)
        access_node = currNode

        currIndex_col = new_node.getInitialStateIndex()[0]
        currIndex_row = new_node.getInitialStateIndex()[1]

        new_node.n_puzzle[currIndex_col, currIndex_row], new_node.n_puzzle[currIndex_col, currIndex_row + 1] = new_node.n_puzzle[currIndex_col, currIndex_row + 1], new_node.n_puzzle[currIndex_col, currIndex_row]
        new_node.parent = access_node

        new_node.cost += 1

        return new_node
    
    #Moves 0 -> upwards in the matrix
    def operator_go_up(self, currNode) -> Node:
        new_node = copy.deepcopy(currNode)
        access_node = currNode

        currIndex_col = currNode.getInitialStateIndex()[0]
        currIndex_row = currNode.getInitialStateIndex()[1]

        new_node.n_puzzle[currIndex_col, currIndex_row], new_node.n_puzzle[currIndex_col - 1, currIndex_row] = new_node.n_puzzle[currIndex_col - 1, currIndex_row], new_node.n_puzzle[currIndex_col, currIndex_row]
        new_node.parent = access_node

        new_node.cost += 1

        return new_node
    
    #Moves 0 -> downwards in the matrix
    def operator_go_down(self, currNode) -> Node:
        new_node = copy.deepcopy(currNode)
        access_node = currNode

        currIndex_col = new_node.getInitialStateIndex()[0]
        currIndex_row = new_node.getInitialStateIndex()[1]

        new_node.n_puzzle[currIndex_col, currIndex_row], new_node.n_puzzle[currIndex_col + 1, currIndex_row] = new_node.n_puzzle[currIndex_col + 1, currIndex_row], new_node.n_puzzle[currIndex_col, currIndex_row]
        new_node.parent = access_node

        new_node.cost += 1

        return new_node
