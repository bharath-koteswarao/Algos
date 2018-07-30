package Datastructures.disjoint_sets;

/**
 * Created by bk on 30-07-2018.
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

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

class Set {
    Set parent;
    String key;
    int rank;

    public Set(String key) {
        this.key = key;
        this.parent = this;
        this.rank = 1;
    }

    @Override
    public String toString() {
        return "(" + this.key + ", " + this.rank + ")";
    }
}

public class merging_communities {
    public static void main(String[] __) {
        FastIO sc = new FastIO();
        int n = sc.nextInt(), q = sc.nextInt();
        HashMap<String, Set> container = new HashMap<>();
        for (int i = 1; i <= n; i++) container.put(i + "", new Set(i + ""));
        for (int i = 0; i < q; i++) {
            char type = sc.next().charAt(0);
            if (type == 'M') {
                String first = sc.next(), second = sc.next();
                merge(container.get(first), container.get(second));
            } else {
                System.out.println(findParent(container.get(sc.next())).rank);
            }
        }
    }

    private static void merge(Set s1, Set s2) {
        Set p1 = findParent(s1);
        Set p2 = findParent(s2);
        if (!p1.key.equals(p2.key)) {
            if (p1.rank >= p2.rank) {
                p2.parent = p1;
                p1.rank += p2.rank;
                p2.rank = 1;
            } else {
                p1.parent = p2;
                p2.rank += p1.rank;
                p1.rank = 1;
            }
        }
    }

    private static Set findParent(Set s) {
        if (s.parent.key.equals(s.key)) return s;
        else return findParent(s.parent);
    }
}
