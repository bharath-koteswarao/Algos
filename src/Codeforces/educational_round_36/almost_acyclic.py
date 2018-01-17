

"""
3 4
1 2
2 3
3 2
3 1

4 4
1 2
2 1
1 3
3 1
"""
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


def dfs(g, vertex, check, path):
    if not vertex.visited:
        check[vertex] = {"cycle": False, "path": []}
        vertex.visited = True
        adj = g.getAdjacencyList(vertex)
        for nei in adj:
            dfs(g, nei, check, path + [vertex])
    else:
        found = vertex in path
        check[vertex]['cycle'] = True if found else False
        if found:
            check[vertex]['path'] = path


if __name__ == '__main__':
    n, v = [int(i) for i in input().strip().split()]
    g = Graph()
    check = {}
    for _ in range(v):
        s, d = [int(i) for i in input().strip().split()]
        g.addEdge(s, d, 1)
    for i in g:
        i.visited = False
    for vertex in g:
        if not vertex.visited:
            dfs(g, vertex, check, [])
    # pp(check)
    if v <= 3:
        print("Yes")
    else:
        valid = True
        tc, fc = 0, 0
        cycles = []
        for i in check:
            if check[i]['cycle']:
                tc += 1
                ind = check[i]['path'].index(i)
                # print(ind)
                cycles.append(check[i]['path'][ind:])
            else:
                fc += 1
        if tc > 2:
            print("No")
        elif fc == len(check):
            # print(cycles)
            print("Yes")
        else:
            print(cycles)
            if len(cycles) < 2:
                print("Yes")
            else:
                p, q = cycles
                p = [str(i.key) for i in p]
                q = [str(i.key) for i in q]
                p = ''.join(p)
                q = ''.join(q)
                if p.endswith(q) or q.endswith(p):
                    print("Yes")
                else:
                    print("No")
