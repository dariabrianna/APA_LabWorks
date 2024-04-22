import heapq
import time
import random
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    # The graph is represented as a dictionary of dictionaries,
    # where keys are nodes and values are dictionaries of neighbors and their corresponding weights
    # For example: graph = {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2, 'D': 5}, 'C': {'A': 4, 'B': 2, 'D': 1}, 'D': {'B': 5, 'C': 1}}
    
    # Distance table, initialized to infinity for all nodes
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    # Priority queue to hold all vertices that need processing
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # Nodes can only be added once to the priority queue
        if current_distance > distances[current_node]:
            continue

        # Explore each neighbor of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

   # Ensure this is at the beginning of your script or appropriately imported if defined elsewhere
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

source_node = 'A'

# Assuming dijkstra function is defined in the same file or correctly imported
shortest_paths = dijkstra(graph, source_node)
print(shortest_paths)

def generate_graph(num_vertices, num_edges, weight_range=(1, 10)):
    G = nx.gnm_random_graph(num_vertices, num_edges)
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(*weight_range)
    return G

def dijkstra_all_pairs(graph):
    return {n: nx.single_source_dijkstra_path_length(graph, n, weight='weight') for n in graph.nodes()}

# Parameters for the graphs
num_vertices_sparse = 100
num_edges_sparse = 100
num_vertices_dense = 100
num_edges_dense = 4950  # Close to V*(V-1)/2 for V=100

# Generate sparse and dense graphs
sparse_graph = generate_graph(num_vertices_sparse, num_edges_sparse)
dense_graph = generate_graph(num_vertices_dense, num_edges_dense)

# Time the Dijkstra's algorithm on sparse and dense graphs
start_time = time.time()
dijkstra_all_pairs(sparse_graph)
print("Dijkstra's on sparse graph took", time.time() - start_time, "seconds.")

start_time = time.time()
dijkstra_all_pairs(dense_graph)
print("Dijkstra's on dense graph took", time.time() - start_time, "seconds.")

def dijkstra(graph, start):
    # Initialize distances with infinity, ensuring every node is in the graph dictionary
    distances = {node: float('infinity') for node in graph.keys()}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

def generate_graph(num_vertices, num_edges):
    G = nx.gnm_random_graph(num_vertices, num_edges, directed=True)
    graph = {node: {} for node in range(num_vertices)}  # Ensure every node is represented
    for u, v in G.edges():
        weight = random.randint(1, 10)
        graph[u][v] = weight  # Only add edges that actually exist
    return graph

def dijkstra_all_pairs(graph):
    return {n: dijkstra(graph, n) for n in graph}

# Example of performance measurement and plotting setup
vertices_range = range(10, 201, 20)  # from 10 to 200 vertices in steps of 20
times_sparse = []
times_dense = []

for vertices in vertices_range:
    num_edges_sparse = vertices
    num_edges_dense = vertices * (vertices - 1) // 4

    sparse_graph = generate_graph(vertices, num_edges_sparse)
    start_time = time.time()
    dijkstra_all_pairs(sparse_graph)
    times_sparse.append(time.time() - start_time)

    dense_graph = generate_graph(vertices, num_edges_dense)
    start_time = time.time()
    dijkstra_all_pairs(dense_graph)
    times_dense.append(time.time() - start_time)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(vertices_range, times_sparse, label='Sparse Graph', marker='o')
plt.plot(vertices_range, times_dense, label='Dense Graph', marker='o')
plt.xlabel('Number of Vertices')
plt.ylabel('Time (seconds)')
plt.title('Performance of Dijkstra\'s Algorithm on Graphs')
plt.legend()
plt.grid(True)
plt.show()