class Graph:
    def __init__(self, graph):
        self.graph = graph

    def BFS(self, start_node):
        visited = []
        queue = []
        queue.append(start_node)
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                for item in graph[node]:
                    if item not in visited:
                        queue.append(item)
        return visited


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

newGraph = Graph(graph)
print(newGraph.BFS('A'))
