"""
10 10 1 2
1 2
3 4
5 6
7 8
9 10
1 3
6 5
4 3
2 1
8 7
"""


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


class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.rank = 1
        self.isParent = True

    def __repr__(self):
        return str(self.val)


def find(x):
    if x.parent == x:
        return x
    else:
        return find(x.parent)


def merge(x, y):
    p1, p2 = find(x), find(y)
    if p1.val != p2.val:
        if p1.rank >= p2.rank:
            p2.parent = p1
            p1.rank += p2.rank
            p2.isParent = False
        else:
            p1.parent = p2
            p2.rank += p1.rank
            p1.isParent = False


if __name__ == '__main__':
    n, m, a, b = [int(__) for __ in input().strip().split()]
    g = Graph()
    dic = {i: Node(i) for i in range(1, n + 1)}
    for x in range(1, n + 1):
        g.addVertex(x)
    for _ in range(m):
        so, dest = [int(__) for __ in input().strip().split()]
        g.addEdge(so, dest, 0)
        g.addEdge(dest, so, 0)
        merge(dic[so], dic[dest])
    adj = {}
    for x in g:
        adj[x.key] = len(g.getAdjacencyList(x))
    conns = {}
    parent = {}
    for x in dic:
        p = find(dic[x]).val
        parent[x] = p
        if p in conns:
            conns[p].append(x)
        else:
            conns[p] = [x]
    adjs = {}
    for x in conns:
        l = [0 for i in range(2 * len(conns[x]))]
        co = 0
        for el in conns[x]:
            l[co] = a * adj[el]
            l[co + 1] = b * adj[el]
            co += 2
        l.sort()
        adjs[x] = l
    ans = 0
    for x in dic:
        check = adjs[parent[x]]
        check.remove(adj[x] * a)
        check.remove(adj[x] * b)
        if len(check) > 0 and adj[x] != check[0] and adj[x] != check[-1]:
            ans += 1
    print(ans)
