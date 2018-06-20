package Hackerrank.week_of_code_38;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Hashtable;
import java.util.List;
import java.util.StringTokenizer;

/**
 * Created by bk on 20-06-2018.
 */
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

class Vertex {
    public String key;
    public Hashtable<String, Long> neighbors;
    boolean fixed = false;
    long sd = (long) Math.pow(10, 10);
    long signalTime = 0;

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

class FastIO {
    private BufferedReader br;
    private StringTokenizer st;

    FastIO() {
        br = new BufferedReader(new
                InputStreamReader(System.in));
    }

    public String next() {
        while (st == null || !st.hasMoreElements()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return st.nextToken();
    }

    public int nextInt() {
        return Integer.parseInt(next());
    }

    public long nextLong() {
        return Long.parseLong(next());
    }

    public double nextDouble() {
        return Double.parseDouble(next());
    }

    public String nextLine() {
        String str = "";
        try {
            str = br.readLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return str;
    }
}

public class C {
    public static void main(String[] __) {
        FastIO sc = new FastIO();
        long n = sc.nextLong();
        long k = sc.nextLong();
        int m = sc.nextInt();
        Graph g = new Graph();
        for (int i = 0; i < n; i++) g.addVertex(i + 1);
        for (int i = 0; i < m; i++) {
            Vertex source = g.getVertex(sc.nextLong());
            Vertex dest = g.getVertex(sc.nextLong());
            long wt = sc.nextLong();
            if (source.hasNeighbor(dest)) wt = Math.min(wt, source.edgeLength(dest));
            if (dest.hasNeighbor(source)) wt = Math.min(wt, dest.edgeLength(source));
            g.addEdge(source, dest, wt);
            g.addEdge(dest, source, wt);
        }
        g.getVertex(1).sd = 0;
        ArrayList<Vertex> vertices = new ArrayList<>(g.verticesList.values());
        while (vertices.size() > 0) {
            Vertex shor = getMin(vertices);
            shor.fixed = true;
            for (Vertex vertex : g.getAdjacencyList(shor.key)) {
                if (!vertex.fixed) {
                    long sd = shor.sd;
                    long cur = vertex.sd;
                    long edg = shor.edgeLength(vertex);
                    long total = sd + edg;
                    if (vertex.key.equals(n + "")) {
                        vertex.sd = Math.min(total, vertex.sd);
                    } else if (Math.floorDiv(total, k) % 2 == 1) {
                        total += k - total % k;
                    }
                    if (total < cur) vertex.sd = total;
                }
            }
        }
        System.out.println(g.getVertex(n).sd);
    }

    private static Vertex getMin(ArrayList<Vertex> vertices) {
        Vertex shortest = vertices.get(0);
        for (Vertex vertex : vertices) if (vertex.sd < shortest.sd) shortest = vertex;
        vertices.remove(shortest);
        return shortest;
    }
}
