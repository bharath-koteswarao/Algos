from Graph import Graph


def buildGraph(g):
    g.addEdge("a", "b", 1)
    g.addEdge("a", "d", 1)
    g.addEdge("e", "d", 1)
    g.addEdge("d", "b", 1)
    g.addEdge("b", "e", 1)
    g.addEdge("c", "e", 1)
    g.addEdge("c", "f", 1)
    g.addEdge("f", "f", 1)


def showGraph(g):
    for vertex in g:
        print(vertex.key, g.getAdjacencyList(vertex))


def dfs_visit(g, vertex, parent_dict):
    if vertex not in parent_dict:
        parent_dict[vertex] = None
    adj = g.getAdjacencyList(vertex)
    for vert in adj:
        if vert not in parent_dict:
            parent_dict[vert] = vertex
            dfs_visit(g, vert, parent_dict)
    pass


def dfs(g, source, parent_dict):
    for vertex in g:
        dfs_visit(g, vertex, parent_dict)


if __name__ == '__main__':
    g = Graph()
    buildGraph(g)
    parent_dict = {g.getVertex('a'): None}
    dfs(g, "a", parent_dict)
    answers = {}
    for i in parent_dict:
        answers[i.key] = parent_dict[i].key if parent_dict[i] is not None else None
    print(answers)
