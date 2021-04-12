class ReverseString:
    # O(n), space O(n)
    def classic(self, s):
        li = list(s)
        i, j = 0, len(s)-1
        while i <= j:
            li[i], li[j] = li[j], li[i]
            i+=1
            j-=1
        return "".join(li)

    def pythonic(self, s):
        return s[::-1]

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        curr = self
        cl = Node.idk
        response = ""
        li = []
        while curr:
            li.append(str(curr.value))
            curr = curr.next
        return response.join(li)

        

n = Node(4, Node(3))
print(n)
print(ReverseString().classic("hello"))
print(ReverseString().pythonic("hello"))
