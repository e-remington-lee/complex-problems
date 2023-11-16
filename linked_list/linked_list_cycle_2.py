class Solution:
    def detectCycle(self, head):
        
        cycle_node = self.find_cycle(head)
        
        if cycle_node:
            start = head
            
            while start != cycle_node:
                start = start.next
                cycle_node = cycle_node.next
            return start
        else:
            return None
        
    
    def find_cycle(self, head):
        cycle = False
        slow = fast = head
        
        while slow and fast and fast.next:
            if slow.next == fast.next.next:
                return fast.next.next
            slow = slow.next
            fast = fast.next.next
        
        return None


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)