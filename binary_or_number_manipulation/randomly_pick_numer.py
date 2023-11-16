import random

class Solution(object):
    def answer(self, li:list)->int:
        length = len(li)
        rand = random.randrange(0, length)
        return li[rand]
        # print(rand)


if __name__ == "__main__":
    x = Solution().answer([1,2,3,4])
    print(x)

