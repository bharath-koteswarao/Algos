from Vertex import Vertex


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

    def adj(self):
        return self.verticesList
