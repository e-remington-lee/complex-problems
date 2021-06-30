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
    def answer(self, node):
        left=right=Node(0, node)
        s=0
        # hm={0:left}
        # right=right.next
        hm={}
        while right:
            s+=right.value
            hm[s]=right
            right=right.next
        # right=left.next
        right=left
        s=0
        while right:
            s+=right.value
            if s in hm:
                right.next=hm[s].next
            right=right.next
        return left.next


        

def main():
    arr = [7,1,5,3,6,4,0,]
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
    ans = Solution().answer(n1)
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
# print(flashcard)

