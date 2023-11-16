class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        rh = self.height(root.right)
        lh = self.height(root.left)
        
        if rh == float('inf') or lh == float('inf'):
            return False
        else:
            return abs(rh - lh) < 2
    
    def height(self, root):
        if not root:
            return 0
        
        rh = self.height(root.right)
        lh = self.height(root.left)
        
        if abs(rh - lh) > 1:
            return float('inf')
        else:
            return max(rh, lh) + 1


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)