# ---------------------------------------------------------------------------------------------------------------------
# Graph Data Structure:
# ---------------------------------------------------------------------------------------------------------------------
# Links connecting two 'Nodes' are called 'Edges'.
# Trees have only one path between two nodes. Graphs may have multiple paths. Tree is a special type of Graph
# ---------------------------------------------------------------------------------------------------------------------
# Types:
# 1. Undirected graph
# 2. Directed graph (Edges may be weighted or unweighted)
# ---------------------------------------------------------------------------------------------------------------------
# Uses:
# 1. Friend suggestions
# 2. Product Recommendation
# 3. Maps, Flight Routes (Directed Graph)
# 4. Network Topology
# ---------------------------------------------------------------------------------------------------------------------
class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print('Graph Dict: ', self.graph_dict)

    def get_paths(self, start, end, path=[]):   # path is the list that holds the intermediate paths during recursion
        path = path + [start]
        if start == end:
            return path

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:                     # e.g. for ['Paris', 'Dubai'] in 'Mumbai'
            if node not in path:                                # check if the destination is not already visited
                new_paths = self.get_paths(node, end, path)     # get new paths between 'node' and 'end'
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path=path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path


if __name__ == '__main__':

    # routes = [
    #     ('Mumbai', 'Pune'),
    #     ('Mumbai', 'Surat'),
    #     ('Surat', 'Bangaluru'),
    #     ('Pune', 'Hyderabad'),
    #     ('Pune', 'Mysuru'),
    #     ('Hyderabad', 'Bangaluru'),
    #     ('Hyderabad', 'Chennai'),
    #     ('Mysuru', 'Bangaluru'),
    #     ('Chennai', 'Bangaluru')
    # ]

    routes = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto'),
    ]

    route_graph = Graph(edges=routes)
    start = 'Paris'
    end = 'New York'

    print(f'Paths between {start} and {end} are: ', route_graph.get_paths(start=start, end=end))
    print(f'Shortest Path between {start} and {end} is: ', route_graph.get_shortest_path(start=start, end=end))
