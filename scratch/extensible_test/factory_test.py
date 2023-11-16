class Direction:
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"
    
    
class AntMovement:
    def __init__(self, board, start_row, start_column):
        self.direction = Direction.NORTH
        self.board = board
        self.current_row = start_row
        self.current_col = start_column
        self.response = [f'{start_row},{start_column}']
        
    def __read_action(self, action):
        if action == "rotate":
            self.__rotate_ant()
        elif action == "flip":
            self.__flip_board()
        else:
            self.__move()
            
    def __rotate_ant(self):
        print("rotate ant")
        print(self.board[self.current_row][self.current_col])
        
        if self.board[self.current_row][self.current_col]:
            if self.direction == Direction.NORTH:
                self.direction = Direction.EAST
            elif self.direction == Direction.EAST:
                self.direction = Direction.SOUTH
            elif self.direction == Direction.SOUTH:
                self.direction = Direction.WEST
            elif self.direction == Direction.WEST:
                self.direction = Direction.NORTH
        else:
            if self.direction == Direction.NORTH:
                self.direction = Direction.WEST
            elif self.direction == Direction.WEST:
                self.direction = Direction.SOUTH
            elif self.direction == Direction.SOUTH:
                self.direction = Direction.EAST
            elif self.direction == Direction.EAST:
                self.direction = Direction.NORTH
        print(self.direction)
                
    def __flip_board(self):
        print("flip board")
        print(self.board[self.current_col][self.current_row])
        if self.board[self.current_col][self.current_row] == True:
            self.board[self.current_col][self.current_row] = False
        else:
            self.board[self.current_col][self.current_row] = True
            
        print(self.board[self.current_col][self.current_row])

    def __move(self):
        if self.direction == Direction.NORTH:
            self.current_row -= 1
        elif self.direction == Direction.EAST:
            self.current_col += 1
        elif self.direction == Direction.SOUTH:
            self.current_row += 1
        elif self.direction == Direction.WEST:
            self.current_col -= 1
        self.response.append(f'{self.current_row},{self.current_col}')
            
    def read_action_list(self, actions):
        for action in actions:
            self.__read_action(action)
        return "|".join(self.response)
        
        
def simulate(board, start_row, start_column, actions):
    antMovement = AntMovement(board, start_row, start_column)
    return antMovement.read_action_list(actions)

b = [[True, True],
    [True, True]]
a = ["flip", "rotate", "move"]

# print(simulate(b, 0, 1, a))

x = "abcd"
x[0] = "d"
print(x)