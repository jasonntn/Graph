class Vertex:
    def __init__(self, id, neighbors: list = None) -> None:
        self.id = id
        self.neighbor = {}
        if neighbors:
            for neighbor in neighbors:
                if isinstance(neighbor, tuple):
                    self.add_neighbor(*neighbor)
                else:
                    self.add_neighbor(neighbor)
        
    def add_neighbor(self, id, weight: int = 1):
        self.neighbor[id] = weight

    def __str__(self):
        return f"Vertex(id={self.id}, neighbor={list(self.neighbor.keys())})"
    
    def __eq__(self, __o: object) -> bool:
        return self.id == __o.id


class Graph:
    def __init__(self, directed: bool = False) -> None:
        self.vertex = {}
        self.directed = directed

    def add_vertex(self, vertex: Vertex):
        self.vertex[vertex.id] = vertex
        return vertex

    def __contains__(self, id):
        return self.vertex[id]

    def add_edge(self, edge: tuple):
        if edge[0] not in self.vertex:
            self.add_vertex(Vertex(edge[0]))
        if edge[1] not in self.vertex:
            self.add_vertex(Vertex(edge[1]))
        if self.directed:
            assert len(edge) == 3, "Directed graph's edge format: (vertex_id0, vertext_id1, weight)"
            self.vertex[edge[0]].add_neighbor(edge[1], edge[2])
        else:
            self.vertex[edge[0]].add_neighbor(edge[1])
            self.vertex[edge[1]].add_neighbor(edge[0])

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
            print(s_id)
            visited.append(s_id)
            for n_id in self.vertex[s_id].neighbors:
                self.dfs(n_id, visited)
            
    
    def get_partition(self):
        subgraphs = []
        current_subgraph = set()
        for vertex in self:
            if all([(v == vertex.id) or (v in vertex.neighbor.keys()) for v in current_subgraph]):
                current_subgraph.add(vertex.id)
            else:
                subgraphs.append(current_subgraph)
                current_subgraph = {vertex.id}
        subgraphs.append(current_subgraph)
        return subgraphs

    def __str__(self) -> str:
        conns = []
        for s, e in self.vertex.items():
            for n in e.neighbor.keys():
                conns.append((s, n))
        return f"Graph({conns})"
    
    def __repr__(self) -> str:
        return self.__str__()

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
    test = [("A", "B"), ("B", "C"), ("A", "C"), ("B", "E"), ("E", "D")]

    graph = Graph(directed=False)
    for edge in test:
        graph.add_edge(edge)
    print(graph)
    print(graph.get_partition())
