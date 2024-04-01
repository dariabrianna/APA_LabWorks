import time
import matplotlib.pyplot as plt
import pandas as pd
from networkx.generators.random_graphs import erdos_renyi_graph
from collections import defaultdict, deque

class DepthFirstSearch:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        self._dfs_util(start, visited)

    def _dfs_util(self, node, visited):
        visited.add(node)
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                self._dfs_util(neighbour, visited)

class BreadthFirstSearch:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        queue = deque([start])
        max_node = max(self.graph.keys(), default=-1)
        visited = [False] * (max_node + 1)
        visited[start] = True
        while queue:
            node = queue.popleft()
            for neighbour in self.graph[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)

# Parameters for the experiment
values = [4, 8, 16, 32, 64, 128, 256, 512]
times_dfs = []
times_bfs = []

# Running DFS and BFS experiments
for num_nodes in values:
    g = erdos_renyi_graph(num_nodes, 0.5)

    # Depth First Search
    dfs_graph = DepthFirstSearch()
    for node, edge in g.edges:
        dfs_graph.add_edge(node, edge)
    start_time = time.perf_counter()
    dfs_graph.dfs(0)
    times_dfs.append(time.perf_counter() - start_time)

    # Breadth First Search
    bfs_graph = BreadthFirstSearch()
    for node, edge in g.edges:
        bfs_graph.add_edge(node, edge)
    start_time = time.perf_counter()
    bfs_graph.bfs(0)
    times_bfs.append(time.perf_counter() - start_time)

# Plotting performance comparison
plt.figure(figsize=(12, 6))
plt.plot(values, times_dfs, label="DFS Time", marker='o')
plt.plot(values, times_bfs, label="BFS Time", marker='x')
plt.xlabel('Number of Nodes')
plt.ylabel('Time (seconds)')
plt.title('Performance of Graph Traversal Algorithms')
plt.legend()
plt.show()

# Displaying times in a DataFrame
data = list(zip(values, times_dfs, times_bfs))
df = pd.DataFrame(data, columns=["Number of Nodes", "DFS Time (s)", "BFS Time (s)"])
print(df)
