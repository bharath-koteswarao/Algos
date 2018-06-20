package Datastructures.Graphs.hackerrank;

/**
 * Created by bk on 19-06-2018.
 *
 11
 a b 2
 a c 6
 a e 5
 a f 10
 b e 3
 b d 3
 c d 1
 c f 2
 d e 4
 d g 5
 f g 5
 */

import java.util.*;

class Edge implements Comparable<Edge> {
    String source, destination;
    long weight;

    Edge() {

    }

    Edge(String source, String destination, long weight) {
        this.source = source;
        this.destination = destination;
        this.weight = weight;
    }

    Edge(long source, long destination, long weight) {
        this.source = source + "";
        this.destination = destination + "";
        this.weight = weight;
    }

    @Override
    public int compareTo(Edge o) {
        return (int) (this.weight - o.weight);
    }
}

class Graph {
    public Hashtable<String, Vertex> verticesList;
    private ArrayList<Edge> edges;

    Graph() {
        verticesList = new Hashtable<>();
        edges = new ArrayList<>();
    }

    public ArrayList<Edge> getEdges() {
        return this.edges;
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

    public void addVertex(long key) {
        verticesList.put(key + "", new Vertex(key));
    }

    public List<Vertex> getAdjacencyList(String key) {
        List<Vertex> ret = new ArrayList<>();
        for (String ver : verticesList.get(key).getNeighbors()) {
            ret.add(verticesList.get(ver));
        }
        return ret;
    }

    public List<String> getAdjacencyList(Vertex vertex) {
        return verticesList.get(vertex.key).getNeighbors();
    }

    public Vertex getVertex(String key) {
        if (!verticesList.containsKey(key)) verticesList.put(key, new Vertex(key));
        return verticesList.get(key);
    }

    public Vertex getVertex(long key) {
        if (!verticesList.containsKey(key + "")) verticesList.put(key + "", new Vertex(key));
        return verticesList.get(key + "");
    }

    public void addEdge(String source, String destination, long weight) {
        if (!verticesList.containsKey(source)) addVertex(source);
        if (!verticesList.containsKey(destination)) addVertex(destination);
        verticesList.get(source).addNeighbor(destination, weight);
        edges.add(new Edge(source, destination, weight));
    }

    public void addEdge(Vertex source, Vertex destination, long weight) {
        if (!verticesList.containsKey(source.key)) addVertex(source.key);
        if (!verticesList.containsKey(destination.key)) addVertex(destination.key);
        verticesList.get(source.key).addNeighbor(destination.key, weight);
        edges.add(new Edge(source.key, destination.key, weight));
    }

    public void addEdge(long source, long destination, long weight) {
        if (!verticesList.containsKey(source + "")) addVertex(source);
        if (!verticesList.containsKey(destination + "")) addVertex(destination);
        verticesList.get(source + "").addNeighbor(destination, weight);
        edges.add(new Edge(source, destination, weight));
    }

}

class Vertex {
    public String key;
    public Hashtable<String, Long> neighbors;

    public Vertex(String key) {
        this.key = key;
        neighbors = new Hashtable<>();
    }

    public Vertex(long key) {
        this.key = key + "";
        neighbors = new Hashtable<>();
    }

    public void addNeighbor(String key, long weight) {
        neighbors.put(key, weight);
    }

    public void addNeighbor(long key, long weight) {
        neighbors.put(key + "", weight);
    }

    public boolean hasNeighbor(String key) {
        return neighbors.containsKey(key);
    }

    public boolean hasNeighbor(long key) {
        return neighbors.containsKey(key + "");
    }

    public boolean hasNeighbor(Vertex destination) {
        return neighbors.containsKey(destination.key);
    }

    public long edgeLength(String destination) {
        return neighbors.get(destination);
    }

    public long edgeLength(Vertex destination) {
        return neighbors.get(destination.key);
    }

    public long edgeLength(long destination) {
        return neighbors.get(destination + "");
    }

    public List<String> getNeighbors() {
        return new ArrayList<>(neighbors.keySet());
    }
}

public class kruskals_algorithm {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int edges = sc.nextInt();
        Graph g = new Graph();
        for (int i = 0; i < edges; i++) {
            String source = sc.next(), dest = sc.next();
            long wt = sc.nextLong();
            g.addEdge(source, dest, wt);
        }
        List<Edge> edgs = g.getEdges();
        Collections.sort(edgs);
        Hashtable<String, Long> container = new Hashtable<>();
        List<Vertex> vertices = g.getAllVertices();
        for (int i = 0; i < vertices.size(); i++) {
            container.put(vertices.get(i).key, (long) i);
        }
        long minSPTWt = 0;
        for (Edge edge: edgs) {
            String source = edge.source;
            String dest = edge.destination;
            long wt = edge.weight;
            if (!container.get(source).equals(container.get(dest))) {
                minSPTWt += wt;
                container.put(dest, container.get(source));
            }
        }
        System.out.println(minSPTWt);
    }
}
