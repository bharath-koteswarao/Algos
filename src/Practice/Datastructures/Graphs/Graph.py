from Vertex import Vertex


class Graph:
    def __init__(self):
        self.verticesList = {}

    def addVertex(self, key):
        self.verticesList[key] = Vertex(key)

    def addEdge(self, source, destination, weight):
        if source not in self.verticesList:
            self.verticesList[source] = Vertex(source)
        if destination not in self.verticesList:
            self.verticesList[destination] = Vertex(destination)
        self.verticesList[source].addNeighbor(destination, weight)

