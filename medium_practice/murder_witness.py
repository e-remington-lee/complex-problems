'''
Hi, here's your problem today. This problem was recently asked by Google:

There are n people lined up, and each have a height represented as an integer. A murder has happened right in front of them, and only people who are taller than everyone in front of them are able to see what has happened. How many witnesses are there?

Example:
Input: [3, 6, 3, 4, 1]  
Output: 3
Explanation: Only [6, 4, 1] were able to see in front of them.
 #
 #
 # #
####
####
#####
36341                                 x (murder scene)
'''

import sys
class Solution:
    def answer(self, arr):
        _max=-sys.maxsize-1
        count=0
        for i in range(len(arr)-1, -1, -1):
            if arr[i]>_max:
                count+=1
                # super optimal, only set max each time you increment the count
                # also, no need for max(), just set _max=arr[i]
                _max=max(arr[i], _max)
        return count
            

def main():
    arr = [3,6,3,4,1]
    ans = Solution().answer(arr)
    print(ans)
    import sys
    sys.path.append(".")
    from utilities import to_string
    flashcard=to_string.file_to_string(__file__)
    print(flashcard)

if __name__=="__main__":
    main()


