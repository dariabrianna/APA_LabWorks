
import time
import random
import networkx as nx
import matplotlib.pyplot as plt
import networkx as nx

def kruskal(graph):
    graph_nx = nx.Graph(graph)  # Convert input graph to NetworkX graph
    mst_edges = list(nx.minimum_spanning_edges(graph_nx, algorithm='kruskal', data=False))
    return mst_edges

# Example usage:
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 4, 'D': 5},
    'C': {'A': 3, 'B': 4, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

minimum_spanning_tree = kruskal(graph)
print(minimum_spanning_tree)




def generate_graph(num_vertices, num_edges, weight_range=(1, 10)):
    G = nx.gnm_random_graph(num_vertices, num_edges)
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(*weight_range)
    return G

def kruskal(graph):
    return list(nx.minimum_spanning_edges(graph, algorithm='kruskal', data=False))

# Parameters for the graphs
num_vertices_range = range(10, 201, 20)  # From 10 to 200 vertices, in steps of 20
num_edges_sparse = 10
num_edges_dense = 100

# Measurement storage
times_kruskal_sparse = []
times_kruskal_dense = []

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

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(num_vertices_range, times_kruskal_sparse, label='Kruskal Sparse', marker='o')
plt.plot(num_vertices_range, times_kruskal_dense, label='Kruskal Dense', marker='o')
plt.xlabel('Number of Vertices')
plt.ylabel('Time (seconds)')
plt.title('Performance of Kruskal\'s Algorithm')
plt.legend()
plt.grid(True)
plt.show()
