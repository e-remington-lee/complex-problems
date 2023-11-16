class Solution:
    def validTree(self, n: int, edges):
        if len(edges) != n -1:
            return False
        dg = DisjointedGraph(n)
        
        for x, y in edges:
            if not dg.union(x, y):
                return False
        return True
    
    
    
class DisjointedGraph:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        
    def find(self, x):
        if x is not self.root[x]:
            self.root[x] = self.find(self.root[x])
            return self.root[x]
        return x
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX is rootY:
            return False
        if rootX is not rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
        return True

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)

'''
Approach 3: Advanced Graph Theory + Union Find
Intuition

In Approach 2, we used this definition for a tree:

For the graph to be a valid tree, it must have exactly n - 1 edges. Any less, and it can't possibly be fully connected. Any more, and it has to contain cycles. Additionally, if the graph is fully connected and contains exactly n - 1 edges, it can't possibly contain a cycle, and therefore must be a tree!

This definition simplified the problem down to checking whether or not the graph is fully connected. If it is, and if it contains n - 1 edges, then we know it's a tree. In the previous approaches, we used graph search algorithms to check whether or not all nodes were reachable, starting from a single source node.

Another way we could approach the problem is by considering each connected component to be a set of nodes. When an edge is put between two separate connected components, they are merged into a single connected component. We'll use the example n = 6 and edges = [(0, 5), (4, 0), (1, 2), (4, 5), (3, 2)]. Before we look at the edges, we have 6 sets.

Each of the nodes is in a separate set to start with.

We can then go through the list of edges, and merge sets together. For example, because the first edge is (0, 5), we merge the sets with 0 and 5. This means that we now have five connected components.

0 and 5 are merged into a single set, leaving 5 sets.

The next edge is (4, 0). Therefore, we merge the sets {0, 5} and {4} (remember that because 0 and 5 are connected, and 4 and 0 are connected, this means that 4 and 5 must also be connected).

{0, 5} and {4} are merged into a single set, leaving 4 sets.

We can continue this same process until we've gone through all the edges. Here is an animation showing this.

Current
11 / 11
The conclusion we can draw for this example is that the edges are not in a single connected component, and therefore must contain a cycle. The algorithm should return false.

And here is another example where the edges do form a single connected component.

Current
1 / 12
Did you notice that in the second animation, every edge resulted in a merge operation, but in the first animation, some didn't? This was because of cycles in the graph. Each time there was no merge, it was because we were adding an edge between two nodes that were already connected via a path. This means there is now an additional path between them—which is the definition of a cycle. Therefore, as soon as this happens, we can terminate the algorithm and return false.

Now, how should we implement this? Well, we could create a list of Sets and then carry out the algorithm as it was done in the animation. There is, however, a better way; a really clever algorithm we call union find. I'll give a brief introduction to the algorithm here, however, if you aren't familiar with it, I strongly recommend reading up on it out of a good algorithm textbook. We don't yet have an explore card on union find (at the time of writing this!). Union find is a very useful algorithm that can be used to solve many graph problems.

Union find represents each of the sets as a directed tree, with the edges pointing towards the root node. For example, consider this graph from our first example above (the one that was not a valid tree).

Example of a graph

One way its connected components could be represented by union find is as follows:

Trees representation for graph 1.

Union find is a data structure with 3 methods; makeset(A), find(A) and union(A, B).

The makeset(A) method is the simplest. It creates a new size-1 set containing just element A.

The find(A) method starts at A, and traces parent links up until it gets to A's tree root. It then returns the tree root ID. Two nodes that are in the same connected component have the same root. If they're in different connected components, then they will have different roots. For the above example, find(0), find(4), and find(5) will all return 5. Whereas find(1), find(2) and find(3) will all return 1. This method can be used to check whether or not 2 elements are in the same connected component, and is also used by the union(A, B) method, as we're about to see.

The union(A, B) method works by finding the root for A and the root for B, using the find(...) operation. It then sets Bs parent to be A, thus combining the two trees into one. For example, if we add the edge (4, 3) to the example above, the algorithm will find that the root of 4 is 5, and the root of 3 is 1, and merge those subtrees. Once this is done, all of the nodes have the same root of 5, and therefore we know they all belong to the same connected component.

Merging the two trees with the edge (4, 3).

We don't need to use linked nodes to represent this structure; we can simply maintain an array of parent pointers. For example, here's how the above tree is represented as an array.

Parent pointers for the above tree.

Notice how 5 simply points to itself, as it's the root. The find(...) operation works its way up parent links until it finds a node that points back to itself.

This algorithm might not seem very efficient, after all, the find(...) operation could be O(n)O(n) in the worst case. However, there are two straightforward optimizations we can apply that bring the amortized time close to O(1)O(1) for both union(...) and find(...).

Tracking the sizes of each set; this helps to ensure the tree depth is minimised, as we can ensure the smaller set is attached onto the larger set, and not the other way around. The modifications for this are in the union(...) method.

When doing a find(...), keeping track of all the nodes along the path so that afterwards we can make each point directly at the root, so that next time any of those nodes are searched for, it is O(1)O(1). The modifications for this are all in the find(...) method.

Variants of these also exist, that result in the same overall time complexity.

Algorithm

Firstly, here's the code without the optimizations. Below, I've also included the code with the optimizations. If you're new to union find, then I recommend reading the code without optimizations first, as it's a lot easier to understand!


These are the solutions using the optimizations path compression and union by size.


Complexity Analysis

Let EE be the number of edges, and NN be the number of nodes.

α(N)α(N) is the Inverse Ackermann Function.

Time Complexity : O(N \cdot α(N))O(N⋅α(N)).

When E ≠ N - 1E 

​
 =N−1, we simply return false. Therefore, the worst case is when E = N - 1E=N−1. Because EE is proportional to NN, we'll say E = NE=N to simplify the analysis.

We are putting each of the NN edges into the UnionFind data structure, using the union(...) method. The union(...) method itself has no loops or recursion, so the entire cost of calling it is dependent on the cost of the find(...) method that it calls.

find(...)'s cost is dependent on how far the node it was searching for is from the root. Using the naïve implementation of union find, this depth could be NN. If this was the case for all of the calls, we'd have a final cost of O(N^2)O(N 
2
 ).

However, remember those optimizations we did? Those keep the tree depths very shallow. It turns out that find(...) amortizes to O(α(N))O(α(N)), where α is the Inverse Ackermann Function. The incredible thing about this function is that it grows so slowly that NN will never go higher than 44 in the universe as we know it! So while in "practice" it is effectively O(1)O(1), in "theory" it is not.

Actually proving this upper bound on the depth is a very advanced proof, which I'd certainly hope you'd never need to do in an interview! If you're interested though, I recommend looking in a good algorithm's text book or paper.

Anyway, this gives us a total of N \cdot O(α(N)) = O(N \cdot α(N))N⋅O(α(N))=O(N⋅α(N)).

Space Complexity : O(N)O(N).

The UnionFind data structure requires O(N)O(N) space to the store the javaPractice it uses.

So, why is this better than Approach 2?

Complexity analysis ignores constants. For example, O(10 \cdot N) = O(N)O(10⋅N)=O(N). Even O(10000 \cdot N) = O(N)O(10000⋅N)=O(N). Sometimes the constants we're ignoring in the analysis are still having a big impact on the run-time in practice.

Approach 2 had a lot of overhead in needing to create an adjacency list with the edges before it could even begin the depth-first search. This is all treated as a constant, as it ultimately had the same time complexity as the depth-first search itself.

Approach 3 doesn't need to change the input format, it can just get straight to determining whether or not there is a cycle. Additionally the bit that stops it being constant, the α(N)α(N), will never have a value larger than 44. So in practice, it behaves as a constant too—and a far smaller one at that!

When weighing up the pros and cons of different algorithms for solving problems, it's best to treat union find's operations as O(1)O(1) to get a fair and accurate comparison.
'''