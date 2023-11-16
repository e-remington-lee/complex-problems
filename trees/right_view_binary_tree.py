# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def two_queues(self, root):
        if not root:
            return []
        output=[]
        queue=[root]
        while queue:
            li=[]
            for i in range(len(queue)):
                current=queue.pop(0)
                li.append(current)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            output.append(li.pop().val)
        return output

    def sentinel_node(self, root):
        if not root:
            return []
        output=[]
        queue=[root, None]
        c=root
        while queue:
            prev, c=c, queue.pop(0)
            
            while c:
                if c.left:
                    queue.append(c.left)
                if c.right:
                    queue.append(c.right)             
                prev, c = c, queue.pop(0)
                
            output.append(prev.val)
            if queue:
                queue.append(None)
            
        return output

    def recursive(self, root):
            if not root:
                return []
            output=[]
            self.helper(root, output, 0)
            return output
        
    def helper(self, root, output, level):
        if len(output) is level:
            output.append(root.val)
        if root.right:
            self.helper(root.right, output, level+1)
        if root.left:
            self.helper(root.left, output, level+1)

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)

'''
Overview
DFS vs. BFS

There are two ways to traverse the tree: DFS depth first search and BFS breadth first search. Here is a small summary

diff

BFS traverses level by level, and DFS first goes to the leaves.

diff

Which approach to choose, BFS or DFS?

The problem is to return a list of last elements from all levels, so it's the way more natural to implement BFS here.

Time complexity is the same \mathcal{O}(N)O(N) both for DFS and BFS since one has to visit all nodes.

Space complexity is \mathcal{O}(H)O(H) for DFS and
\mathcal{O}(D)O(D) for BFS, where HH is a tree height, and DD is a tree diameter. They both result in \mathcal{O}(N)O(N) space in the worst-case scenarios: skewed tree for DFS and complete tree for BFS.

BFS wins for this problem, so let's use the opportunity to check out three different BFS implementations with the queue.

BFS implementation

All three implementations use the queue in a standard BFS way:

Push the root into the queue.

Pop-out a node from the left.

Push the left child into the queue, and then push the right child.

diff

Three BFS approaches

The difference is how to find the end of the level, i.e. the rightmost element:

Two queues, one for the previous level and one for the current.

One queue with sentinel to mark the end of the level.

One queue + level size measurement.



Approach 1: BFS: Two Queues
Let's use two queues: one for the current level, and one for the next. The idea is to pop the nodes one by one from the current level and push their children into the next level queue. Each time the current queue is empty, we have the right side element in hands.

diff

Algorithm

Initiate the list of the right side view rightside.

Initiate two queues: one for the current level, and one for the next. Add root into nextLevel queue.

While nextLevel queue is not empty:

Initiate the current level: currLevel = nextLevel, and empty the next level nextLevel.

While current level queue is not empty:

Pop out a node from the current level queue.

Add first left and then right child node into nextLevel queue.

Now currLevel is empty, and the node we have in hands is the last one, and makes a part of the right side view. Add it into rightside.

Return rightside.

Implementation


Complexity Analysis

Time complexity: \mathcal{O}(N)O(N) since one has to visit each node.

Space complexity: \mathcal{O}(D)O(D) to keep the queues, where DD is a tree diameter. Let's use the last level to estimate the queue size. This level could contain up to N/2N/2 tree nodes in the case of complete binary tree.



Approach 2: BFS: One Queue + Sentinel
Another approach is to push all the nodes in one queue and to use a sentinel node to separate the levels. Typically, one could use null as a sentinel.

diff

The first step is to initiate the first level: root + null as a sentinel. Once it's done, continue to pop the nodes one by one from the left and push their children to the right. Stop each time the current node is null because it means we hit the end of the current level. Each stop is a time to update a right side view list and to push null in the queue to mark the end of the next level.

Algorithm

Initiate the list of the right side view rightside.

Initiate the queue by adding a root. Add null sentinel to mark the end of the first level.

Initiate the current node as root.

While queue is not empty:

Save the previous node prev = curr and pop the current node from the queue curr = queue.poll().

While the current node is not null:

Add first left and then right child node into the queue.

Update both previous and current nodes: prev = curr, curr = queue.poll().

Now the current node is null, i.e. we reached the end of the current level. Hence the previous node is the rightmost one and makes a part of the right side view. Add it into rightside.

If the queue is not empty, push the null node as a sentinel, to mark the end of the next level.

Return rightside.

Implementation

Note, that ArrayDeque in Java doesn't support null elements, and hence the data structure to use here is LinkedList.


Complexity Analysis

Time complexity: \mathcal{O}(N)O(N) since one has to visit each node.

Space complexity: \mathcal{O}(D)O(D) to keep the queues, where DD is a tree diameter. Let's use the last level to estimate the queue size. This level could contain up to N/2N/2 tree nodes in the case of complete binary tree.



Approach 3: BFS: One Queue + Level Size Measurements
Instead of using the sentinel, we could write down the length of the current level.

diff

Algorithm

Initiate the list of the right side view rightside.

Initiate the queue by adding a root.

While the queue is not empty:

Write down the length of the current level: levelLength = queue.size().

Iterate over i from 0 to level_length - 1:

Pop the current node from the queue: node = queue.poll().

If i == levelLength - 1, then it's the last node in the current level, push it to rightsize list.

Add first left and then right child node into the queue.

Return rightside.

Implementation


Complexity Analysis

Time complexity: \mathcal{O}(N)O(N) since one has to visit each node.

Space complexity: \mathcal{O}(D)O(D) to keep the queues, where DD is a tree diameter. Let's use the last level to estimate the queue size. This level could contain up to N/2N/2 tree nodes in the case of complete binary tree.



Approach 4: Recursive DFS
Everyone likes recursive DFS, so let's add it here as well. The idea is simple: to traverse the tree level by level, starting each time from the rightmost child.

Implementation


Complexity Analysis

Time complexity: \mathcal{O}(N)O(N) since one has to visit each node.

Space complexity: \mathcal{O}(H)O(H) to keep the recursion stack, where HH is a tree height. The worst-case situation is a skewed tree, when H = NH=N.
'''