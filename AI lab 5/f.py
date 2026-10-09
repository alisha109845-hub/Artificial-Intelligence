from collections import deque

class Graph:
    def __init__(self):
        # Adjacency list to store the graph
        self.graph = {}

    def add_edge(self, node, neighbors):
        # Add a node and its neighbors to the graph
        self.graph[node] = neighbors

    # Task 1: Normal BFS
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        order = [] # to store BFS order

        while queue:
            node = queue.popleft()
            order.append(node)
            print(f"Visited: {node}") # changed

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print(f"BFS Order: {order}") # added

    # Task 2: BFS with Goal
    def bfs_with_goal(self, start, goal):
        visited = set()
        queue = deque([start])
        visited.add(start)
        order = [] # to store BFS order

        while queue:
            node = queue.popleft()
            order.append(node)
            print(f"Visited: {node}") # changed

            if node == goal:
                print(f"\nGoal '{goal}' found! Stopping search.") # changed
                break

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        else:
            print("\nGoal not found.")
            return

        print(f"BFS Order: {order}") # added

g1 = Graph()
g1.add_edge(0, [1, 4])
g1.add_edge(1, [0, 4, 3, 2])
g1.add_edge(2, [1, 3])
g1.add_edge(3, [1, 2, 4])
g1.add_edge(4, [0, 1, 3])

print("BFS from 0:")
g1.bfs(0)

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

print("\nBFS Search:")
g2.bfs_with_goal('A', 'G')