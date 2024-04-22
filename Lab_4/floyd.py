import time
import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def generate_sparse_graph():
    G = nx.DiGraph()
    G.add_edge('A', 'B', weight=2)
    G.add_edge('A', 'C', weight=5)
    G.add_edge('B', 'C', weight=1)
    G.add_edge('C', 'D', weight=2)
    return G

def generate_dense_graph():
    G = nx.DiGraph()
    G.add_edge('A', 'B', weight=3)
    G.add_edge('B', 'A', weight=1)
    G.add_edge('A', 'C', weight=7)
    G.add_edge('B', 'C', weight=1)
    G.add_edge('C', 'D', weight=1)
    G.add_edge('D', 'A', weight=5)
    G.add_edge('B', 'D', weight=2)
    G.add_edge('D', 'B', weight=3)
    return G

def floyd_warshall_nx(graph):
    return nx.floyd_warshall_numpy(graph, weight='weight')

# Generate sparse and dense graphs
sparse_graph = generate_sparse_graph()
dense_graph = generate_dense_graph()

# Execute Floyd-Warshall on both graphs and print the results
fw_result_sparse = floyd_warshall_nx(sparse_graph)
fw_result_dense = floyd_warshall_nx(dense_graph)

print("Shortest paths in the sparse graph:")
print(fw_result_sparse)

print("\nShortest paths in the dense graph:")
print(fw_result_dense)


def generate_graph(num_vertices, num_edges, weight_range=(1, 10)):
    """
    Generates a random graph with the specified number of vertices and edges.
    Weights are randomly assigned within the specified range.
    """
    G = nx.gnm_random_graph(num_vertices, num_edges, directed=True)
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(*weight_range)
    return G

def floyd_warshall_nx(graph):
    """
    Executes the Floyd-Warshall algorithm using NetworkX's built-in function
    and returns the shortest path distance matrix.
    """
    return nx.floyd_warshall_numpy(graph, weight='weight')

# Graph parameters
num_vertices_sparse = 100
num_edges_sparse = 100  # Sparse graph: number of edges is close to the number of vertices
num_vertices_dense = 100
num_edges_dense = 4950  # Dense graph: number of edges close to V*(V-1)/2 for an undirected graph

# Generate sparse and dense graphs
sparse_graph = generate_graph(num_vertices_sparse, num_edges_sparse)
dense_graph = generate_graph(num_vertices_dense, num_edges_dense)

# Timing the Floyd-Warshall algorithm on the sparse graph
start_time = time.time()
fw_result_sparse = floyd_warshall_nx(sparse_graph)
print("Floyd-Warshall on sparse graph took", time.time() - start_time, "seconds.")

# Timing the Floyd-Warshall algorithm on the dense graph
start_time = time.time()
fw_result_dense = floyd_warshall_nx(dense_graph)
print("Floyd-Warshall on dense graph took", time.time() - start_time, "seconds.")

def generate_graph(num_vertices, density='sparse'):
    G = nx.gnm_random_graph(num_vertices, num_vertices if density == 'sparse' else (num_vertices * (num_vertices - 1)) // 2, directed=True)
    for u, v in G.edges():
        G.edges[u, v]['weight'] = 1  # Assign a uniform weight for simplicity
    return G

def floyd_warshall_nx(graph):
    start_time = time.time()
    nx.floyd_warshall_numpy(graph, weight='weight')
    return time.time() - start_time

# Parameters
vertex_counts = range(5, 101, 5)  # From 5 to 100 vertices, in steps of 5

# Measurement storage
times_sparse = []
times_dense = []

# Performance measurement
for count in vertex_counts:
    sparse_graph = generate_graph(count, 'sparse')
    dense_graph = generate_graph(count, 'dense')
    times_sparse.append(floyd_warshall_nx(sparse_graph))
    times_dense.append(floyd_warshall_nx(dense_graph))

# Plotting the results
plt.figure(figsize=(10, 5))
plt.plot(vertex_counts, times_sparse, label='Sparse Graph', marker='o')
plt.plot(vertex_counts, times_dense, label='Dense Graph', marker='o')
plt.xlabel('Number of Vertices')
plt.ylabel('Time in seconds')
plt.title('Performance of Floyd-Warshall Algorithm')
plt.legend()
plt.grid(True)
plt.show()
