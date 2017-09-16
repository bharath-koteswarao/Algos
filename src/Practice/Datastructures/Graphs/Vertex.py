class Vertex:
    def __init__(self, key):
        self.connections = {}
        self.key = key

    def addNeighbor(self, key, weight):
        self.connections[key] = weight

    def getConnections(self):
        return self.connections.keys()
