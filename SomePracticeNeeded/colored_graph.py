class Node:
    def __init__(self, value, node=None):
        self.value = value
        self.next = node

class Fib:
    def fib(self, n):
        if n==0:
            return 0
        if n ==1:
            return 1
        return self.fib(n-1) + self.fib(n-2)

print(Fib().fib(5))
    
class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = None
    
    def add_node(self, node):
        if self.head == None:
            self.head = node
        elif self.head != None and self.tail == None:
            self.tail = self.head
        self.head.next = node
        self.head = node
        
    def _traverse_helper(self, node):
        if node is not None:
            print(node.value)
            self._traverse_helper(node.next)
    
    def traverse(self):
        if self.tail is not None:
            self._traverse_helper(self.tail)
        else:
            return "Not instantiated"
        

class Solution:
    def answer(self, grid):
        for row in grid:
            pass


def main():
    grid = [
        ['r', 'g', 'b'],
        ['r', 'r', 'r'],
        ['g', 'g', 'r']
        ]
    Solution().answer(grid)
    n1 = Node(5)
    n2 = Node(6)
    n3 = Node(7)
    ll = LinkedList()
    ll.add_node(n1)
    ll.add_node(n2)
    ll.add_node(n3)
    print(ll.head.value, ll.tail.value)
    ll.traverse()

main()