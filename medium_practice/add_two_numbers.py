class Node(object):
    def __init__(self, value, next=None):
        self.value=value
        self.next=next

class Solution(object):
    def answer(self, n1, n2):
        carry=0
        prev=None
        while n1 or n2:
            if n1:
                carry+=n1.value
                n1=n1.next
            if n2:
                carry+=n2.value
                n2=n2.next
            node=Node(carry%10)
            node.next=prev
            prev=node
            carry//=10
        return prev

# print(19//10)
# x=None
# if x is None:
#     print("x")
# else:
#     print("wow")

n1=Node(2, Node(4, Node(6, Node(7))))
n2=Node(7, Node(9, Node(8)))
x = Solution().answer(n1, n2)
while x:
    print(x.value, end="")
    x=x.next