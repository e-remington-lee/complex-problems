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
# https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
# https://www.youtube.com/watch?v=HDUzBEG1GlA
from collections import defaultdict

#TODO do with BFS and DFS, also make sure to do this better
# time is O vertexes+edges. It looks like n^2, it traverses through each vertex+their edge, each vertex does not see each edge
# space is linear to how many vertexes we have.
class Graph(object):
    def __init__(self, graph:dict=defaultdict(list)):
        super().__init__()      
        self.graph = graph

    def add_edge(self, x, y):
        self.graph[x].append(y)
        self.graph[y].append(x)

    def undirected_cycle(self):
        # visited={x:False for x in self.graph.keys()}
        visited = defaultdict(lambda: False)
        for vertex in self.graph.keys():
            if not visited[vertex]:
                if self.__cyclic_helper(vertex, visited, ""):
                    return True
        return False

    def __cyclic_helper(self, vertex, visited, parent):
        visited[vertex]=True
        for i in self.graph[vertex]:
            if not visited[i]:
                if self.__cyclic_helper(i, visited, vertex):
                    return True
            elif parent!=i:
                return True
        return False

    def directed_cycle(self):
        return self.undirected_cycle()

def main():
    undirected_graph_true = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A"],
        "D": ["A", "B", "E"],
        "E": ["D"]
    }
    undirected_graph_false = {
            "A": ["B", "C"],
            "B": ["D", "A"],
            "D": ["B"],
            "C": ["A"]
        }
    directed_graph_true = {
        "A": ["C", "B"],
        "B": ["D"],
        "C": [],
        "D": ["A","B", "E"],
        "E": []
    }
    directed_graph_false = {
        "A": ["C", "B"],
        "B": ["D"],
        "C": [],
        "D": ["B", "E"],
        "E": []
    }
    x = Graph(undirected_graph_false).undirected_cycle()
    print(x)
    x = Graph(directed_graph_false).directed_cycle()
    print(x)



if __name__ == "__main__":
    main()
