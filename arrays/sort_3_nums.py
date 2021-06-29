'''
Hi, here's your problem today. This problem was recently asked by Google:

Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

Example 1:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]
def sortNums(nums):
  # Fill this in.

print sortNums([3, 3, 2, 1, 3, 2, 1])
# [1, 1, 2, 2, 3, 3, 3]


Tricks:
You can swap indexes in an array like this in python, doing this is O(n) time
Reorganizing an array with 1 pass-through is key, important to recognize it
While loops are required for this if you want to reorganize a list, this is because a for loop will not work the way you want
'''
class Solution:
    def answer_On(self, arr):
        ones = []
        twos = []
        threes = []

        for x in arr:
            if x == 1:
                ones.append(x)
            elif x == 2:
                twos.append(x)
            else:
                threes.append(x)            
        return ones+twos+threes

    def answer_O1(self, arr):
        one_idx = 0
        three_idx = len(arr)-1
        idx = 0
        while idx <= three_idx:
            if arr[idx] == 1:
                arr[idx], arr[one_idx] = arr[one_idx], arr[idx]
                one_idx+=1
                idx+=1
            elif arr[idx]==2:
                idx+=1
            elif arr[idx] == 3:
                arr[idx], arr[three_idx] = arr[three_idx], arr[idx]
                three_idx-=1
        return arr


def main():
    # [2,2,2,3,3,3,3,3,3,3]
    arr = [2, 1, 3, 3, 2, 1, 3, 2, 1, 3, 1]
    ans = Solution().answer_O1(arr)
    print(ans)

main()
