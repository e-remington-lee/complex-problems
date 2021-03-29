# Hi, here's your problem today. This problem was recently asked by Facebook:

# Given an undirected graph, determine if a cycle exists in the graph.

# Here is a function signature:

# def find_cycle(graph):
#   # Fill this in.

# graph = {
#   'a': {'a2':{}, 'a3':{} },
#   'b': {'b2':{}},
#   'c': {}
# }
# print find_cycle(graph)
# # False
# graph['c'] = graph
# graph = {
#   'a': {'a2':{}, 'a3':{} },
#   'b': {'b2':{}},
#   'c': {
#     'a': {'a2':{}, 'a3':{} },
#     'b': {'b2':{}},
#     'c': {}
#     }
# }
# print find_cycle(graph)
# # True

# Can you solve this in linear time, linear space?

#TODO how to implement DFS vs BFS
class Solution:
    def dfs_solution(self, graph: dict) -> bool:
        vertexes = set()
        for vertex in graph.keys():
            if vertex not in vertexes:
                answer = self.dfs_2(vertex, vertexes, vertex, graph)
        return answer

    def dfs_2(self, vertex: str, vertexes: set, parent: str, graph: dict)->bool:
        vertexes.add(vertex)
        # 1, {a)
        # 2, {a, b}
        # 3, a, b, d
        children = graph[vertex]
        # a - b, c
        # 1, b
        # b - a,d
        # 2, a - retuns nothing
        # 3, d
        # d - a, b, e
        for value in children:            
            if value in vertexes and value != parent:
                return True
            elif value not in vertexes:
                return self.dfs_2(value, vertexes, vertex, graph)
        # needs a check here or something
        return False


def main():
    directed_graph = {
        "A": ["C", "B"],
        "B": ["D"],
        "C": [],
        "D": ["A", "E"],
        "E": []
    }

    undirected_graph_true = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A"],
        "D": ["A", "B", "E"],
        "E": ["D"]
    }

    undirected_graph_false = {
            "A": ["B", "C"],
            "B": ["A", "D"],
            "C": ["A"],
            "D": ["E"],
            "E": ["D"]
        }
    # ans = Solution().dfs_solution(undirected_graph_true)
    # print(ans)
    ans2 = Solution().dfs_solution(undirected_graph_false)
    print(ans2)


if __name__ == "__main__":
    main()
