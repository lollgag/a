from collections import defaultdict, deque

class GraphBFS:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Undirected graph: add edges in both directions
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            # Add all unvisited neighbors to the queue
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


# Input section with error handling
graph_bfs = GraphBFS()
while True:
    try:
        num_edges = int(input("Enter the number of edges: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer for the number of edges.")

print("Enter each edge (u, v):")
for _ in range(num_edges):
    while True:
        try:
            u, v = map(int, input().split())
            graph_bfs.add_edge(u, v)
            break
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")

# Start BFS traversal
while True:
    try:
        start_vertex = int(input("Enter the starting vertex for BFS: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer for the starting vertex.")

print("Breadth-First Search:")
graph_bfs.bfs(start_vertex)
print()
