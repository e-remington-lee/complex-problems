from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        ans = Node(node.val)
        self.map = {}
        self.backtracking(node, ans)
        
        return ans
    
    # @lru_cache(maxsize = None)
    def backtracking(self, current, new_current):
        if current.val in self.map:
            return
        
        self.map[current.val] = new_current
        
        for child in current.neighbors:
            if child.val in self.map:
                new_child = self.map[child.val]
            else:
                new_child = Node(child.val)
            
            new_current.neighbors.append(new_child)
            self.backtracking(child, new_child)

    def DFS2(self, node: 'Node') -> 'Node':
        if not node:
            return node
        self.copy_nodes = {}
        copy_head = self.clone_helper(node)
        return copy_head
    
    def clone_helper(self, node):
        if not node:
            return node
        
        if node.val in self.copy_nodes:
            return self.copy_nodes[node.val]
        
        copy_current = Node(node.val)
        self.copy_nodes[node.val] = copy_current
            
        for child in node.neighbors:
            copy_current.neighbors.append(self.clone_helper(child))
        
        return copy_current


    def BFS(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        visited = {node.val: Node(node.val)}
        queue = deque([node])
        
        while queue:
            current = queue.popleft()
            for child in current.neighbors:
                if child.val not in visited:
                    queue.append(child)
                    new_child = Node(child.val)
                    visited[child.val] = new_child
                else:
                    new_child = visited[child.val]
                visited[current.val].neighbors.append(new_child)
        
        return visited[node.val]


from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)