# we can implement graphs using tuples
class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        # print(self.edges)

    def dictify(self):
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        return self.graph_dict

    # e.g. we want to get paths between Mumbai and New York
    def get_paths(self, start, end, path=[]):
        path = path + [start]

        # return starting point of starting point is same as end point
        if start == end:
            return [path]

        # return [] if the starting point has no routes
        if start not in self.graph_dict:
            return []
        paths = []
        # explore all routes per city, e.g. all routes from Mumbai
        # here e.g. for Mumbai, node is Paris and Dubai
        for node in self.graph_dict[start]:
            if node not in path:  # we need to check if the destination has been visited or not
                # call the function recursively, e.g. now I want to get how many paths are there from paris to New York
                # whatever paths you get, you need to supply the first path wich is Mumbai
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    # shortest path

    def get_shortest_path(self, start, end):
        path = []
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None

        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
    }

    route_graph = Graph(routes)

print(route_graph.dictify())

start = "Mumbai"
end = "New York"
print(f"paths between {start} and {end}: ", route_graph.get_paths(start, end))
print(route_graph.get_shortest_path(start, end))
