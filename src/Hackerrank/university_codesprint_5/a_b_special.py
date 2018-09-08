import sys


class Vertex:
    def __init__(self, key):
        self.connections = {}
        self.key = key
        self.visited = False
        self.group = 0

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


def dfs(g, vertex, group):
    vertex.visited = True
    adjL = g.getAdjacencyList(vertex)
    vertex.group = group
    for verte in adjL:
        if not verte.visited:
            dfs(g, verte, group)


if __name__ == '__main__':
    sys.setrecursionlimit(2147483647)
    n, m, a, b = [int(__) for __ in input().strip().split()]
    g = Graph()
    for x in range(1, n + 1):
        g.addVertex(x)
    for _ in range(m):
        so, dest = [int(__) for __ in input().strip().split()]
        g.addEdge(so, dest, 0)
        g.addEdge(dest, so, 0)
    adj = {}
    for x in g:
        adj[x.key] = len(g.getAdjacencyList(x))
    gp = 0
    for ver in g:
        if not ver.visited:
            gp += 1
            dfs(g, ver, gp)
    conns = {}
    for x in g:
        if x.group in conns:
            conns[x.group].append(x.key)
        else:
            conns[x.group] = [x.key]
    ans = 0
    for vertex in g:
        gpp = vertex.group
        if len(conns[gpp]) > 1:
            v = adj[vertex.key]
            le, rt = False, False
            for y in conns[gpp]:
                if y != vertex.key:
                    if a * adj[y] < v:
                        le = True
                    if b * adj[y] > v:
                        rt = True
            if le and rt:
                ans += 1
    print(ans)
