class Node(object):
    def __init__(self, value, next=None):
        self.value=value
        self.next=next
 
class Solution:
    def answer(self, arr):
        pass


def main():
    arr = [3,6,3,4,1]
    ans = Solution().answer(arr)
    print(ans)
    import heapq
    heapq.heapify(arr)
    print(arr)
    print(heapq.heappop(arr))
    print(heapq.heappop(arr))
    print(heapq.heappop(arr))
    print(heapq.heappop(arr))
    print(heapq.heappop(arr))
    heapq.heapify

if __name__=="__main__":
    main()


class NodesSumToZero(object):
    def answer(self, node):
        dummy_head=start = Node(0, node)
        map={}
        sum=0
        while start:
            sum+=start.value
            map[sum]=start
            start=start.next
        start=dummy_head
        sum=0
        while start:
            sum+=start.value
            start.next=map[sum].next
            start=start.next
        return dummy_head.next


# import sys
# from utilities import to_string
# flashcard=to_string.file_to_string(__file__)
# print(flashcard)

