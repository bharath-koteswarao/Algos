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


def main():
    graph = Graph()
    print(graph.verticesList)
    graph.addEdge("a", "b", 1)
    graph.addEdge("a", "c", 2)
    print(graph.verticesList)
    print(graph.verticesList["a"].connections)


main()
