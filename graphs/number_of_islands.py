from collections import deque
class Solution:
    # Time/Space O(n*m), n*m for grid search, n*m for seen matrix. It can be 
    def bfs_do_not_modify_input(self, grid):
        y, x = len(grid), len(grid[0])
        seen = [[False for _ in range(x)] for _ in range(y)]
        deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        islands = 0
        for row in range(y):
            for col in range(x):
                queue = deque()
                if grid[row][col] == "1" and not seen[row][col]:
                    seen[row][col] = True
                    queue.append((row, col))
                    islands += 1
                    
                    while queue:
                        temp_row, temp_col = queue.popleft()
                        for dr, dc in deltas:
                            new_row, new_col = temp_row + dr, temp_col + dc
                            if 0 <= new_row < y and 0 <= new_col < x and grid[new_row][new_col] == "1" and not seen[new_row][new_col]:
                                seen[new_row][new_col] = True
                                queue.append((new_row, new_col))
        return islands

    # time/space O(n*m), O(min(n, m)) The space is hard to see. If everything is a land, then the queue can only get as large as 
    # the smallest dimension, think of a 3x100
    def bfs_modify_input(self, grid):
        y, x = len(grid), len(grid[0])
        deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        islands = 0
        for row in range(y):
            for col in range(x):
                queue = deque()
                if grid[row][col] == "1":
                    
                    grid[row][col] = "0"
                    queue.append((row, col))
                    islands += 1
                    
                    while queue:
                        temp_row, temp_col = queue.popleft()
                        for dr, dc in deltas:
                            new_row, new_col = temp_row + dr, temp_col + dc
                            if 0 <= new_row < y and 0 <= new_col < x and grid[new_row][new_col] == "1":
                                grid[new_row][new_col] = "0"
                                queue.append((new_row, new_col))
        return islands


from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)