from pprint import pprint as pp

from Graph import Graph


def buildGraph(graph):
    graph.addEdge("p", "q", 1)
    graph.addEdge("p", "t", 7)
    graph.addEdge("p", "s", 6)
    graph.addEdge("q", "r", 1)
    graph.addEdge("q", "s", 4)
    graph.addEdge("s", "t", 3)
    graph.addEdge("s", "u", 2)
    graph.addEdge("t", "u", 2)
    graph.addEdge("r", "u", 1)
    graph.addEdge("r", "s", 2)


def extract_shortest_node(vertices):
    shortest = vertices[0]
    for vert in vertices:
        if vert.distance < shortest.distance:
            shortest = vert
    vertices.remove(shortest)
    return shortest


def relax(shortest_node, neighbor, parent):
    # Here the shortest_node in parameters is the node whose shortest path
    # is already decided
    # The shortest path of neighbor is being decided in this
    # If path of neighbor is greater than distance of shortest_node + edge between them
    # Then obviously the shortest path is edge b/w them + distance of shortest_node
    edge_length = shortest_node.edgeLength(neighbor)
    if neighbor.distance > shortest_node.distance + edge_length:
        neighbor.distance = shortest_node.distance + edge_length
        parent[neighbor.key] = shortest_node.key


def dijkstra(graph, parent, vertices, source):
    while len(vertices) > 0:
        shortest_node = extract_shortest_node(vertices)
        shortest_node.fixed_shortest_path = True
        print(shortest_node.key, " in order")
        adjacent_nodes = graph.getAdjacencyList(shortest_node)
        for neighbor in adjacent_nodes:
            if not neighbor.fixed_shortest_path:
                parent[neighbor.key] = shortest_node.key
                relax(shortest_node, neighbor, parent)


def initialize_all_vertices(vertices, source):
    for vertex in vertices:
        vertex.fixed_shortest_path = False
        # This fixed shortest path has to be checked since there is a chance
        # that a vertex may be checked again for shortest path
        # Though it doesn't effect the shortest path but it effects the parent
        if vertex is source:
            vertex.distance = 0
        else:
            vertex.distance = float("inf")


def show_shortest_path_of_all_vertices(graph, parent):
    for vertex in graph:
        path = []
        path.append(vertex.key)
        temp = vertex
        while parent[temp.key] is not None:
            path.append(parent[temp.key])
            temp = graph.getVertex(parent[temp.key])
        print("Shortest path to", vertex.key, "is", path[::-1])


if __name__ == "__main__":
    graph = Graph()
    buildGraph(graph)
    parent = {}
    vertices = list(graph.getAllVertices().values())
    source = graph.getVertex("p")
    parent[source.key] = None
    initialize_all_vertices(vertices, source)
    dijkstra(graph, parent, vertices, source)
    pp(parent, width=1)
    show_shortest_path_of_all_vertices(graph, parent)
