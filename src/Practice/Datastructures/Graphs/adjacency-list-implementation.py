from Vertex import Vertex
from Graph import Graph

def main():
    graph = Graph()
    print(graph.verticesList)
    graph.addEdge("a", "b", 1)
    graph.addEdge("a", "c", 2)
    print(graph.verticesList)
    print(graph.verticesList["a"].connections)


main()