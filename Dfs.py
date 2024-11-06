from collections import defaultdict

class GraphDFS:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Undirected graph: add edges in both directions
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')

        # Recurse for all the vertices adjacent to this vertex
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


# Input section
graph_dfs = GraphDFS()
num_edges = int(input("Enter the number of edges: "))
print("Enter each edge (u, v):")
for _ in range(num_edges):
    u, v = map(int, input().split())
    graph_dfs.add_edge(u, v)

# Start DFS traversal
start_vertex = int(input("Enter the starting vertex for DFS: "))
print("Depth-First Search:")
graph_dfs.dfs(start_vertex)
print()
