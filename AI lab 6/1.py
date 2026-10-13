class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

    def dfs(self, start):
        visited = set()
        stack = [start]
        visited.add(start)
        order = []

        while stack:
            node = stack.pop()
            order.append(node)
            print(f"Visited: {node}")

            for neighbor in reversed(self.graph[node]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        print(f"DFS Order: {order}")

g1 = Graph()
g1.add_edge(1, [2, 7, 8])
g1.add_edge(2, [3, 6])
g1.add_edge(3, [4, 5])
g1.add_edge(4, [])
g1.add_edge(5, [])
g1.add_edge(6, [])
g1.add_edge(7, [])
g1.add_edge(8, [9, 12])
g1.add_edge(9, [10, 11])
g1.add_edge(10, [])
g1.add_edge(11, [])
g1.add_edge(12, [])

print("DFS from 1:")
g1.dfs(1)