package Hackerrank.university_codesprint_5;

/**
 * Created by bk on 08-09-2018.
 */


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

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

    public void addVertex(long key, String name) {
        Vertex vertex = new Vertex(key);
        vertex.name = name;
        verticesList.put(key + "", vertex);
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

    public void addEdge(String source, String destination, String weight) {
        if (!verticesList.containsKey(source)) addVertex(source);
        if (!verticesList.containsKey(destination)) addVertex(destination);
        verticesList.get(source).addNeighbor(destination, weight);
    }

    public void addEdge(Vertex source, Vertex destination, String weight) {
        if (!verticesList.containsKey(source.key)) addVertex(source.key);
        if (!verticesList.containsKey(destination.key)) addVertex(destination.key);
        verticesList.get(source.key).addNeighbor(destination.key, weight);
    }

    public void addEdge(long source, long destination, String weight) {
        if (!verticesList.containsKey(source + "")) addVertex(source);
        if (!verticesList.containsKey(destination + "")) addVertex(destination);
        verticesList.get(source + "").addNeighbor(destination, weight);
    }

}

class Vertex implements Comparable<Vertex> {
    public String key;
    public Hashtable<String, String> neighbors;
    String name;
    String distance = "zzzzzzzzzzzzzzzzzzzz";
    boolean fixed = false;

    public Vertex(String key) {
        this.key = key;
        neighbors = new Hashtable<>();
    }

    public Vertex(long key) {
        this.key = key + "";
        neighbors = new Hashtable<>();
    }

    public void addNeighbor(String key, String weight) {
        neighbors.put(key, weight);
    }

    public void addNeighbor(long key, String weight) {
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

    public String edgeLength(String destination) {
        return neighbors.get(destination);
    }

    public String edgeLength(Vertex destination) {
        return neighbors.get(destination.key);
    }

    public String edgeLength(long destination) {
        return neighbors.get(destination + "");
    }

    public List<String> getNeighbors() {
        return new ArrayList<>(neighbors.keySet());
    }

    @Override
    public int compareTo(Vertex o) {
        return this.distance.compareTo(o.distance);
    }

    @Override
    public String toString() {
        return "(" + this.key + ", " + this.distance + ")";
    }
}

public class interesting_trip {
    public static void main(String[] __) {
        String maxDistance = "zzzzzzzzzzzzzzzzzzzz";
        FastIO sc = new FastIO();
        int n = sc.nextInt(), m = sc.nextInt();
        String names = sc.next();
        Graph g = new Graph();
        for (int i = 1; i <= n; i++) {
            g.addVertex(i, names.charAt(i - 1) + "");
        }
        for (int i = 0; i < m - 1; i++) {
            long so = sc.nextLong(), de = sc.nextLong();
            g.addEdge(so, de, g.getVertex(de).name);
        }
        Vertex source = g.getVertex(sc.nextInt()), destination = g.getVertex(sc.nextInt());
        source.distance = source.name;
        PriorityQueue<Vertex> heap = new PriorityQueue<>();


//        heap.add(source);
//        while (heap.size() > 0) {
//            Vertex cur = heap.remove();
//            if (!cur.fixed) {
//                List<Vertex> adj = g.getAdjacencyList(cur.nodeNumber);
//                for (Vertex nei : adj) {
//                    if (!nei.fixed) {
//                        String newD = cur.distance + cur.edgeLength(nei);
//                        if (nei.distance.compareTo(newD) > 0) {
//                            nei.distance = newD;
//                            heap.add(nei);
//                        }
//                    }
//                }
//            }
//        }


        String dist = g.getVertex(destination.key).distance;
        if (dist.equals(maxDistance)) System.out.println("No way");
        else System.out.println(dist);
    }

}
