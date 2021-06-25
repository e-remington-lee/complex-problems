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
            # just making sure I understand the problem better, I know that if I do not have this check in here, I need to reset the 
            # visited graph each time or the integrity of the search is compromisd bc it carries over for each loop
            if not visited[vertex]:
            # visited = defaultdict(lambda: False)
                if self.__cyclic_helper(vertex, visited, ""):
                    return True
        return False

    def __cyclic_helper(self, vertex, visited, parent):
        visited[vertex]=True
        for i in self.graph[vertex]:
            if visited[i] and parent!=i:
                return True
            if not visited[i]:
                if self.__cyclic_helper(i, visited, vertex):
                    return True
            # if not visited[i]:
            #     if self.__cyclic_helper(i, visited, vertex):
            #         return True
            # elif parent!=i:
            #     return True
        return False

    def directed_cycle_no_back_edge(self):
        recent_stack = defaultdict(lambda: False)
        for vertex in self.graph.keys():
            '''
            We need to reset the recent/visited stacks with each loop. If we have:
            directed_graph_false2 = {
                "C": ["A", "B"],
                "B": ["A"],
                "A": ["C"]
            }
            and we do not reset the stacks, C->A->C is false bc C is A's parent. If we did not reset them, then when we have B->A, A is in seen and 
            is not in the recent_stack, so it will not continue. If it did continue we would find a cycle bc B->A->C-B is a cycle. So we need to reset
            them each time. This makes sense bc in a directed graph, searching from each node can deliver different results
            '''
            visited = defaultdict(lambda: False)
            if not visited[vertex]:
                if self.directed_helper(vertex, visited, recent_stack, ""):
                    return True
        return False

    def directed_helper(self, vertex, visited, recent_stack, parent):
        visited[vertex], recent_stack[vertex] = True, True
        for node in self.graph[vertex]:
            if not visited[node]:
                if self.directed_helper(node, visited, recent_stack, vertex):
                    return True
            elif recent_stack[node] and parent!=node:
                return True
            # if visited[node] and recent_stack[node] and parent is not node:
            #     return True
            # elif not visited[node]:
            #     if self.directed_helper(node, visited, recent_stack, vertex):
            #         return True
        recent_stack[vertex]=False
        return False

    def directed_cycle_with_back_edge(self):
        visited = defaultdict(lambda: False)
        recent_stack = defaultdict(lambda: False)       
        for vertex in self.graph.keys():    
            if self.directed_helper_with_back_edge(vertex, visited, recent_stack):
                return True
        return False

    def directed_helper_with_back_edge(self, vertex, visited, recent_stack):
        visited[vertex], recent_stack[vertex] = True, True
        for node in self.graph[vertex]:
            if not visited[node]:
                if self.directed_helper_with_back_edge(node, visited, recent_stack):
                    return True
            elif recent_stack[node]:
                return True
            # if visited[node] and recent_stack[node] and parent is not node:
            #     return True
            # elif not visited[node]:
            #     if self.directed_helper_with_back_edge(node, visited, recent_stack, vertex):
            #         return True
        recent_stack[vertex]=False
        return False

    def answer(self, graph):
        visited={}
        for vertex in graph.keys():
            if vertex not in visited:
                if self.__helper(graph, vertex, "", visited):
                    return True
        return False
            
    def __helper(self, graph, vertex, parent, visited):
        visited[vertex]=True
        for edge in graph[vertex]:
            if edge not in visited:
                if self.__helper(graph, edge, vertex, visited):
                    return True
            elif edge!=parent:
                return True
        return False


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
    directed_graph_false = {
        "A": ["C", "B"],
        "B": ["D"],
        "C": [],
        "D": ["B", "E"],
        "E": []
    }
    directed_graph_true = {
        "C": ["A", "B"],
        "B": ["A"],
        "A": ["C"]
    }
    directed_graph_false = {
        "C": ["A", "B"],
        "B": ["A"],
        "A": []
    }
    directed_graph_true_back_edge = {
        "C": ["A", "B"],
        "B": [],
        "A": ["C"]
    }
    x = Graph(undirected_graph_true).undirected_cycle()
    print(x)
    x = Graph(directed_graph_true).directed_cycle_no_back_edge()
    print(x)
    x = Graph(directed_graph_false).directed_cycle_with_back_edge()
    print(x)
    # x = Graph(directed_graph_true_back_edge).directed_cycle_with_back_edge()
    # print(x)
    # x = Graph(directed_graph_true_back_edge).directed_cycle_no_back_edge()
    # print(x)


if __name__ == "__main__":
    main()
