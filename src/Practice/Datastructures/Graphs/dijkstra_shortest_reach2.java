package Datastructures.Graphs;

import java.util.*;

import static java.lang.Math.min;

/**
 * Created by bk on 16-06-2018.
 */

class Graph {
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
    }

    public void addEdge(Vertex source, Vertex destination, long weight) {
        if (!verticesList.containsKey(source.key)) addVertex(source.key);
        if (!verticesList.containsKey(destination.key)) addVertex(destination.key);
        verticesList.get(source.key).addNeighbor(destination.key, weight);
    }

    public void addEdge(long source, long destination, long weight) {
        if (!verticesList.containsKey(source + "")) addVertex(source);
        if (!verticesList.containsKey(destination + "")) addVertex(destination);
        verticesList.get(source + "").addNeighbor(destination, weight);
    }

}

class Vertex implements Comparable<Vertex> {
    public String key;
    public Hashtable<String, Long> neighbors;
    int sd = (int) Math.pow(10, 9);
    boolean fixed = false;
    boolean visited = false;

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

    @Override
    public int compareTo(Vertex o) {
        return this.sd - o.sd;
    }

    @Override
    public String toString() {
        return this.sd + "";
    }
}

public class dijkstra_shortest_reach2 {

    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            Graph g = new Graph();
            int n = sc.nextInt(), m = sc.nextInt();
            for (int i = 0; i < m; i++) {
                long source = sc.nextLong(), dest = sc.nextLong(), weight = sc.nextLong();
                Vertex so = g.getVertex(source);
                Vertex de = g.getVertex(dest);
                long mi = weight;
                if (so.hasNeighbor(de)) mi = min(mi, so.edgeLength(de));
                if (de.hasNeighbor(so)) mi = min(mi, de.edgeLength(so));
                g.addEdge(source, dest, mi);
                g.addEdge(dest, source, mi);
            }
            Vertex source = g.getVertex(sc.nextLong());
            source.sd = 0;
            PriorityQueue<Vertex> heap = new PriorityQueue<>(g.verticesList.values());
            while (heap.size() > 0) {
                Vertex shortest = heap.peek();
                shortest.fixed = true;
                List<Vertex> adj = g.getAdjacencyList(shortest.key);
                for (Vertex vert : adj) {
                    vert.visited = true;
                    if (!vert.fixed) vert.sd = (int) min(vert.sd, shortest.sd + shortest.edgeLength(vert));
                }
                heap.remove();
            }
            for (int i = 1; i <= n; i++) {
                Vertex v = g.getVertex(i);
                if (!v.key.equals(source.key)) System.out.print(v.sd == Math.pow(10, 9) ? -1 + " " : v.sd + " ");
            }
            System.out.println();
        }
    }

    private static Vertex getMin(List<Vertex> vertices) {
        Vertex mi = vertices.get(0);
        for (Vertex ver : vertices) {
            if (mi.sd > ver.sd) mi = ver;
        }
        vertices.remove(mi);
        return mi;
    }
}
