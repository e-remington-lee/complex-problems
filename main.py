# class Node(object):
#     def __init__(self, value, next=None):
#         self.value=value
#         self.next=next

class Node(object):
    def __init__(self, value, right=None, left=None):
        self.value=value
        self.right=right
        self.left=left
 
class Solution:
    def answer(self, node):
        if node:
            node.left, node.right=node.right, node.left
            self.answer(node.left)
            self.answer(node.right)
            return node

    def other_invert(self, node):
        if node:
            node.left, node.right = self.other_invert(node.right), self.other_invert(node.left)
            return node

    def preorder(self, node):
        if node:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)


def main():
    b = Node("b", left=Node("d"), right=Node("e"))
    c = Node("c", left=Node("f"), right=Node("g"))
    root = Node("a", left=b, right=c)
    x=Solution()
    n=x.other_invert(root)
    print(x.preorder(n))

    


if __name__=="__main__":
    main()


class NodesSumToZero(object):
    def answer(self, node):
        dummy_head=start = Node(0, node)
        map={}
        sum=0
        while start:
            sum+=start.value
            map[sum]=start
            start=start.next
        start=dummy_head
        sum=0
        while start:
            sum+=start.value
            start.next=map[sum].next
            start=start.next
        return dummy_head.next


# import sys
# from utilities import to_string
# flashcard=to_string.file_to_string(__file__)
# print(flashcard)

