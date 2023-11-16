class ListNode(object):
    def __init__(self, value, next=None):
        self.value=value
        self.next=next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = response = ListNode(0)
        carry = 0
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            div, mod = divmod(carry, 10)
            
            carry = div
            current.next = ListNode(mod)
            current = current.next
            
        if carry > 0:
            current.next = ListNode(carry)
        
        return response.next


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)