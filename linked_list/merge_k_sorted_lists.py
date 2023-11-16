import heapq
class Solution:
    def optimal(self, lists):
        if not lists:
            return None
        
        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self.mergeTwo(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]
            
        
    def mergeTwo(self, n1, n2):
        head = cur = ListNode(-1)
        while n1 and n2:
            if n1.val < n2.val:
                cur.next = n1
                n1 = n1.next
            else:
                cur.next = n2
                n2 = n2.next
            cur = cur.next
        
        if not n1:
            cur.next = n2
        else:
            cur.next = n1
        
        return head.next

    def mergeKLists(self, lists):
        if not lists:
            return None
        
        dummy_head = cur = ListNode(-1)
        
        queue = []
        for head in lists:
            if head:
                heapq.heappush(queue, Comparator(head.val, head, head.next))
        
        while queue:
            comparator = heapq.heappop(queue)
            val, node, _next = comparator.val, comparator.cur, comparator._next
            cur.next = node
            cur = cur.next
            if _next:
                heapq.heappush(queue, Comparator(_next.val, _next, _next.next))
            
        return dummy_head.next
    
class Comparator:
    def __init__(self, val, cur, _next):
        self.val = val
        self.cur = cur
        self._next = _next
        
    def __lt__(self, y):
        if self.val == y.val:
            return True
        else:
            return self.val < y.val

from utilities import to_string
flashcard=to_string.file_to_string(__file__)
# print(flashcard)

li = [1,2,34]

for i, x in enumerate(li, start=1):
    print(i, x)