'''
https://leetcode.com/problems/balanced-binary-tree/
create a binary search tree that is always balanced or 1 node away from being balanced
constructing a BST is O(n log(n)), a BST is sorted, fastest sorting algorithm is O(n log n)
'''
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def answer(self, root):
        if not root:
            return True
        height = self.height(root)
        return height!=-1
    
    def height(self, node):
        if not node:
            return 0

        rh = self.height(node.right)
        lh = self.height(node.left)
        if rh==-1 or lh==-1 or abs(rh-lh)>1:
            return -1
        else:
            return max(rh+1, lh+1) 

def main():
    '''
             7
         3       3
            2       2
                       3
    '''
    right2=Node(3)
    left=Node(3, right=right2)
    right=Node(3, left=None, right=Node(2, right=right2))
    root=Node(7, right=right, left=left)
    x=Solution().answer(root)
    print(x)

if __name__=="__main__":
    main()
    # import sys
    # sys.path.append(".")
    # from utilities import to_string
    # flashcard=to_string.file_to_string(__file__)
    # print(flashcard)