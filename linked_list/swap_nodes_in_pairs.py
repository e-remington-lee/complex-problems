class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head
        th=head
        followup=head.next.next
        head=head.next
        head.next = th
        th.next=self.swapPairs(followup)
        return head

    def iterative(self, head):
        if not head or not head.next:
            return head
        th=head
        second=head.next
        current=second.next
        second.next=th
        while current and current.next:
            th.next=current.next
            followup = current.next.next
            n=current.next
            n.next=current
            th=current
            current=followup

        th.next=current
        return second