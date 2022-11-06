class Graph:
    def __init__(self, edges) -> None:
        self.path_dict = {}
        self.edges = edges
        for start, end in self.edges:
            if start in self.path_dict:
                self.path_dict[start].append(end)
            else:
                self.path_dict[start] = [end]

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]

        if start not in self.path_dict:
            return []

        paths = []
        for node in self.path_dict[start]:
            if node not in path: # only interested in unvisited nodes.
                new_path = self.get_paths(node, end, path)
                for p in new_path:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]

        if start not in self.path_dict:
            return []

        shortest_path = []
        for node in self.path_dict[start]:
            if node not in path: # only interested in unvisited nodes.
                new_path = self.get_shortest_path(node, end, path)
                if new_path:
                    if shortest_path is None or len(new_path) < len(shortest_path):
                        shortest_path = new_path
        return new_path

        

if __name__ == "__main__":
    # I want to represent routes as smth immutable --> I will use tuples.

    routes = [
        ("Warsaw", "Paris"),
        ("Warsaw", "London"),
        ("Paris", "London"),
        ("London", "New York")
    ]

    graph_paths = Graph(routes)

    # Graphs like trees are recursive data strcutres. Hence, to get paths from a starting point to an end point,
    # we will use recursion.
    start = "Warsaw"
    end = "New York"

    print(f"Possible routes from {start} to {end}: {graph_paths.get_paths(start, end)}")

    # Now, let's find the shortest path.

    print(f"The shortest path from {start} to {end}: {graph_paths.get_shortest_path(start, end)}")




