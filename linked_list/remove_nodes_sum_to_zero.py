'''
Hi, here's your problem today. This problem was recently asked by Uber:

Given a linked list of integers, remove all consecutive nodes that sum up to 0.

Example:
Input: 10 -> 5 -> -3 -> -3 -> 1 -> 4 -> -4
Output: 10

The consecutive nodes 5 -> -3 -> -3 -> 1 sums up to 0 so that sequence should be removed. 4 -> -4 also sums up to 0 too so that sequence should also be removed.

Here's a starting point:
'''
class Node(object):
    def __init__(self, value, next=None):
        self.value=value
        self.next=next

    '''
    can be solved by finding prefix sum
    if l1+l2 = l1+l2+...+l5, meaning that l3 + ... + l5 = 0, 
    then l3 + ... + l5 is the consecutive sequence of nodes we want to delete. 
    If it's a array we could just remove numbers from index of l3 to l5. 
    If it's a linked list, we could let l2.next = l5.next, we then need to have two pointers,
    one point to l2 and the other point to l5

    more:
    Intuition and Algorithm
    Imagine that you have this Linked list:
    head: [3,4,2,-6, 1,1,5, -6]

    What elements should I remove?
    We will accumulate the values.
    head’ : [3, 7,9,3,4,5,10,4]
    (Like an array), head'[i] = head[i] + head' [i-1]
    If we see repeated elements then we have to deleted as follows.
    '''
class Solution(object):
    def answer(self, node):
        dummy_head=start = Node(0, node)
        map={}
        #map={0, start}
        sum=0
        while start:
            sum+=start.value
            map[sum]=start
            start=start.next
        start=dummy_head
        # we cannot do this bc it disassociates the left.next from the right.next if the first node is to be removed
        # start=dummy_head.next
        sum=0
        while start:
            sum+=start.value
            start.next=map[sum].next
            start=start.next
        return dummy_head.next

    # TODO does not work for [1,3,2,-3,-2,5,5,-5,1]
    # def optimal(self, node):
    #     left=right=Node(0, node)
    #     s=0
    #     hm={}
    #     while right:
    #         s+=right.value
    #         if s in hm:
    #             hm[s].next=right.next
    #         else:
    #             hm[s]=right
    #         right=right.next
    #     return left.next


def main():
    n1 = Node(10, Node(-10, Node(5, Node(-3, Node(-3, Node(1, Node(7, Node(4, Node(-4)))))))))
    x = Solution().very_difficult(n1)
    # x = Solution().answer(n1)
    while x:
        print(x.value)
        x=x.next

if __name__=="__main__":
    main()

# /**
#  * Definition for singly-linked list.
#  * public class ListNode {
#  *     int val;
#  *     ListNode next;
#  *     ListNode(int x) { val = x; }
#  * }
#  */
# class Solution {
#     public ListNode removeZeroSumSublists(ListNode head) {
#         // The observation here is that the sum from index 0 to index M will be 
#         // equal to sum from index 0 to index N if sum from index (M+1) to index N is 0.
#         // Thus, here we track the sum from index 0 to each index, using a Map to indicate
#         // the farthest index N that we can remove from index M, then we shall be able to
#         // remove M+1 -> N and continue from N+1. This works since we don't have to optimize
#         // for the number of sequences to be removed
        
#         // Map from sum from index 0 to the farthest value that the sum stays unchanged.
#         Map<Integer, ListNode> sumToFarthestNodeMap = new HashMap<>();
        
#         // Need the dummy node to track the new head if changed.
#         ListNode preHead = new ListNode(0);
#         preHead.next = head;
        
#         // First iteration to compute the map.
#         int sum = 0;
#         for (ListNode p = preHead; p != null; p = p.next) {
#             sum += p.val;
#             sumToFarthestNodeMap.put(sum, p);
#         }
        
#         // Second iteration to re-connect the nodes to the farthest node where the sum stays unchanged
#         sum = 0;
#         for (ListNode p = preHead; p != null; p = p.next) {
#             sum += p.val;
#             p.next = sumToFarthestNodeMap.get(sum).next;
#         }
        
#         // Done, return the head from preHead
#         return preHead.next;
#     }
# }    

if __name__ == "__main__":
    main()

