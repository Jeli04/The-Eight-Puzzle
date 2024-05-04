import math
import heapq
from n_puzzle import Node
from n_puzzle import puzzleProblem

class uniform_cost_search:
    def execute_ucs(self, game):
        
        heapq.heappush(game.frontier, (0, game.root))
        
        while game.frontier:
            pair = heapq.heappop(game.frontier)
            node = pair[1] # we actually want current!
            cur_cost = node.cost
            
            # return current state if goal is found
            if game.isGoal():
                return game.seen
       
            # mark current node as visited
            game.seen.append(node)
            
            # obtain child node from all 4 possible operators
            for action in game.expandNode(node):
                child = None
                
                if action == "right":
                    print("right")
                    child = game.operator_go_right(node)
                elif action == "left":
                    child = game.operator_go_left(node)
                    print("left")
                elif action == "up":
                    child = game.operator_go_up(node)
                    print("up")
                elif action == "down":
                    child = game.operator_go_down(node)
                    print("down")
            
                # calculate the child node cost (delete later)
                # child_cost = child.parent.cost + 1 //already in n_puzzle
                
                child_cost = child.parent.cost
                visited = False
                
                #get child cost (child.cost) to use below
               
                
                # update child node if smaller cost is found
                for pair in game.frontier:
                    if (pair[1].n_puzzle == child.n_puzzle).all():
                        visited = True
                        
                        if child_cost < cur_cost:
                            pair[1].cost = child_cost
                            pair[1].parent = node
                
                if visited == False:
                    for item in game.seen:
                        if (item.n_puzzle == child.n_puzzle).all():
                            visited = True
                            
                            if child_cost < cur_cost:
                                item.cost = child_cost
                                item.parent = node
                                heapq.heappush(game.frontier, (child_cost, item))
                
                # add into frontier if never seen yet
                if visited == False:
                    child.cost = child_cost
                    heapq.heappush(game.frontier, (child_cost, item))
                
            game.seen.append(node)
        
        return None
    