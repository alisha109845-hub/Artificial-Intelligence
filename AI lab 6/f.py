class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

    # Normal DFS
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

    # DFS with Goal
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

# ---------- Question 1: Walkthrough Graph (1-12) ----------
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

print("Q1 - DFS from 2:")
g1.dfs(2)

# ---------- Question 2: Practice Task (A-G) ----------
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

print("\nQ2 - DFS without Goal (full traversal from A):")
g2.dfs('A')

print("\nQ2 - DFS with Goal G:")
g2.dfs_with_goal('A', 'Z')