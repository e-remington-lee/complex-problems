class Node(object):
    def __init__(self, value, next=None):
        self.value=value
        self.next=next
 
class Solution:
    def answer(self, arr):
        pass





def main():
    arr = [3,6,3,4,1]
    ans = Solution().answer(arr)
    print(ans)

if __name__=="__main__":
    main()


def fib(n):
    #index 0, 1, 2 are 1,1,2 vs indexing at 1,2,3 as 1,1,2
    first=0
    second=1
    for _ in range(n):
        first, second = second, first+second
    return second
import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)

