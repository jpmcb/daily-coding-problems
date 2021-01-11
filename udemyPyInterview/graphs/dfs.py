graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    visited, stack = set(), [start]

    while stack:
        cur = stack.pop()
        if cur not in visited:
            visited.add(cur)
            print(visited)
            for x in graph[cur]:
                stack.append(x)

    return visited

print(dfs(graph, 'A'))
