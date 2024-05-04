import math
import heapq
from n_puzzle import Node
from n_puzzle import puzzleProblem

class uniform_cost_search:
    def execute_ucs(self, game):
        
        heapq.heappush(game.frontier, (0, game))
        
        while game.frontier:
            pair = heapq.heappop(game.frontier)
            # print("hellooooo")
            # print(pair[0])
            # print(pair[1].root.printPuzzle())
            cur_cost = pair[0]
            puzzle = pair[1] # we actually want current!
            
            # return current state if goal is found
            if puzzle.isGoal():
                print("fgfv")
                return puzzle
            else:
                print("im not the goal!!!!!")
       
            # mark current node as visited
            game.seen.add(pair)
            
            # obtain child node from all 4 possible operators
            for action in puzzle.expandNode(puzzle.root):
                child = None
                current = puzzle.root
                
                if action == "right":
                    print("right")
                    child = puzzle.operator_go_right(current)
                elif action == "left":
                    child = puzzle.operator_go_left(current)
                    print("left")
                elif action == "up":
                    child = puzzle.operator_go_top(current)
                    print("up")
                elif action == "down":
                    child = puzzle.operator_go_bottom(current)
                    print("down")
            
                # calculate the child node cost (delete later)
                # child_cost = child.parent.cost + 1 //already in n_puzzle
                
                visited = False
                
                #get child cost (child.cost) to use below
               
                
                # update child node if smaller cost is found
                for pair in game.frontier:
                    if pair[1].get_board() == child.get_board():
                        visited = True
                        
                        if child_cost < cur_cost:
                            pair[1].cost = child_cost
                            pair[1].parent = node
                
                for item in game.seen:
                    if item.get_board() == child.get_board():
                        visited = True
                        
                        if child_cost < cur_cost:
                            item.cost = child_cost
                            item.parent = node
                            game.frontier.heappush((child_cost, item))
                
                # add into frontier if never seen yet
                if visited == False:
                    child.cost = child_cost
                    game.frontier.heappush((child_cost, child))
                
            game.seen.append(node)
        
        return None
    