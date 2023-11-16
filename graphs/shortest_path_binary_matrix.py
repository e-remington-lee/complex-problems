'''
You should always discuss the possibility of overwriting the input with your interviewer and clarify what kind of 
environment your algorithm is expected to run in. Sometimes they won't care, sometimes they'll state it has to run in 
a multithreaded environment, or sometimes they'll have a particular preference as it impacts what they're trying to see from you.
'''
from collections import deque
class Solution:
    def overwrite_input(self, grid):
        self.grid = grid
        self.n = len(self.grid)
        if self.grid[0][0] != 0 or self.grid[self.n  - 1][self.n - 1] != 0:
            return -1     
        
        self.directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        queue = [(0,0)]
        self.grid[0][0] = 1
        
        while queue:
            row, col = queue.pop(0)
            distance = self.grid[row][col]
            if row == self.n  - 1 and col == self.n - 1:
                return distance
            else:
                for adj_row, adj_col in self.get_valid_neighbors(row, col):
                    self.grid[adj_row][adj_col] = distance + 1
                    queue.append((adj_row, adj_col))
        return -1
    
    def get_valid_neighbors(self, row, col):
        for dr, dc in self.directions:
            new_row = row + dr
            new_col = col + dc
            if not (0 <= new_row <= self.n - 1 and 0 <= new_col <= self.n - 1):
                continue
            if self.grid[new_row][new_col] == 0:
                yield (new_row, new_col)


    def dont_modify_input(self, grid):
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Check that the first and last cells are open. 
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        # Set up the BFS.
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        current_distance = 1
        
        # Do the BFS.
        while queue:
            # Process all nodes at current_distance from the top-left cell.
            nodes_of_current_distance = len(queue)
            for _ in range(nodes_of_current_distance):
                row, col = queue.popleft()
                if (row, col) == (max_row, max_col):
                    return current_distance
                for neighbour in get_neighbours(row, col):
                    if neighbour in visited:
                        continue
                    visited.add(neighbour)
                    queue.append(neighbour)
            # We'll now be processing all nodes at current_distance + 1
            current_distance += 1
                    
        # There was no path.
        return -1 
    

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
                
nums = [1,2,3,4,5,6]
def generate(nums):
    for x in nums:
        if x % 2 == 0:
            yield x

for x in generate(nums):
    print(x)


# print(10%4)