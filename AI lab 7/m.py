class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

    def DLS(self, src, target, limit, path, visited_order):
        visited_order.append(src)
        path.append(src)
        
        if src == target:
            return True
        if limit <= 0:
            path.pop()
            return False
            
        for child in self.graph.get(src, []):
            if self.DLS(child, target, limit-1, path, visited_order):
                return True
        path.pop()
        return False

    def IDDFS(self, src, target, max_depth):
        for limit in range(max_depth+1):
            visited_order = []
            path = []
            found = self.DLS(src, target, limit, path, visited_order)
            print(f"IDDFS Limit {limit}:")
            print(f"  Visited Order: {' -> '.join(visited_order)}")
            print(f"  Path: {path}")
            print(f"  Found: {found}\n")
            if found:
                print(f"GOAL FOUND! Final Path: {' -> '.join(path)}")
                return path
        return None

# ---------- Task Tree: Start A, Goal G ----------
g = Graph()
g.add_edge('A', ['B','F','D','E'])
g.add_edge('B', ['K','J'])
g.add_edge('F', [])
g.add_edge('D', ['G'])
g.add_edge('E', ['C','H','I'])
g.add_edge('K', ['N','M'])
g.add_edge('J', [])
g.add_edge('G', [])
g.add_edge('C', [])
g.add_edge('H', [])
g.add_edge('I', ['L'])
g.add_edge('N', [])
g.add_edge('M', [])
g.add_edge('L', [])

# --- Testing DLS ---
print("======== DEPTH LIMITED SEARCH (DLS) ========")
for lim in [0,1,2,3]:
    v = []
    p = []
    found = g.DLS('A','G',lim, p, v)
    print(f"DLS Limit {lim}: Visited={' -> '.join(v)} | Found={found} | Path={p}")

print("\n======== ITERATIVE DEEPENING SEARCH (IDDFS) ========")
g.IDDFS('A','G',3)