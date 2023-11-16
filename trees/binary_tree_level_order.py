class Solution:
    def levelOrder(self, root):
        if not root:
            return
        output=[]
        stack=[root]
        while stack:
            n=len(stack)
            li=[]
            for i in range(n):
                cur=stack.pop(0)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
                li.append(cur.val)
            output.append(li)
        return output

    def recursive(self, root):
        output=[]
        if not root:
            return output
        self.helper(root, 0, output)
        return output
    
    def helper(self, root, level, output):
        if len(output)==level:
            output.append([])
        output[level].append(root.val)
        if root.left:
            self.helper(root.left, level+1, output)
        if root.right:
            self.helper(root.right, level+1, output)

    def my_custom_one(self, root):
        if not root:
            return []
        depth=self.depth(root)
        output = [[] for i in range(depth)]
        self.helper(root, 0, output)
        return output
    
    def custom_helper(self, root, level, output):
        if not root:
            return 
        output[level].append(root.val)
        if root.left:
            self.custom_helper(root.left, level+1, output)
        if root.right:
            self.custom_helper(root.right, level+1, output)
        
    def depth(self, root):
        if not root:
            return 0
        return 1+max(self.depth(root.left), self.depth(root.right))


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
