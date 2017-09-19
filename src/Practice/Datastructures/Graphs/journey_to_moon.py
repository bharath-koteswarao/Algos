from Graph import Graph


def buildGraph(graph):
    (n, p) = [int(i) for i in input().split(" ")]
    for i in range(n):
        graph.addVertex(i)
    for i in range(p):
        (end1, end2) = [int(j) for j in input().split(" ")]
        graph.addEdge(end1, end2, 1)
        graph.addEdge(end2, end1, 1)


def initialize(graph):
    for vertex in graph:
        vertex.visited = False


def c(n, r):
    if n < r:
        return 0
    elif n == r:
        return 1
    else:
        numerator = 1
        denominator = 1
        for j in range(n, n - r, -1):
            numerator *= j
        # print("numerator is ",numerator)
        for j in range(r, 0, -1):
            denominator *= j
        # print("denominator is ",denominator)
        return numerator / denominator


def dfs_visit(graph, vertex, parent):
    vertex.visited = True
    adj = graph.getAdjacencyList(vertex)
    for vert in adj:
        if vert.key not in parent:
            parent[vert.key] = parent[vertex.key] if parent[vertex.key] is not None else vertex.key
        if not vert.visited:
            dfs_visit(graph, vert, parent)


if __name__ == '__main__':
    graph = Graph()
    buildGraph(graph)
    initialize(graph)
    parent = {}
    for vertex in graph:
        if vertex.key not in parent:
            parent[vertex.key] = None
        dfs_visit(graph, vertex, parent)
    parsed = {}
    for i in parent:
        if parent[i] is None:
            parsed[i] = 1
        if parent[i] in parsed:
            parsed[parent[i]] += 1
    answer = c(graph.verticesCount(), 2)
    for i in parsed:
        answer -= c(parsed[i], 2)
    print(int(answer))
