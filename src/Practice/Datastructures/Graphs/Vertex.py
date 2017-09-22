class Vertex:
    def __init__(self, key):
        self.connections = {}
        self.key = key

    def addNeighbor(self, key, weight):
        self.connections[key] = weight

    def edgeLength(self, destination):
        return self.connections[destination.key]

    def getConnections(self):
        return self.connections.keys()
