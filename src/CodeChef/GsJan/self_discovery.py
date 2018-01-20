from heapq import *


class Vertex:
    def __init__(self, key):
        self.connections = {}
        self.key = key

    def addNeighbor(self, key, weight):
        self.connections[key] = weight

    def removeNeighbor(self, key):
        if key in self.connections:
            del self.connections[key]

    def edgeLength(self, destination):
        return self.connections[destination.key]

    def isNeighbor(self, destination):
        if type(destination) == int:
            return destination in self.connections
        else:
            return destination.key in self.connections

    def getConnections(self):
        return self.connections.keys()

    def __repr__(self):
        return str(self.key)


class Graph:
    def __init__(self):
        self.verticesList = {}

    def containsVertex(self, key):
        return key in self.verticesList

    def getAllVertices(self):
        return self.verticesList

    def verticesCount(self):
        return len(self.verticesList)

    def addVertex(self, key):
        self.verticesList[key] = Vertex(key)

    def __iter__(self):
        return iter(self.verticesList.values())

    def getAdjacencyList(self, key):
        if type(key) is str:
            return [self.getVertex(val) for val in list(self.getVertex(key).connections.keys())]
            # These return statements simply return adjacency list with vertices in it
        elif type(key) is Vertex:
            return [self.getVertex(val) for val in list(key.connections.keys())]

    def getVertex(self, key):
        return self.verticesList[key]

    def addEdge(self, source, destination, weight):
        if source not in self.verticesList:
            self.verticesList[source] = Vertex(source)
        if destination not in self.verticesList:
            self.verticesList[destination] = Vertex(destination)
        self.verticesList[source].addNeighbor(destination, weight)

    def removeEdge(self, source, destination):
        if source in self.verticesList and destination in self.verticesList:
            self.verticesList[source].removeNeighbor(destination)

    def adj(self):
        return self.verticesList


def extract_shortest_node(vertices):
    # mi = heappop(vert_keys)
    # return g.getVertex(mi)
    shortest = vertices[0]
    for vert in vertices:
        if vert.distance < shortest.distance:
            shortest = vert
    vertices.remove(shortest)
    return shortest


def dijkstra(graph, parent, vertices, source):
    while len(vertices) > 0:
        shortest_node = extract_shortest_node(vertices)
        shortest_node.fixed_shortest_path = True
        adjacent_nodes = graph.getAdjacencyList(shortest_node)
        for neighbor in adjacent_nodes:
            if not neighbor.fixed_shortest_path:
                parent[neighbor.key] = shortest_node.key
                relax(shortest_node, neighbor, parent)


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


if __name__ == '__main__':
    for __ in range(int(input().strip())):
        n, m, s, e = [int(i) for i in input().strip().split()]
        g = Graph()
        for i in range(n):
            g.addVertex(i + 1)
        for _ in range(m):
            a, b = [int(i) for i in input().strip().split()]
            g.addEdge(a, b, 1)
        for vert in g:
            vert.fixed_shortest_path = False
            if vert.key == s:
                vert.distance = 0
            else:
                vert.distance = float('inf')
        parent = {}
        vertices = list(g.getAllVertices().values())
        vert_keys = [i.key for i in vertices]
        source = g.getVertex(s)
        parent = {s: None}
        heapify(vert_keys)
        dijkstra(g, parent, vertices, source)
        dist = g.getVertex(e).distance
        if dist == float('inf'):
            print("NO")
        else:
            print("YES", str(dist - 1))
