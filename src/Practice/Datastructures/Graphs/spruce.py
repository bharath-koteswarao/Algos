from Graph import Graph


def buildGraph(graph):
    n = int(input().strip())
    for i in range(2, n + 1):
        v = int(input().strip())
        graph.addEdge(v, i, 1)


if __name__ == '__main__':
    g = Graph()
    buildGraph(g)
    for i in g.verticesList:
        ve = g.getVertex(i)
        adj = g.getAdjacencyList(ve)
        ve.is_leaf = len(adj) == 0
    spruce = True
    for i in g.verticesList:
        if not g.getVertex(i).is_leaf:
            adj = g.getAdjacencyList(g.getVertex(i))
            c = 0
            for child in adj:
                if child.is_leaf:
                    c += 1
            if c < 3:
                spruce = False
            if not spruce:
                break
    print("Yes" if spruce else "No")
