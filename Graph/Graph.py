
graph = {}


def add_node(v):
    if v in graph:
        print("Node is already present")
    else:
        graph[v] = []


def add_edge(v1, v2):
    if v1 not in graph:
        print("Node not present")
    elif v2 not in graph:
        print("Node not present")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


def del_node(v):
    if v not in graph:
        print("Node not present")
    else:
        graph.pop(v)
        for i in graph:
            l = graph[i]
            for v in l:
                l.remove(v)


def del_edge(v1, v2):
    if v1 not in graph:
        print("Node not present")
    elif v2 not in graph:
        print("Node not present")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)


def BFS(node, graph):
    visited = set()
    if node not in graph:
        print("Node not present")
        return
    queue = []
    queue.append(node)
    while queue:
        current = queue.pop(0)
        if current not in visited:
            print(current, end=" ")
            visited.add(current)
            for i in graph[current]:
                queue.append(i)



def DFS(node,graph):
    visited = set()
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current,end=" ")
            visited.add(current)
            for i in graph[current]:
                stack.append(i)





add_node(1)
add_node(2)
add_node(3)
add_node(4)
add_node(5)

add_edge(1,2)
add_edge(1,3)
add_edge(1,4)

add_edge(2,3)
add_edge(3,5)

BFS(1,graph)

print('\n')

DFS(2,graph)


