# Greedy Best First Search - f(n) = h(n)
import heapq

graph = {
    'Arad': [('Sibiu', 140), ('Timisoara', 118), ('Zerind', 75)],
    'Sibiu': [('Fagaras', 99), ('Rimnicu', 80)],
    'Fagaras': [('Bucharest', 211)],
    'Rimnicu': [('Pitesti', 97)],
    'Pitesti': [('Bucharest', 101)],
    'Timisoara': [('Lugoj', 111)],
    'Lugoj': [('Mehadia', 70)],
    'Mehadia': [('Drobeta', 75)],
    'Drobeta': [('Craiova', 120)],
    'Craiova': [('Pitesti', 138)],
    'Zerind': [('Oradea', 71)],
    'Oradea': [('Sibiu', 151)],
    'Bucharest': []
}

# Heuristic - straight line distance to Bucharest
h = {'Arad':366, 'Sibiu':253, 'Fagaras':176, 'Rimnicu':193,
     'Pitesti':100, 'Timisoara':329, 'Lugoj':244, 'Mehadia':241,
     'Drobeta':242, 'Craiova':160, 'Zerind':374, 'Oradea':380, 'Bucharest':0}

def greedy(start, goal):
    pq = [(h[start], start, [start])]  # (h, node, path)
    visited = set()
    while pq:
        _, node, path = heapq.heappop(pq)
        if node in visited: continue
        visited.add(node)
        print(f"Visited: {node}, h = {h[node]}, Path: {path}")
        if node == goal:
            return path
        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (h[neighbor], neighbor, path + [neighbor]))
    return None

print("Greedy Path:", greedy('Arad', 'Bucharest'))