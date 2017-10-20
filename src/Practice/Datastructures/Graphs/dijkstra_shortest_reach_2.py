from Graph import Graph


class G(Graph):
    def __init__(self):
        super().__init__()
        self.vertices_list = list(self.getAllVertices().values())

    def relax(self, source, destination):
        edge_length = source.edgeLength(destination)
        if destination.distance > source.distance + edge_length:
            destination.distance = source.distance + edge_length

    def extract_nearest_node(self):
        shortest = self.vertices_list[0]
        for i in range(1, len(self.vertices_list)):
            if self.vertices_list[i].distance < shortest.distance:
                shortest = self.vertices_list[i]
        self.vertices_list.remove(shortest)
        return shortest

    def get_input(self):
        nodes, edges = [int(i) for i in input().strip().split(" ")]
        for i in range(1, nodes + 1):
            self.addVertex(i)
            self.getVertex(i).fixed_shortest_path = False
            self.getVertex(i).distance = float('inf')
        for i in range(edges):
            first, last, weight = [int(i) for i in input().strip().split(" ")]
            first = self.getVertex(first)
            last = self.getVertex(last)
            if first.isNeighbor(last):
                self.addEdge(first.key, last.key,
                             min(weight, first.edgeLength(last)))
            else:
                self.addEdge(first.key, last.key, weight)
            if last.isNeighbor(first):
                self.addEdge(last.key, first.key,
                             min(weight, last.edgeLength(first)))
            else:
                self.addEdge(last.key, first.key, weight)

    def dijk(self):
        self.vertices_list = list(self.getAllVertices().values())
        while len(self.vertices_list) > 0:
            shortest = self.extract_nearest_node()
            shortest.fixed_shortest_path = True
            adj_nodes = self.getAdjacencyList(shortest)
            for vert in adj_nodes:
                if not vert.fixed_shortest_path:
                    self.relax(shortest, vert)


if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        g = G()
        g.get_input()
        start = g.getVertex(int(input().strip()))
        start.distance = 0
        g.dijk()
        for i in range(1, len(g.getAllVertices()) + 1):
            if i != start.key:
                dist = g.getVertex(i).distance
                print(dist if dist != float('inf') else -1, end=" ")
            print()
