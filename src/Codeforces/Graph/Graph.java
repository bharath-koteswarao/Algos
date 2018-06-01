package Codeforces.Graph;

import java.util.ArrayList;
import java.util.Hashtable;
import java.util.List;

/**
 * Created by bk on 28-05-2018.
 */

public class Graph {
    public Hashtable<String, Vertex> verticesList;

    Graph() {
        verticesList = new Hashtable<>();
    }

    public boolean containsVertex(String key) {
        return verticesList.containsKey(key);
    }

    public List<Vertex> getAllVertices() {
        return new ArrayList<>(verticesList.values());
    }

    public long verticesCount() {
        return verticesList.size();
    }

    public void addVertex(String key) {
        verticesList.put(key, new Vertex(key));
    }

    public List<String> getAdjacencyList(String key) {
        return verticesList.get(key).getNeighbors();
    }

    public Vertex getVertex(String key) {
        return verticesList.get(key);
    }

    public void addEdge(String source, String destination, long weight) {
        if (!verticesList.containsKey(source)) addVertex(source);
        if (!verticesList.containsKey(destination)) addVertex(destination);
        verticesList.get(source).addNeighbor(destination, weight);
    }
}
