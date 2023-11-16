class Solution:
    def threeSum_twoSum(self, nums):
        # response = []
        response = set()
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                self.two_sum(nums, response, i)
            
        return response
    
    def two_sum(self, nums, response, i):
        low, high = i + 1, len(nums) - 1
        while low < high:
            _sum = nums[i] + nums[low] + nums[high]
            if _sum < 0:
                low += 1
            elif _sum > 0:
                high -= 1
            else:
                li = [nums[i], nums[low], nums[high]]
                response.add(tuple(sorted(li)))
                low += 1
                high -= 1
                # response.append(li)
                # low += 1
                # high -= 1
                '''
                If you add a list instead of a set to response
                you need to do this bc if you choose to use a list, there is a chance to add duplicates if you have [-1, -1, -1, 0, 1, 2]
                you need to check backwards bc if you check forwards you can get a mistake with [-2,0,1,1,2], you get -2,0,2, but you 
                miss -2, 1, 1 since low == 2, high = 3, but low == low + 1
                '''
                # while low < high and nums[low] == nums[low - 1]:
                #     low += 1
 
    def threeSum_no_sort(self, nums):
        response = set()
        seen = {}
        for i, val1 in enumerate(nums):
            for j, val2 in enumerate(nums[i + 1:], start = i + 1):
                triplet_val = val1 + val2
                zero_compliment = -triplet_val
                '''
                [-1,0,1,2,-1,-4]
                we need the seen[zero_compliment] == i check bc 2 is added to the seen map on a previous iteration
                when we get to 2, -4, we have "seen" the zeros compliment 2 before, but it was on a previous iteration
                that check helps us check against the previous iteration, this protects us against counting 1 values twice
                '''
                if zero_compliment in seen and seen[zero_compliment] == i:
                    '''
                    sorted returns a list, so we need to use tuple() to cast it to a tuple
                    bc lists are not hashable (they are mutable, all mutable items not hashable)
                    '''
                    response.add(tuple(sorted([val1, val2, zero_compliment])))
                seen[val2] = i
        return response

from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)