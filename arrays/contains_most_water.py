class Solution:
    def maxArea(self, height):
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            h_left, h_right = height[left], height[right]
            _min = min(h_left, h_right)
            max_area = max(max_area, _min * (right - left))
            if h_left < h_right:
                left += 1
            else:
                right -= 1
            '''
you do not need "smart next step calculations" outside of the current left/right
19, 600, 0, 0, 31, 19
if at 19/19 they are equal, and you go to 31 instead of 600, you only go off the min value, 19, then
you would move left up 1 and youd be at the same spot as before

19, 600, 0, 500, 0, 19
if you default and move right down 1, youll get 0, then move down to 500, which will lead to go from 19 to 600

the thing that may not be obvious is when you increment left/right, you might think there is an edge case that
if you don't increment properly it will fail. The good thing is bc it checks each iteration whether to go right or left, you will
eventually get to the best area even if you just check the current level
            '''
            # elif h_right < h_left:
            #     right -= 1
            # else:
            #     sub_left, sub_right = left + 1, right - 1
            #     if sub_left < sub_right:
            #         sub_h_left, sub_h_right = height[sub_left], height[sub_right]
            #         if sub_h_left < sub_h_right:
            #             right -= 1
            #         else:
            #             left += 1
            #     else:
            #         left += 1
        return max_area

from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)