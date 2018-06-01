package Datastructures.Graphs;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.Math.min;

/**
 * Created by bk on 28-05-2018.
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

    public List<String> getAdjacencyList(String key) {
        return verticesList.get(key).getNeighbors();
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

class Vertex implements Comparable {
    public String key;
    public Hashtable<String, Long> neighbors;
    boolean fixed = false;
    long sd = Integer.MAX_VALUE;

    public Vertex(String key) {
        this.key = key;
        neighbors = new Hashtable<>();
    }

    public Vertex(long key) {
        this.key = key + "";
        neighbors = new Hashtable<>();
    }

    @Override
    public String toString() {
        return sd + "";
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
    public int compareTo(Object o) {
        return (int) (sd - ((Vertex) o).sd);
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

public class dijkstra_shortest_reach_2 {
    public static void main(String[] __) {
        FastIO sc = new FastIO();
        int tc = sc.nextInt();
        for (int tc_i = 0; tc_i < tc; tc_i++) {
            Graph graph = new Graph();
            long n = sc.nextLong(), m = sc.nextLong();
            for (int i = 1; i <= n; i++) graph.addVertex(i);
            for (int i = 0; i < m; i++) {
                Vertex source = graph.getVertex(sc.nextLong()), destination = graph.getVertex(sc.nextLong());
                long wt = sc.nextLong();
                if (source.hasNeighbor(destination)) wt = min(wt, source.edgeLength(destination.key));
                graph.addEdge(source, destination, wt);
                graph.addEdge(destination, source, wt);
//                System.out.println(source.getNeighbors());
            }
            String source = sc.nextLong() + "";
            graph.verticesList.get(source).sd = 0;
            PriorityQueue<Vertex> heap = new PriorityQueue<>(graph.verticesList.values());
            while (heap.size() > 0) {
                Vertex nearest = heap.poll();
//                System.out.println(nearest.key+" "+nearest.getNeighbors());
//                System.out.println(nearest.key);
                graph.verticesList.get(nearest.key).fixed = true;
                for (String nei : nearest.getNeighbors()) {
                    Vertex neighbor = graph.getVertex(nei);
//                    System.out.println(nei + " "+neighbor.sd);
                    neighbor.sd = min(neighbor.sd, nearest.sd + nearest.edgeLength(neighbor));
//                    System.out.println(nei+" "+neighbor.sd);
                }
            }
            show(graph, n, source);
        }
    }

    private static void show(Graph graph, long n, String source) {
        for (int i = 1; i <= n; i++) {
            if (!((i + "").equals(source))) {
                long sd = graph.getVertex(i + "").sd;
                System.out.print(sd >= Integer.MAX_VALUE ? -1 + " " : sd + " ");
            }
        }
        System.out.println();
    }
}
