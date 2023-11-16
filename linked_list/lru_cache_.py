class DllNode:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head, self.tail = DllNode(), DllNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_back(node)
            return node.value
        return -1
    
    def add_node(self, node):
        prev_tail = self.tail.prev
        prev_tail.next = node
        node.prev = prev_tail
        self.tail.prev = node
        node.next = self.tail
        
        
    def remove_node(self, node):
        prev = node.prev
        _next = node.next
        prev.next = _next
        _next.prev = prev
    
    def move_to_back(self, node):
        self.remove_node(node)
        self.add_node(node)
        
    def remove_head(self):
        head = self.head.next
        self.remove_node(head)
        del self.cache[head.key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove_node(node)
            self.move_to_back(node)
        else:
            node = DllNode(key, value)
            self.add_node(node)
        
            self.cache[key] = node
            self.size += 1
            if self.size > self.capacity:
                self.remove_head()
                self.size -= 1
                
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)