# Question 1
def transpose_d(di):
    transposed = {key: set() for key in di}
    for node, neighbors in di.items():
        for neighbor in neighbors:
            transposed[neighbor].add(node)
    return transposed

# Question 2
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)
    return visited

def weakly_connected(di):
    undirected = {key: set(neighbors) for key, neighbors in di.items()}
    for node, neighbors in di.items():
        for neighbor in neighbors:
            undirected[neighbor].add(node)

    start_node = next(iter(undirected))
    visited = bfs(undirected, start_node)
    return len(visited) == len(undirected)

# Question 3
def greatest_weight_d(di):
    max_weight = float('-inf')
    result = None
    
    for node, edges in di.items():
        for neighbor, weight in edges:
            if weight > max_weight:
                max_weight = weight
                result = (max_weight, node, neighbor)
    
    return result

#Question 4
import numpy as np

def incidence_to_matrix(inc):
    num_nodes = len(inc)
    num_edges = len(inc[0])

    adjacency_matrix = np.zeros((num_nodes, num_nodes), dtype=int)

    for j in range(num_edges):  
        nodes = [i for i in range(num_nodes) if inc[i][j] == 1]
        if len(nodes) == 2:
            adjacency_matrix[nodes[0]][nodes[1]] = 1
            adjacency_matrix[nodes[1]][nodes[0]] = 1  # Since it's an undirected graph

    return adjacency_matrix.tolist()

# Question 5
def dict_to_incidence(di):
    edges = []
    node_list = sorted(di.keys())
    node_index = {node: i for i, node in enumerate(node_list)}

    for node in node_list:
        for neighbor in di[node]:
            if (neighbor, node) not in edges: 
                edges.append((node, neighbor))

    num_nodes = len(node_list)
    num_edges = len(edges)
    incidence_matrix = [[0] * num_edges for _ in range(num_nodes)]

    for j, (u, v) in enumerate(edges):
        incidence_matrix[node_index[u]][j] = 1
        incidence_matrix[node_index[v]][j] = 1

    return incidence_matrix
