from collections import defaultdict


class Graph:
    def __init__(self, edges: list, directed: bool = True):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_edges(edges)

    @classmethod
    def from_txt(cls, path: str):
        """Load graph's edges from .txt file. Nodes separated by ",".

        Args:
            path (str): Path to .txt file

        Returns:
            Graph: Initialize graph with edges from file
        """
        with open(path, "r") as f:
            edges = [line.strip().split(",") for line in f.readlines()]
        return cls(edges)

    def add_edges(self, edges: list):
        """Add edges to graph

        Args:
            edges (list): List of edges
        """
        for node1, node2 in edges:
            self.add_edge(node1, node2)

    def add_edge(self, node1, node2):
        """Add edge to graph

        Args:
            node1 (Any): Node 1
            node2 (Any): Node 2
        """
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """Remove node and all references to node

        Args:
            node (Any): Node to remove
        """
        for ref_nodes in self._graph.values():
            try:
                ref_nodes.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2) -> bool:
        """Check if node1 directly connected to node2

        Args:
            node1 (Any): Node 1
            node2 (Any): Node 2

        Returns:
            bool: Is directly connected?
        """
        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path: list = []):
        """Find path from node1 to node2

        Args:
            node1 (Any): Node 1
            node2 (Any): Node 2
            path (list, optional): additional argument for recursive. Defaults to [].

        Returns:
            list: List of nodes from node1 to node2. If not found, return None.
        """
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    @property
    def nodes(self):
        """Graph's nodes

        Returns:
            list: List of nodes sorted ascending
        """
        return sorted(self._graph.keys())

    @property
    def edges(self):
        """Graph's edges

        Returns:
            list: List of edges
        """
        edges = []
        for root, nodes in self._graph.items():
            for node in nodes:
                edges.append((root, node))
        return edges

    def __str__(self):
        return "{}({})".format(self.__class__.__name__, dict(self._graph))


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
    graph = Graph(edges=word_transform_edges)
    print(graph.nodes)
