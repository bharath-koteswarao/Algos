from Graph import Graph


def findPath(source, destination, graph):   # This is bfs
    i = 1  # Indicates level
    for vertex in graph:
        vertex.visited = False
    levels = {}  # This stores the nodes visited in each level current level is i-1 = 0
    current_level = [graph.getVertex(source)]  # Stores vertices of current level
    while len(current_level) is not 0:
        next_level = []  # Add all nodes adjacent to nodes of current level
        for popped in current_level:
            popped.visited = True  # Since we have visited this already
            print(popped.key, " is visited")
            for neighbor in graph.getAdjacencyList(popped):
                if neighbor not in next_level and not neighbor.visited:
                    neighbor.visited = True  # This is to prevent this node to be visited again
                    print(neighbor.key)
                    next_level.append(neighbor)
        levels[i] = [vert.key for vert in next_level]
        current_level = next_level
        i += 1
    print(levels)
    for i in levels:
        if destination in levels[i]:
            print(destination, " arrived at ", i)
            break


def buildGraph(dictionary, graph):
    for collection in dictionary.keys():
        words = dictionary[collection]
        for word1 in words:
            for word2 in words:
                if word1 != word2:
                    graph.addEdge(word1, word2, 0)

    findPath("fool", "sage", graph)


def main():
    dictionary = {}
    wordList = ["foul", "foil", "fool", "fail", "fall", "pall",
                "poll", "pole", "pool", "cool", "pope", "pale",
                "sale", "page", "sage"]
    for word in wordList:
        for i in range(len(word)):
            bucket = (word[:i] + "_" + word[i + 1:])
            if bucket in dictionary:
                dictionary[bucket].append(word)
            else:
                dictionary[bucket] = [word]
    graph = Graph()
    buildGraph(dictionary, graph)


main()
