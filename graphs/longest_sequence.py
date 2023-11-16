class Solution:
    def custom_optimal(self, nums):
        cmap = {}
        for num in nums:
            cmap[num] = [num -1, num + 1, False]
        
        max_sequence = 0
        for key, values in cmap.items():
            sequence = 0
            if not values[2]:
                cmap[key][2] = True
                stack = [key]
                while stack:
                    sequence += 1
                    cur = stack.pop()
                    for child in cmap[cur][:2]:
                        if child in cmap and not cmap[child][2]:
                            stack.append(child)
                            cmap[child][2] = True
            max_sequence = max(sequence, max_sequence)
                
        return max_sequence

    def leetcode_optimal(self, nums):
        num_set = set(nums)
        max_sequence = 0
        for num in num_set:
            sequence = 0
            if num - 1 not in num_set:
                sequence += 1
                next_sequence = num + 1
                while next_sequence in num_set:
                    next_sequence += 1
                    sequence += 1
                max_sequence = max(sequence, max_sequence)
                
        return max_sequence

from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)