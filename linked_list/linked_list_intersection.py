# https://leetcode.com/problems/intersection-of-two-linked-lists/
class Node(object):
    def __init__(self, value, next=None):
        self.value=value
        self.next=next

class Solution(object):
    def __init__(self):
        pass

    def answer(self, n1:Node, n2:Node):
        hash_set=set()
        while n1:
            hash_set.add(n1.value)
            n1=n1.next
        while n2:
            if n2.value in hash_set:
                return n2.value
            else:
                n2=n2.next
        return None

    def get_length(self, node):
        if not node:
            return 0
        else:
            return 1+self.get_length(node.next)
        # l=0
        # current=node
        # while current:
        #     l+=1
        #     current=current.next
        # return l
        
    def iterative(self, node):
        if not node:
            return 0
        count=0
        while node:
            count+=1
            node=node.next
        return count
    
    def optimal(self, headA, headB):
        l1, l2 = self.get_length(headA), self.get_length(headB)
        cur_1, cur_2 = headA, headB
        if l1>l2:
            for i in range(l1-l2):
                cur_1=cur_1.next
        else:
            for i in range(l2-l1):
                cur_2=cur_2.next
        while cur_1 != cur_2:
            cur_1=cur_1.next
            cur_2=cur_2.next
        return cur_1


    def idk(self, headA, headB):
        pA = headA
        pB = headB


        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        
        return pA

link=Node(3, Node(5, Node(7)))
headA = Node(2, link)
headB = Node(4, Node(8, link))

x = Solution().idk(headA, headB)
print(x.value)

li=[1,2,3]
li.insert(0,5)
print(li)