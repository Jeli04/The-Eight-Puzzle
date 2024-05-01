import math
import heapq
from n_puzzle import Node
from n_puzzle import puzzleProblem

class uniform_cost_search:
    def execute_ucs(initial_game_board):
        frontier.heappush((0, initial_game_board))
        
        while frontier.empty() != True:
            pair = frontier.heappop
            cur_cost = pair[0]
            node = pair[1]
        
            # return current state if goal is found
            if node.is_goal():
                return node
       
            # mark current node as visited
            seen.append(pair)
            
            # obtain child node from all 4 possible operators
            for action in node.get_actions():
                child = None
                
                if action == "right":
                    child = node.go_right()
                elif action == "left":
                    child = node.go_left()
                elif action == "top":
                    child = node.go_top()
                elif action == "bottom":
                    child = node.go_bottom()
            
                # calculate the child node cost (delete later)
                child_cost = child.parent.cost + 1
                
                seen = False
                
                # update child node if smaller cost is found
                for pair in frontier:
                    if pair[1].get_board() == child.get_board():
                        seen = True
                        
                        if child_cost < cur_cost:
                            pair[1].cost = child_cost
                            pair[1].parent = node
                
                for item in seen:
                    if item.get_board() == child.get_board():
                        seen = True
                        
                        if child_cost < cur_cost:
                            item.cost = child_cost
                            item.parent = node
                            frontier.heappush((child_cost, item))
                
                # add into frontier if never seen yet
                if seen == False:
                    child.cost = child_cost
                    frontier.heappush((child_cost, child))
                
            seen.append(node)
        
        return None