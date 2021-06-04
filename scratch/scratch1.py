class Solution:
    # infinite loop bc our conditions continue to route to a return function
    # 
    def __helperbad(self, graph, vertex, parent, visited):
        visited[vertex]=True
        for edge in graph[vertex]:
            if edge in visited and edge!=parent:
                return True
            else:
                return self.__helper(graph, edge, vertex, visited)


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
        "D": ["B", "A", "E"],
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
    x=Solution()
    print(x.answer(undirected_graph_true))

main()




def fib(n):
    if n<=2:
        return 1
    first=0
    second=1
    for i in range(2, n+1):
        first, second = second, first+second
    return second

# print(fib(3))