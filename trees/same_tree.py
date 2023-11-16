# https://leetcode.com/problems/same-tree/solution/
class Solution:
    def recursion(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        if p.val==q.val:
            if self.recursion(p.left, q.left) and self.recursion(p.right, q.right):
                return True
            else:
                return False
        else:
            return False


    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        stack1=[p]
        stack2=[q]
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1.val==node2.val:
                if node1.right and node2.right:
                    stack1.append(node1.right)
                    stack2.append(node2.right)
                elif not node1.right and not node2.right:
                    pass
                else:
                    return False
                
                if node1.left and node2.left:
                    stack1.append(node1.left)
                    stack2.append(node2.left)
                elif not node1.left and not node2.left:
                    pass
                else:
                    return False
            else:
                return False
        return True

# import sys
# sys.path.append(".")
# from utilities import to_string
# flashcard=to_string.file_to_string(__file__)
# print(flashcard)