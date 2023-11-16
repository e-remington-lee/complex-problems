# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int):
        return self.helper(1, n)
    
    
    def helper(self, start, end):
        if start>end:
            return [None]
        response=[]
        for i in range(start, end+1):
            left = self.helper(start, i-1)
            right = self.helper(i+1, end)
            
            for r in right:
                for l in left:
                    c = TreeNode(i)
                    c.right=r
                    c.left=l
                    response.append(c)
        return response

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
'''
If you have a tree with branching of b and max depth of m, the total number of nodes in this tree in worst case: 
1 + b + b^2 + ... + b^(m-1), 
which is a sum of geometric sequence: (b^m-1)/(b-1). So you can say that time complexity is O(b^m).
 For the example above it will be O(n*2^n). It is not exact as a Catalan number but I think it is enough in an interview.

 Approach 1: Recursion
First of all let's count how many trees do we have to construct. As you could check in this article, the number of possible BST is actually a Catalan number.

Let's follow the logic from the above article, this time not to count but to actually construct the trees.

Algorithm

Let's pick up number i out of the sequence 1 ..n and use it as the root of the current tree. Then there are i - 1 elements available for the construction of the left subtree and n - i elements available for the right subtree. As we already discussed that results in G(i - 1) different left subtrees and G(n - i) different right subtrees, where G is a Catalan number.

BST

Now let's repeat the step above for the sequence 1 ... i - 1 to construct all left subtrees, and then for the sequence i + 1 ... n to construct all right subtrees.

This way we have a root i and two lists for the possible left and right subtrees. The final step is to loop over both lists to link left and right subtrees to the root.


Complexity analysis

Time complexity : The main computations are to construct all possible trees with a given root, that is actually Catalan number G_nG 
n
​
  as was discussed above. This is done n times, that results in time complexity n G_nnG 
n
​
 . Catalan numbers grow as \frac{4^n}{n^{3/2}} 
n 
3/2
 
4 
n
 
​
time: 4^n/n^(1/2)
 
​
 ). Seems to be large but let's not forget that here we're asked to generate G_n \sim \frac{4^n}{n^{3/2}}G 
n
​
 ∼ 
n 
3/2
 
4 
n
 
​
  tree objects as output.

Space complexity : n G_n
n
​
  as we keep G_nG 
n
​
  trees with n elements each, that results in \mathcal{O}(\frac{4^n}{n^{1/2}})O( 
n 
1/2
 
4 
n
 
​
 ) complexity.
'''