class Solution:
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in map:
                return [i, map[ans]]
            map[nums[i]] = i
        return [0, 0]
            