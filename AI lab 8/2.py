# A* Search - f(n) = g(n) + h(n)
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

h = {'Arad':366, 'Sibiu':253, 'Fagaras':176, 'Rimnicu':193,
     'Pitesti':100, 'Timisoara':329, 'Lugoj':244, 'Mehadia':241,
     'Drobeta':242, 'Craiova':160, 'Zerind':374, 'Oradea':380, 'Bucharest':0}

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]  # (f, g, node, path)
    visited = {}
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node in visited and visited[node] <= g: continue
        visited[node] = g
        print(f"Visited: {node}, g={g}, h={h[node]}, f={f}, Path: {path}")
        if node == goal:
            return path, g
        for neighbor, cost in graph.get(node, []):
            new_g = g + cost
            new_f = new_g + h[neighbor]
            heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))
    return None, 0

path, cost = astar('Pitesti', 'Bucharest')
print(f"\nA* Path: {path}, Total Cost: {cost}")