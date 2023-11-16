from collections import deque
class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        flood_color = image[sr][sc]
        
        if flood_color == newColor:
            return image
        
        queue = deque()
        queue.append((sr, sc))
        image[sr][sc] = newColor

        while queue:
            row, col = queue.popleft()    
            for dr, dc in deltas:
                new_row = row + dr
                new_col = col + dc
                if 0 <= new_row < len(image) and 0 <= new_col < len(image[0]):
                    if image[new_row][new_col] == flood_color:
                        queue.append((new_row, new_col))
                        image[new_row][new_col] = newColor
                    
        return image


from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard) 