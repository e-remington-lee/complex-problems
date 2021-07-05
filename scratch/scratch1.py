class Node(object):
    def __init__(self, value, next=None):
        self.value=value
        self.next=next

    def __str__(self):
        current=self
        r=[]
        while current:
            r.append(str(current.value)+",")
            current=current.next
        return "".join(r)

class Solution:
    def answer(self, coins, target):
        dp = [0]+[float('inf')]*target
        for i in range(1, target+1):
            for coin in coins:
                if i-coin>=0:
                    dp[i]=min(dp[i], dp[i-coin]+1)
        if dp[-1]==float('inf'):
            return -1
        else:
            return dp[-1]

    # def answer(self, coins, target):
    #     if target==0:
    #         return 1
    #     else:
    #         response = self.answer_helper(coins, target)
        
    #     if response==float('inf'):
    #         return -1
    #     else:
    #         return response

    # def answer_helper(self, coins, target):
    #     if target==0:
    #         return 0
    #     count=float('inf')
    #     for coin in coins:
    #         if target-coin>=0:
    #             count=min(count, self.answer_helper(coins, target-coin)+1)
    #     return count
        



def main():
    # arr = [7,1,5,3,6,4,0]
    arr = [1,7,5,3,2,4]
    coins=[2,5,10]
    i=10
    s="pwwxkew"
    c = {
        'CSC300': ['CSC100', 'CSC200'], 
        'CSC200': ['CSC100'], 
        'CSC100': []
        }
    # n1 = Node(10, Node(0, Node(5, Node(-3, Node(-3, Node(1, Node(7, Node(4, Node(-4)))))))))
    n1=Node(1, Node(-1))
    ans = Solution().answer(coins, 8)
    print(ans)

if __name__=="__main__":
    main()


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
# print(flashcard)

