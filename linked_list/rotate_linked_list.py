class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        
        old_tail = head
        length = 1
        while old_tail.next:
            old_tail = old_tail.next
            length += 1
        
        old_tail.next = head
        true_rotations = k % length
        for _ in range(length - true_rotations):
            old_tail = old_tail.next
        new_head = old_tail.next
        old_tail.next = None
        return new_head

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)