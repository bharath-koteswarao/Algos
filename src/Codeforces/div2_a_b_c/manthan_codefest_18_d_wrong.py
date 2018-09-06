from collections import Counter


class Vertex:
    def __init__(self, key):
        self.connections = {}
        self.key = key
        self.visited = False

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


def vldt(adj, start, ed, path):
    c1 = Counter(adj)
    c2 = {}
    for i in range(start, ed):
        if path[i] in c2:
            c2[path[i]] += 1
        else:
            c2[path[i]] = 1
    if len(c1) == len(c2):
        for x in c1:
            if x not in c2:
                return False
            else:
                if c1[x] != c2[x]:
                    return False
        return True
    else:
        return False


if __name__ == '__main__':
    n = int(input().strip())
    if n == 1:
        print("Yes")
    else:
        g = Graph()
        for _ in range(n - 1):
            a, b = [int(__) for __ in input().strip().split()]
            g.addEdge(a, b, 0)
        path = [int(__) for __ in input().strip().split()]
        p1, p2 = 0, 0
        for i in range(n):
            if p2 >= n:
                break
            cur = g.getVertex(path[i])
            adj = [i.key for i in g.getAdjacencyList(cur)]
            sub = path[p2 + 1: p2 + 1 + len(adj)]
            if vldt(adj, p2 + 1, p2 + 1 + len(adj), path):
                p2 += len(adj)
            else:
                print("No")
                exit(0)
        print("Yes")
