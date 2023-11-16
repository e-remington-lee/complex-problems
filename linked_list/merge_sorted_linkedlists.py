#https://leetcode.com/problems/merge-two-sorted-lists/
class ListNode(object):
    def __init__(self, val, next=None):
        self.val=val
        self.next=next

class MergeTwoLists(object):
    def answer(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if not l1:
        #     return l2
        # elif not l2:
        #     return l1

        cur = head = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        
        # if not l1:
        #     cur.next = l2
        # elif not l2:
        #     cur.next = l1
        '''
        you probably need to write this out to visualize it, 2 if-statements is fine as well
        This also lets us get rid of the first null check in the beginning, I would never recommend this if you have not seen the problem before 
        bc it could be risky
        '''
        cur.next = l1 if l1 else l2
        return head.next

            
    def recursive(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.recursive(l1.next, l2)
            return l1
        else:
            l2.next = self.recursive(l1, l2.next)
            return l2
            
import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)