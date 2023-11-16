class Solution:
    def optimal(self, head):
        if not head:
            return None
        
        current = head
        copy_head = copy_current = None
        
        while current:
            if not copy_head:
                copy_head = copy_current = Node(current.val)
            else:
                copy_current = Node(current.val)
                
            _next = current.next
            current.next = copy_current
            copy_current.next = _next
            current = current.next.next
        
        current = head
        copy_current = copy_head
        
        while current:
            if current.random:
                copy_current.random = current.random.next
            else:
                copy_current.random = None
            
            current = current.next.next
            if current:
                copy_current.next = copy_current.next.next
            else:
                copy_current.next = None
            copy_current = copy_current.next
                
        return copy_head


    def remakes_input(self, head):
        if not head:
            return None
        copy_head = copy = None
        cur = head
        
        while cur:
            if not copy_head:
                copy_head = copy = Node(cur.val)
            else:
                copy = Node(cur.val)
            hold = cur.next
            cur.next = copy
            copy.next = hold
            cur = hold
        
        cur = head
        copy = copy_head
        while cur:
            if cur.random:
                copy.random = cur.random.next
            else:
                copy.random = None
            if copy.next:
                copy = copy.next.next
            cur = cur.next.next
            
            
        cur = head
        copy = copy_head
        while cur:
            cur.next = cur.next.next
            if copy.next:
                copy.next = copy.next.next
            copy = copy.next
            cur = cur.next
        return copy_head


    def iterative2(self, head):
        if not head:
            return None        
        
        current = head
        copy_head = copy_current = Node(head.val)
        self.visited = {head: copy_head}

        while current:
            copy_current.next = self.helper(current.next)
            copy_current.random = self.helper(current.random)
            
            current = current.next
            copy_current = copy_current.next
        
        return copy_head
            
    def helper(self, node):
        if node:
            if node not in self.visited:
                self.visited[node] = Node(node.val)
                return self.visited[node]
            else:
                return self.visited[node]
        return None


    def iterative(self, head):
        if not head:
            return None
        current = head
        new_head = current_copy = Node(head.val)
        hashmap = {}
        while current:
            hashmap[current] = current_copy                            
            if current.next:
                _next = Node(current.next.val)
            else:
                _next = None
            current_copy.next = _next
            current = current.next
            current_copy = current_copy.next
    
        current = head
        current_copy = new_head
        while current:
            if current.random:
                current_copy.random = hashmap[current.random]
            else:
                current_copy.random = None
            current = current.next
            current_copy = current_copy.next
        
        return new_head


    def recursive(self, head):
        if not head:
            return None        
        
        self.visited = {}
        self.copy_helper(head)
        return self.visited[head]
        
    def copy_helper(self, node):
        if not node:
            return None
        if node in self.visited:
            return self.visited[node]
        
        new_node = Node(node.val)
        self.visited[node] = new_node
        new_node.random = self.copy_helper(node.random)
        new_node.next = self.copy_helper(node.next)
        return new_node

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)