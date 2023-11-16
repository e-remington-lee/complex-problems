class Solution:
    def recursive(self, root):
        if not root:
            return root
        self.response = []
        self.recursion(root, 0)
        return self.response
    
    def recursion(self, root, level):
        if not root:
            return
        
        if len(self.response) <= level:
            self.response.append([])

        self.response[level].append(root.val)
        
        for child in root.children:
            self.recursion(child, level + 1)

    def iterative(self, root):
        if not root:
            return root
        
        queue = [root]
        response = []
        
        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                current = queue.pop(0)
                level.append(current.val)
                for child in current.children:
                    queue.append(child)
            response.append(level)
        return response    

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)