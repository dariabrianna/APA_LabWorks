import time
import random
import matplotlib.pyplot as plt
import heapq
import networkx as nx

def prim(graph, start_node):
    # Initialize an empty set to keep track of visited nodes
    visited = set()
    # Initialize a priority queue to store edges with their weights
    priority_queue = [(0, start_node, None)]
    # Initialize an empty list to store the minimum spanning tree edges
    mst_edges = []

    while priority_queue:
        # Pop the edge with the minimum weight
        weight, current_node, parent_node = heapq.heappop(priority_queue)

        # Check if the current node has been visited
        if current_node not in visited:
            # Mark the current node as visited
            visited.add(current_node)
            # Add the edge to the minimum spanning tree
            if parent_node is not None:
                mst_edges.append((parent_node, current_node, weight))
            # Explore neighbors of the current node
            for neighbor, edge_data in graph[current_node].items():
                neighbor_weight = edge_data['weight']
                # Add unvisited neighbors to the priority queue
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (neighbor_weight, neighbor, current_node))

    return mst_edges

# Example usage:
graph = {
    'A': {'B': {'weight': 2}, 'C': {'weight': 3}},
    'B': {'A': {'weight': 2}, 'C': {'weight': 4}, 'D': {'weight': 5}},
    'C': {'A': {'weight': 3}, 'B': {'weight': 4}, 'D': {'weight': 1}},
    'D': {'B': {'weight': 5}, 'C': {'weight': 1}}
}

start_node = 'A'
minimum_spanning_tree = prim(graph, start_node)
print(minimum_spanning_tree)

def generate_graph(num_vertices, num_edges, weight_range=(1, 10)):
    G = nx.gnm_random_graph(num_vertices, num_edges)
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(*weight_range)
    return G

def kruskal(graph):
    return list(nx.minimum_spanning_edges(graph, algorithm='kruskal', data=False))

def prim(graph, start_node):
    return list(nx.minimum_spanning_edges(graph, algorithm='prim', data=False))

# Parameters for the graphs
num_vertices_range = range(10, 201, 20)  # From 10 to 200 vertices, in steps of 20
num_edges_sparse = 10
num_edges_dense = 100

# Measurement storage
times_kruskal_sparse = []
times_kruskal_dense = []
times_prim_sparse = []
times_prim_dense = []

# Performance measurement
for num_vertices in num_vertices_range:
    sparse_graph = generate_graph(num_vertices, num_edges_sparse)
    dense_graph = generate_graph(num_vertices, num_edges_dense)

    start_time = time.time()
    kruskal(sparse_graph)
    times_kruskal_sparse.append(time.time() - start_time)

    start_time = time.time()
    kruskal(dense_graph)
    times_kruskal_dense.append(time.time() - start_time)

    start_time = time.time()
    prim(sparse_graph, random.choice(list(sparse_graph.nodes())))
    times_prim_sparse.append(time.time() - start_time)

    start_time = time.time()
    prim(dense_graph, random.choice(list(dense_graph.nodes())))
    times_prim_dense.append(time.time() - start_time)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(num_vertices_range, times_kruskal_sparse, label='Kruskal Sparse', marker='o')
plt.plot(num_vertices_range, times_kruskal_dense, label='Kruskal Dense', marker='o')
plt.plot(num_vertices_range, times_prim_sparse, label='Prim Sparse', marker='o')
plt.plot(num_vertices_range, times_prim_dense, label='Prim Dense', marker='o')
plt.xlabel('Number of Vertices')
plt.ylabel('Time (seconds)')
plt.title('Performance of Kruskal\'s and Prim\'s Algorithms')
plt.legend()
plt.grid(True)
plt.show()
