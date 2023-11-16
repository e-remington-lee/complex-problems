class Solution:
    '''
    n^2 time
    '''
    def largestRectangleArea(self, heights):
        output = 0
        for i in range(len(heights)):
            minimum=heights[i]
            for j in range(i, len(heights)):
                current = heights[j]
                minimum = min(minimum, current)
                response = minimum*(j-i+1)
                output = max(output, response, current)
        return output

    '''
    n log N time
    '''
    def divide_conquer(self, heights):
        output = 0
        for i in range(len(heights)):
            minimum=heights[i]
            for j in range(i, len(heights)):
                current = heights[j]
                minimum = min(minimum, current)
                response = minimum*(j-i+1)
                output = max(output, response, current)
        return output

    '''
    linear time and space
    '''
    def optimal(self, heights):
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            stack.append(i)

        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)
        return max_area


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)