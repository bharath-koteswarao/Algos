from Graph import Graph


def initialize_graph(g):
    for vertex in g:
        vertex.distance = float("inf")
        vertex.fixed_shortest_path = False


def extract_shortest_node(vertices):
    shortest = vertices[0]
    for vert in vertices:
        if vert.distance < shortest.distance:
            shortest = vert
    vertices.remove(shortest)
    return shortest


def relax(shortest, neighbor):
    edge = shortest.edgeLength(neighbor)
    if neighbor.distance > shortest.distance + edge:
        neighbor.distance = shortest.distance + edge


def dijk(g, vertices):
    while len(vertices) > 0:
        shortest = extract_shortest_node(vertices)
        shortest.fixed_shortest_path = True
        for neighbor in g.getAdjacencyList(shortest):
            if not neighbor.fixed_shortest_path:
                relax(shortest, neighbor)


if __name__ == '__main__':
    tc = int(input().split(" ")[0])
    for k in range(tc):
        g = Graph()
        (nodes, edges) = [int(i) for i in input().split(" ")]
        for i in range(1, edges + 1):
            (node1, node2) = [int(j) for j in input().split(" ")]
            g.addEdge(node1, node2, 6)
            g.addEdge(node2, node1, 6)
        source = int(input().split(" ")[0])
        initialize_graph(g)
        g.getVertex(source).distance = 0
        vertices = list(g.getAllVertices().values())
        dijk(g, vertices)
        for i in range(1, nodes + 1):
            if g.containsVertex(i):
                vert = g.getVertex(i)
                if vert is g.getVertex(source):
                    pass
                else:
                    print(vert.distance if vert.distance != float("inf") else -1, end=" ")
            else:
                print(-1, end=" ")
