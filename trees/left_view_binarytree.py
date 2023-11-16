#https://www.geeksforgeeks.org/print-left-view-binary-tree/
# https://www.youtube.com/watch?v=thkuu_FWFD8&t=6s
class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right

# does this really just work?
class Solution(object):
    def answer(self, node):
        if node:
            print(node.value, end="")
        current = node
        while current:
            if current.left:
                print(current.left.value, end="")
                current = current.left
            elif current.right:
                print(current.right.value, end="")
                current=current.right
            else:
                current=None

    def preorder(self, node):
        if node:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)



n1 = Node(1,left=Node(2, right=Node(4, right=Node(5, right=Node(6)))), right=Node(3))
# x=Solution().preorder(n1)
x=Solution().answer(n1)