class Solution:
    def getRow(self, rowIndex):
        return self.helper(rowIndex, [1])
    
    def helper(self, ri, p):
        if ri==0:
            return p
        ri-=1
        tp=[0]*(len(p)+1)
        l=len(tp)
        for i in range(l):
            if i==0 or i==l-1:
                tp[i]=1
            else:
                tp[i]=p[i]+p[i-1]
        return self.helper(ri, tp)

    def iterative(self, rowIndex):
        prev=[1]

        for i in range(1, rowIndex+1):
            current=[1]*(i+1)
            for j in range(0, i+1):
                if j==0 or j==i:
                    current[j]=1
                else:
                    current[j]=prev[j]+prev[j-1]
            prev=current
        return prev

    #we can calculate the next row from the previous row. 1 3 3 1, makes 4, 6, 4 1, then we add 1 to the beginning (we can do it reversed too)
    def iterative_optimal(self, rowIndex):
        p=[1]
        for i in range(rowIndex):
            for j in range(i):
                p[j]=p[j]+p[j+1]
            p.insert(0,1)
        return p


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
'''
We'll utilize a nice little property of Pascal's Triangle (given in the problem description):



In Pascal's triangle, each number is the sum of the two numbers directly above it.

Approach 4 will expand more on why it is so.

Algorithm

Let's say we had a function getNum(rowIndex, colIndex), which gave us the colIndexth number in the rowIndexth row, we could simply build the k^{th}k 
th
  row by repeatedly calling getNum(...) for columns 00 to kk.

We can formulate our intuition into the following recursion:

\text{getNum(rowIndex, colIndex) = getNum(rowIndex-1, colIndex-1) + getNum(rowIndex-1, colIndex)}getNum(rowIndex, colIndex) = getNum(rowIndex-1, colIndex-1) + getNum(rowIndex-1, colIndex)

The recursion ends in some known base cases:

The first row is just a single 11, i.e. \text{getNum(0, ...) = 1}getNum(0, ...) = 1

The first and last number of each row is 11, i.e. \text{getNum(k, 0) = getNum(k, k) = 1}getNum(k, 0) = getNum(k, k) = 1


Complexity Analysis

Time complexity : O(2^k)O(2 
k
 ). The time complexity recurrence is straightforward:

T(k,i) = T(k-1,i) + T(k-1,i-1) + O(1) \quad \ni \quad T(k,k) = T(k,0) = O(1)T(k,i)=T(k−1,i)+T(k−1,i−1)+O(1)∋T(k,k)=T(k,0)=O(1)

Thus, \text{T(k, m)}T(k, m) takes {k \choose m}( 
m
k
​
 ) units of constant time. [1]

For the k^{th}k 
th
  row, total time required is:

T(k, 0) + T(k, 1) + ... + T(k, k-1) + T(k, k) \\ \begin{aligned} &= \sum_{m=0}^k T(k, m) \\ &\simeq \sum_{m=0}^k O({k \choose m}) \\ &\simeq O(\sum_{m=0}^k {k \choose m}) \\ &= O(2^k) \end{aligned}T(k,0)+T(k,1)+...+T(k,k−1)+T(k,k)
​
  
= 
m=0
∑
k
​
 T(k,m)
≃ 
m=0
∑
k
​
 O(( 
m
k
​
 ))
≃O( 
m=0
∑
k
​
 ( 
m
k
​
 ))
=O(2 
k
 )
​
 

Space complexity : O(k) + O(k) \simeq O(k)O(k)+O(k)≃O(k).

We need O(k)O(k) space to store the output of the k^{th}k 
th
  row.
At worst, the recursive call stack has a maximum of kk calls in memory, each call taking constant space. That's O(k)O(k) worst case recursive call stack space.

Approach 2: Dynamic Programming
Intuition

In the previous approach, we end up making the same recursive calls repeatedly.



For example, to calculate getNum(5, 3) and getNum(5, 4), we end up calling getNum(3, 2) thrice. To generate, the entire fifth row (0-based row indexing), we'd have to call getNum(3, 2) four times.

It makes sense to store the results of intermediate recursive calls for later use.

Algorithm

Simple memoization caches results of deep recursive calls and provides significant savings on runtime.


But, it is worth noting that generating a number for a particular row requires only two numbers from the previous row. Consequently, generating a row only requires numbers from the previous row.

Thus, we could reduce our memory footprint by only keeping the latest row generated, and use that to generate a new row.


The std::move() operator on vectors in C++ is an O(1)O(1) operation. [2]

Complexity Analysis

Time complexity : O(k^2)O(k 
2
 ).

Simple memoization would make sure that a particular element in a row is only calculated once. Assuming that our memoization cache allows constant time lookup and updation (like a hash-map), it takes constant time to calculate each element in Pascal's triangle.
Since calculating a row requires calculating all the previous rows as well, we end up calculating 1 + 2 + 3 + ... + (k+1) = \dfrac {(k+1)(k+2)}{2} \simeq k^21+2+3+...+(k+1)= 
2
(k+1)(k+2)
​
 ≃k 
2
  elements for the k^{th}k 
th
  row.
Space complexity : O(k) + O(k) \simeq O(k)O(k)+O(k)≃O(k).

Simple memoization would need to hold all 1 + 2 + 3 + ... + (k+1) = \dfrac {(k+1)(k+2)}{2}1+2+3+...+(k+1)= 
2
(k+1)(k+2)
​
  elements in the worst case. That would require O(k^2)O(k 
2
 ) space.
Saving space by keeping only the latest generated row, we need only O(k)O(k) extra space, other than the O(k)O(k) space required to store the output.

Approach 3: Memory-efficient Dynamic Programming
Intuition

Notice that in the previous approach, we have maintained the previous row in memory on the premise that we need terms from it to build the current row. This is true, but not wholly.

What we actually need, to generate a term in the current row, is just the two terms above it (present in the previous row).

Formally, in memory,

pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
where pascal[i][j] is the number in ith row and jth column of Pascal's triangle.

So, trying to compute pascal[i][j], only the memory regions of pascal[i-1][j-1] and pascal[i-1][j] are required to be accessed.

Algorithm

Let's take a step back and analyze the circumstances under which pascal[i][j] might be accessed. Given that we have already employed DP to save us valuable run-time, the access pattern for pascal[i][j] looks a bit like this:

WRITE pascal[i][j] (after generating it from pascal[i-1][j-1] and pascal[i-1][j])
READ pascal[i][j] to generate pascal[i+1][j]
READ pascal[i][j] to generate pascal[i+1][j+1]
That's it! Once we've written out pascal[i][j]:

We don't ever need to modify it.
It's only read a fixed number of times, i.e. twice (thanks to DP).
Hypothetically, if we kept the the current row (in the process of being generated) and the previous row, in the same memory block, what kind of access patterns would we see (assume pascal[j] means the jth number in a row)?

pascal[j] was somehow generated in a previous instance. Currently, it holds the previous row value.

pascal[j] (which holds the jth number of the previous row) must be read when writing out pascal[j] (the jth number of the current row).

Obviously they are the same memory location, so a conflict exists: the previous row value of pascal[j] will be lost after the write-out.
Is that ok? If we don't need to read the previous row value of pascal[j] anymore, is there any harm in writing out the current row value in its place?
pascal[j] (which holds the jth number of the previous row) must be read when writing out pascal[j+1] (the j+1th number of the current row). These are two different memory locations, so there is no conflict.

If we managed to keep all read accesses on the previous row value of pascal[j], before any write access to pascal[j] for the current row value, we should be good! That's possible by evaluating each row from the end, instead of the beginning. Thus, a new row value of pascal[j+1] must be generated before doing so for pascal[j].

The following animation demonstrates the above algorithm, used to generate the 4th row of Pascal's Triangle, from an existing 3rd row:

Current
8 / 8

Complexity Analysis

Time complexity : O(k^2)O(k 
2
 ). Same as the previous dynamic programming approach.

Space complexity : O(k)O(k). No extra space is used other than that required to hold the output.

Although there is no savings in theoretical computational complexity, in practice there are some minor wins:

We have one vector/array instead of two. So memory consumption is roughly half.
No time wasted in swapping references to vectors for previous and current row.
Locality of reference shines through here. Since every read is for consecutive memory locations in the array/vector, we get a performance boost.
'''