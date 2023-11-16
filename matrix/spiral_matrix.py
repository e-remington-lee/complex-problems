class Solution:
    def spiralOrder(self, matrix):
        response = []
        state = Direction()
        left, up = 0, 0
        rows, cols = len(matrix), len(matrix[0])
        down = rows - 1
        right = cols - 1
        
        while len(response) < rows * cols:
            if state.direction == "right":
                for i in range(left, right + 1):
                    response.append(matrix[up][i])
                up += 1
                state.transition()   
            elif state.direction == "down":
                for i in range(up, down + 1):
                    response.append(matrix[i][right])
                right -= 1
                state.transition()
            
            elif state.direction == "left":
                for i in range(right, left - 1, -1):
                    response.append(matrix[down][i])
                down -= 1
                state.transition()
            
            elif state.direction == "up":
                for i in range(down, up - 1, -1):
                    response.append(matrix[i][left])
                left += 1
                state.transition()
        return response
                        
        
class Direction:
    def __init__(self):
        self.direction = "right"
    
    def get_direction(self):
        return self.direction
    
    def transition(self):
        if self.direction == "right":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "left"
        elif self.direction =="left":
            self.direction = "up"
        elif self.direction == "up":
            self.direction = "right"

class Solution:
    def spiralOrder(self, matrix):
        response = []
        right, left, up, down = Direction("right"), Direction("left"), Direction("up"), Direction("down")
        right.next, left.next, up.next, down.next = down, up, right, left
        state = StateMachine(right)
        left, up = 0, 0
        rows, cols = len(matrix), len(matrix[0])
        down = rows - 1
        right = cols - 1
        
        while len(response) < rows * cols:
            if state.state.direction == "right":
                for i in range(left, right + 1):
                    response.append(matrix[up][i])
                up += 1
                state.transition()   
            elif state.state.direction == "down":
                for i in range(up, down + 1):
                    response.append(matrix[i][right])
                right -= 1
                state.transition()
            
            elif state.state.direction == "left":
                for i in range(right, left - 1, -1):
                    response.append(matrix[down][i])
                down -= 1
                state.transition()
            
            elif state.state.direction == "up":
                for i in range(down, up - 1, -1):
                    response.append(matrix[i][left])
                left += 1
                state.transition()
        return response
                          
class StateMachine:
    def __init__(self, state):
        self.state = state
    
    def get_direction(self):
        return self.state.direction
    
    def transition(self):
        self.state = self.state.next
            
class Direction:
    def __init__(self, direction):
        self.direction = direction
        self.next = None    
            

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)