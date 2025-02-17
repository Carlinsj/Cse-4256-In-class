import numpy as np
from collections import deque

# Question 1
def cycle_m(n):
    mat = np.zeros((n, n), dtype=int)
    for i in range(n):
        mat[i][(i + 1) % n] = 1  # Connect to next node
        mat[i][(i - 1) % n] = 1  # Connect to previous node
    return mat.tolist()

# Question 2
def cycle_d(n):
    graph = {i: {(i - 1) % n, (i + 1) % n} for i in range(n)}
    return graph

# Question 3
def is_regular_m(mat):
    degrees = [sum(row) for row in mat]
    return all(deg == degrees[0] for deg in degrees)

# Question 4
def is_regular_d(di):
    degrees = {len(neighbors) for neighbors in di.values()}
    return len(degrees) == 1

# Question 5
def complete_bipartite_d(m, n):
    graph = {i: set(range(m, m + n)) for i in range(m)}
    for j in range(m, m + n):
        graph[j] = set(range(m))
    return graph

# Question 6
def complete_bipartite_m(m, n):
    size = m + n
    mat = np.zeros((size, size), dtype=int)
    for i in range(m):
        for j in range(m, size):
            mat[i][j] = 1
            mat[j][i] = 1
    return mat.tolist()

# Question 7
def di_to_mat(di):
    size = max(di.keys()) + 1
    mat = np.zeros((size, size), dtype=int)
    for node, neighbors in di.items():
        for neighbor in neighbors:
            mat[node][neighbor] = 1
    return mat.tolist()

# Question 8
def bfs_m(mat, start_node=0):
    n = len(mat)
    distances = [-1] * n  # -1 means unvisited
    queue = deque([start_node])
    distances[start_node] = 0
    while queue:
        node = queue.popleft()
        for neighbor, connected in enumerate(mat[node]):
            if connected and distances[neighbor] == -1:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)

    return distances
