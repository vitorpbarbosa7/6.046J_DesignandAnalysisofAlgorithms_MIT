import math

def high(x, u):
    return x // int(math.sqrt(u))

def low(x, u):
    return x % int(math.sqrt(u))

def index(i, j, u):
    return i * int(math.sqrt(u)) + j

def is_base_case(cluster):
    return isinstance(cluster, list)

def linear_successor(cluster, x):
    for i in range(x + 1, len(cluster)):
        if cluster[i] == 1:
            return i
    return float('inf')

def successor(V, x, u):
    i = high(x, u)
    j = low(x, u)

    if is_base_case(V['cluster'][i]):
        j = linear_successor(V['cluster'][i], j)
    else:
        j = successor(V['cluster'][i], j, int(math.sqrt(u)))

    if j != float('inf'):
        return index(i, j, u)

    # Try to find next non-empty cluster
    if is_base_case(V['summary']):
        i = linear_successor(V['summary'], i)
    else:
        i = successor(V['summary'], i, int(math.sqrt(u)))

    if i == float('inf'):
        return float('inf')

    if is_base_case(V['cluster'][i]):
        j = linear_successor(V['cluster'][i], -1)
    else:
        j = successor(V['cluster'][i], -1, int(math.sqrt(u)))

    return index(i, j, u)

u = 16  # universe size

# Construct clusters (size √u = 4)
V = {
    'cluster': [
        [0,1,0,0],   # V.Cluster[0] (contains 1)
        [0,0,0,0],   # V.Cluster[1] (empty)
        [0,1,1,0],   # V.Cluster[2] (contains 9, 10 → positions 1 and 2)
        [0,0,0,1]    # V.Cluster[3] (contains 15 → position 3)
    ],
    'summary': [1, 0, 1, 1]  # Cluster[i] is non-empty
}

# Find the successor of 1
result = successor(V, 1, u)
print("Successor of 1 is:", result)

