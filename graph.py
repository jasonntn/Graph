from typing import Dict, Any

class Vertex:
    def __init__(self, id) -> None:
        self.id = id
        self.neighbor = {}
        
    def add_neighbor(self, id, weight: int = 0):
        self.neighbor[id] = weight

    def __str__(self):
        return str(self.id) + ' <-> ' + str([x.id for x in self.neighbor])

    @property
    def neighbors(self):
        return self.neighbor.keys()


class Graph:
    def __init__(self) -> None:
        self.vertex = {}

    def add_vertex(self, id):
        vertex = Vertex(id)
        self.vertex[id] = vertex
        return vertex

    def get_vertex(self, id):
        if id in self.vertex:
            return self.vertex[id]

    def __contains__(self, id):
        return self.vertex[id]

    def add_edge(self, id0, id1, weight: int = 0):
        if id0 not in self.vertex:
            self.add_vertex(id0)
        if id1 not in self.vertex:
            self.add_vertex(id1)
        self.vertex[id0].add_neighbor(id1, weight)

    @property
    def vertices(self):
        return self.vertex.keys()

    def __iter__(self):
        return iter(self.vertex.values())

    def bfs(self, s_id):
        visited = [s_id]
        queue = [s_id]
 
        while queue:
            r_id = queue.pop(0)
            print(r_id)
            for n_id in self.vertex[r_id].neighbors:
                if n_id not in visited:
                    queue.append(n_id)
                    visited.append(n_id)
    
    def dfs(self, s_id, visited: list):
        if s_id not in visited:
            print(s_id, " ")
            visited.append(s_id)
            for n_id in self.vertex[s_id].neighbors:
                self.dfs(n_id, visited)


if __name__ == "__main__":
    directed_edges = [
        (0, 5),
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 5),
        (3, 4),
        (4, 0),
        (5, 4),
        (5, 2),
    ]
    word_transform_edges = [
        ("FOOD", "FOOT"),
        ("FOOD", "GOOD"),
        ("FOOD", "FOOL"),
        ("FOOT", "FORT"),
        ("FOOT", "FOOD"),
        ("FORT", "FOOT"),
        ("GOOD", "FOOD"),
        ("FOOL", "FOOD"),
        ("FOOL", "POOL"),
        ("POOL", "POLL"),
        ("POOL", "FOOL"),
        ("POLL", "POLE"),
        ("POLL", "POOL"),
        ("POLE", "POLL"),
        ("POLE", "PALE"),
        ("PALE", "SALE"),
        ("PALE", "POLE"),
        ("PALE", "SAGE"),
        ("PALE", "PALM"),
        ("PALM", "PALE"),
        ("SALE", "PALE"),
        ("SAGE", "SALT"),
        ("SAGE", "PALE"),
        ("SALT", "SAGE"),
    ]
    test = [
        (0, 1),
        (0, 2),
        (1, 2),
        (2, 0),
        (2, 3),
        (3, 3)
    ]
    graph = Graph()
    for edge in test:
        graph.add_edge(*edge)
    graph.bfs(2)
    graph.dfs(2, [])
