class Vertex:
    def __init__(self, key):
        self.connections = {}
        self.key = key

    def addNeighbor(self, key, weight):
        self.connections[key] = weight

    def getConnections(self):
        return self.connections.keys()


class Graph:
    def __init__(self):
        self.verticesList = {}

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


def bfs(source, graph):  # This is bfs
    i = 1  # Indicates level
    for vertex in graph:
        vertex.visited = False
    levels = {}  # This stores the nodes visited in each level current level is i-1 = 0
    current_level = [graph.getVertex(source)]  # Stores vertices of current level
    while len(current_level) is not 0:
        next_level = []  # Add all nodes adjacent to nodes of current level
        for popped in current_level:
            popped.visited = True  # Since we have visited this already
            # print(popped.key, " is visited")
            for neighbor in graph.getAdjacencyList(popped):
                if neighbor not in next_level and not neighbor.visited:
                    neighbor.visited = True  # This is to prevent this node to be visited again
                    # print(neighbor.key)
                    next_level.append(neighbor)
        levels[i] = [vert.key for vert in next_level]
        current_level = next_level
        i += 1
    # print(levels)
    return levels


def main():
    tc = int(input())
    for k in range(tc):
        graph = Graph()
        (nodes, edges) = map(int, input().split(" "))
        for i in range(edges):
            (node1, node2) = map(int, input().split(" "))
            graph.addEdge(node1, node2, 6)
        source = int(input().split(" ")[0])
        dist = bfs(source, graph)
        answer = {}
        for i in dist:
            lis = dist[i]
            for j in lis:
                answer[j] = i * 6
        for i in range(1, nodes + 1):
            if i is source:
                pass
            elif i in answer:
                print(answer[i], end=" ")
            else:
                print(-1, end=" ")
        print()

main()
