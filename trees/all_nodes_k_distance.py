from collections import deque
class Solution(object):
    def distanceK(self, root, target, K):
        self.dfs(root)
        
        queue = deque([(target, 0)])
        seen = {target}
        
        while queue:
            cur = queue.popleft()
            node, depth = cur
            if depth == K:
                response = [node.val]
                for n, d in queue:
                    response.append(n.val)
                return response
            for n in (node.par, node.left, node.right):
                if n and n not in seen:
                    seen.add(n)
                    queue.append((n, depth + 1))
        return []
                    
            
        
    def dfs(self, node, par = None):
        if node:
            node.par = par
            self.dfs(node.left, node)
            self.dfs(node.right, node)