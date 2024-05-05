import numpy as np
import heapq
import copy

class Node:
    #Constructor for puzzle node
    def __init__(self, dim = 3, n_puzzle = None, parent = None) -> None:
        # self.n_puzzle = None
        if dim == 3 and n_puzzle is None or dim > 3 and n_puzzle is None:
            self.dim = dim
            self.n_puzzle = np.arange(self.dim * self.dim)
            np.random.shuffle(self.n_puzzle)
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
            
    ##Prints the puzzle at the current state
    def printPuzzle(self):
        print(self.n_puzzle)

    ##Gets the index of the "blank" (for us 0) puzzle piece
    def getInitialStateIndex(self):
        return [np.where(self.n_puzzle == 0)[0][0], np.where(self.n_puzzle == 0)[1][0]]
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
   
    def Solvable(self, node) -> bool:
        inversions = 0

        #flattening matrix into a list and removing the blank
        flatten_board = [val for row in node.n_puzzle for val in row if val != 0]
        total_size = len(flatten_board)

        #finding the amount of inversions
        for i in range(total_size):
            for j in range(i + 1, total_size):
                if flatten_board[i] > flatten_board[j]:
                    inversions += 1

        if(((node.dim) % 2) == 1) and ((inversions % 2) == 0):
            return True
        
        if((((node.dim) % 2) == 0) and (((node.getInitialStateIndex()[0]) % 2) == 1) and ((inversions % 2) == 1)):
            return True
        
        if((((node.dim) % 2) == 0) and (((node.getInitialStateIndex()[0]) % 2) == 0) and ((inversions % 2) == 0)):
            return True
        
        return False


                

    #Aditi & Jon: implement priority queue
    def expandNode(self,node):
        # this function will figure out a list of all the valid next states that we can get
        dimension= node.dim
        listOfActions = []
        index = node.getInitialStateIndex()
        #print(index[0]) # is row number
        #print(index[1]) # is col 
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

        # print(index)
        #print(listOfActions)
        return listOfActions

    def isGoal(self) -> bool:
        return np.array_equal(self.root.n_puzzle, self.goalState)

    def createGoalState(self, dim) -> np.matrix:
        matrix = np.arange(dim * dim).reshape(dim, dim)
        matrix += 1
        matrix[dim - 1, dim - 1] = 0
        return np.asmatrix(matrix)
    
    def printGoalState(self):
        print(self.goalState)

    #Operators to change 0 -> {some index} to achieve goal state (Vaneeeeesha)
    def operator_go_left(self, currNode):
        new_node = copy.deepcopy(currNode)
        access_node = currNode

        currIndex_col = new_node.getInitialStateIndex()[0]
        currIndex_row = new_node.getInitialStateIndex()[1]
        print(f'Before left operation:\n{new_node.n_puzzle}\n')

        new_node.n_puzzle[currIndex_col, currIndex_row], new_node.n_puzzle[currIndex_col, currIndex_row - 1] = new_node.n_puzzle[currIndex_col, currIndex_row - 1], new_node.n_puzzle[currIndex_col, currIndex_row]
        new_node.parent = access_node

        new_node.cost += 1

        print(f'After left operation:\n{new_node.n_puzzle}')

        return new_node

            
    
    def operator_go_right(self, currNode):
        new_node = copy.deepcopy(currNode)
        access_node = currNode

        currIndex_col = new_node.getInitialStateIndex()[0]
        currIndex_row = new_node.getInitialStateIndex()[1]
        print(f'Before right operation:\n{new_node.n_puzzle}\n')

        new_node.n_puzzle[currIndex_col, currIndex_row], new_node.n_puzzle[currIndex_col, currIndex_row + 1] = new_node.n_puzzle[currIndex_col, currIndex_row + 1], new_node.n_puzzle[currIndex_col, currIndex_row]
        new_node.parent = access_node

        new_node.cost += 1

        print(f'After right operation:\n{new_node.n_puzzle}')

        return new_node

    def operator_go_up(self, currNode):
        new_node = copy.deepcopy(currNode)
        access_node = currNode

        currIndex_col = currNode.getInitialStateIndex()[0]
        currIndex_row = currNode.getInitialStateIndex()[1]
        print(f'Before up operation:\n{new_node.n_puzzle}\n')

        new_node.n_puzzle[currIndex_col, currIndex_row], new_node.n_puzzle[currIndex_col - 1, currIndex_row] = new_node.n_puzzle[currIndex_col - 1, currIndex_row], new_node.n_puzzle[currIndex_col, currIndex_row]
        new_node.parent = access_node

        new_node.cost += 1

        print(f'After up operation:\n{new_node.n_puzzle}')

        return new_node

    def operator_go_down(self, currNode):
        new_node = copy.deepcopy(currNode)
        access_node = currNode

        currIndex_col = new_node.getInitialStateIndex()[0]
        currIndex_row = new_node.getInitialStateIndex()[1]
        print(f'Before down operation:\n{new_node.n_puzzle}\n')

        new_node.n_puzzle[currIndex_col, currIndex_row], new_node.n_puzzle[currIndex_col + 1, currIndex_row] = new_node.n_puzzle[currIndex_col + 1, currIndex_row], new_node.n_puzzle[currIndex_col, currIndex_row]
        new_node.parent = access_node

        new_node.cost += 1

        print(f'After down operation:\n{new_node.n_puzzle}')

        return new_node
    


puzzle = puzzleProblem(Node(4))

print(Node(4))

puzzle.printGoalState()

print(puzzle.isGoal())