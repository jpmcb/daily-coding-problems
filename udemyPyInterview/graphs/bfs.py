graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def bfs(graph, start):
    visited, queue = set(), [start]

    while queue:
        v = queue.pop(0)
        if v not in visited:
            visited.add(v)
            for x in graph[v]:
                queue.append(x)

    return visited

print(bfs(graph, 'A'))