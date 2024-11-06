import heapq
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = defaultdict(list)  # Adjacency list to store the graph

    def add_edge(self, u, v, weight):
        # Since the graph is undirected, add edges in both directions
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def prim_mst(self):
        # Priority queue to store (weight, vertex) and start from vertex 0
        min_heap = [(0, 0)]  # Start from vertex 0 with 0 weight
        visited = set()
        total_weight = 0  # To store total weight of MST

        print("Edges in the Minimum Spanning Tree:")

        while min_heap and len(visited) < self.V:
            weight, u = heapq.heappop(min_heap)

            # If the vertex is already in the MST, skip it
            if u in visited:
                continue

            # Add the edge to the MST
            visited.add(u)
            total_weight += weight
            print(f"Included vertex: {u} with edge weight: {weight}")

            # Check all adjacent vertices
            for v, w in self.graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (w, v))

        print(f"\nTotal weight of MST: {total_weight}")


# Input section
num_vertices = int(input("Enter the number of vertices: "))
graph = Graph(num_vertices)

num_edges = int(input("Enter the number of edges: "))
print("Enter each edge (u, v, weight):")
for _ in range(num_edges):
    u, v, weight = map(int, input().split())
    graph.add_edge(u, v, weight)

# Find and display the MST
print("\nPerforming Prim's Algorithm to find Minimum Spanning Tree:")
graph.prim_mst()
