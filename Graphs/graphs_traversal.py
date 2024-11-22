class Graph:
    def __init__(self, graph):
        self.graph = graph

    def BFS(self, start_node):
        visited = []  # keep track of the nodes we've visited
        queue = []
        queue.append(start_node)
        while queue:
            node = queue.pop(0)  # dequeue a node from front of queue
            # print(node)
            if node not in visited:
                visited.append(node)  # mark the node as visited
                for item in graph[node]:
                    if item not in visited:
                        queue.append(item)

        return visited

    def oldDFS(self, start):
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                stack.extend(graph[node])
        return (stack)

    def DFS(self, node, visited=None):
        if visited is None:
            visited = []
        results = []
        if node not in visited:
            results.append(node)
            visited.append(node)
            for node in graph[node]:
                if node not in visited:
                    results.extend(self.DFS(node, visited))
                    print(results)
                    # res = self.DFS(node, visited)
                    # order.extend(res)

        return results


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

graphs = {
    'Mumbai': ['Paris', 'Dubai'],
    'Paris': ['Dubai', 'New York'],
    'Dubai': ['New York'],
    'New York': ['Toronto']
}

# newGraph = Graph(graph)
newGraph = Graph(graph)
# print(newGraph)
# print(newGraph.BFS('A'))
print(newGraph.DFS('A'))

# queue = [1, 2]
# node = queue.pop()
# queue = queue.extend(graph[node])

# BFS(graph, 'Á')
