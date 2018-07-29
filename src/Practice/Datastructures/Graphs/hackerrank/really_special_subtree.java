package Datastructures.Graphs.hackerrank;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

/**
 * Created by bk on 29-07-2018.
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

    @Override
    public String toString() {
        return "(" + this.source + ", " + this.destination + ")";
    }
}

class Set {
    Set parent;
    String key;
    int rank;

    public Set(String key) {
        this.key = key;
        parent = this;
        rank = 1;
    }

    @Override
    public String toString() {
        return this.key;
    }
}

public class really_special_subtree {
    static HashMap<String, Set> container;

    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), k = sc.nextInt();
        container = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            container.put((i + ""), new Set(i + ""));
        }
        Edge[] edges = new Edge[k];
        for (int i = 0; i < k; i++) {
            String source = sc.next();
            String dest = sc.next();
            int wt = sc.nextInt();
            edges[i] = new Edge(source, dest, wt);
        }
        Arrays.sort(edges);
        int ans = 0;
        for (Edge edge : edges) {
            if (n == 1) break;
            Set s1 = container.get(edge.source);
            Set s2 = container.get(edge.destination);
            if (merge(s1, s2)) {
                ans += edge.weight;
                n -= 1;
            }
        }
        System.out.println(ans);
    }

    private static Set getParent(Set s) {
        if (s.parent == s) return s;
        else return getParent(s.parent);
    }

    private static boolean merge(Set s1, Set s2) {
        Set parent1 = getParent(s1);
        Set parent2 = getParent(s2);
        if (!parent1.key.equals(parent2.key)) {
            if (parent1.rank <= parent2.rank) {
                parent1.parent = parent2;
            } else {
                parent2.parent = parent1;
            }
            return true;
        } else return false;
    }
}
