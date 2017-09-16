from Graph import Graph


def buildGraph(dictionary, graph):
    for collection in dictionary.keys():
        words = dictionary[collection]
        for word1 in words:
            for word2 in words:
                if word1 != word2:
                    graph.addEdge(word1, word2, 0)

    for vertex in graph.verticesList:
        print(vertex, graph.verticesList[vertex].connections)


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
