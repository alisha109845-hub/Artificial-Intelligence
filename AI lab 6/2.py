class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

    def dfs_with_goal(self, start, goal):
        visited = set()
        stack = [start]
        visited.add(start)
        order = []

        while stack:
            node = stack.pop()
            order.append(node)
            print(f"Visited: {node}")

            if node == goal:
                print(f"\nGoal '{goal}' found! Stopping search.")
                break

            for neighbor in reversed(self.graph[node]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        else:
            print("\nGoal not found.")
            return

        print(f"DFS Order: {order}")

g2 = Graph()
g2.add_edge('A', ['B', 'F', 'D', 'E'])
g2.add_edge('B', ['K', 'J'])
g2.add_edge('F', [])
g2.add_edge('D', ['G'])
g2.add_edge('E', ['C', 'H', 'I'])
g2.add_edge('K', ['N', 'M'])
g2.add_edge('J', [])
g2.add_edge('G', [])
g2.add_edge('C', [])
g2.add_edge('H', [])
g2.add_edge('I', ['L'])
g2.add_edge('N', [])
g2.add_edge('M', [])
g2.add_edge('L', [])

print("DFS Search:")
g2.dfs_with_goal('A', 'G')