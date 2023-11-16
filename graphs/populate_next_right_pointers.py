class Solution:
    def optimal(self, root: 'Node') -> 'Node':
        if not root:
            return root
        root.next = None
        self.recursive(root)
        return root
    
    def recursive(self, root):
        if root.left:
            left = root.left
            right = root.right
            left.next = right
            if root.next:
                right.next = root.next.left
            self.recursive(left)
            self.recursive(right)

    def BFS(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        root.next = None
        queue = [root]
        while queue:
            for i in range(len(queue)):
                current = queue.pop(0)
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)
            for i in range(len(queue) - 1):
                queue[i].next = queue[i + 1]
        return root

    def iterative(self, root: 'Node') -> 'Node':
        if not root:
            return root
        root.next = None
        left_most = root
        
        while left_most.left:
            head = left_most
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            left_most = left_most.left
        return root


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)