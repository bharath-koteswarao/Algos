package Spoj;

/*
 * Created by bk on 21-12-2017 13:22
 *
5
5 1 2 3 4
3
2 4 1
4 4 4
1 5 2
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import static java.lang.Math.floorDiv;

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

class Node {
    int min = 0, max = 0;

    @Override
    public String toString() {
        return "(" + this.min + ", " + this.max + ")";
    }
}

public class Kquery {
    static int[] arr;
    static Node[] segTree;

    public static void main(String[] __) {
        FastIO sc = new FastIO();
        int n = sc.nextInt();
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        segTree = new Node[4 * n];
        for (int i = 0; i < segTree.length; i++) segTree[i] = new Node();
        build(0, n - 1, 0);
        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            int l = sc.nextInt() - 1;
            int r = sc.nextInt() - 1;
            int k = sc.nextInt() - 1;
            System.out.println(query(0, n - 1, l, r, 0, k));
        }
    }

    private static void build(int start, int end, int node) {
        if (start == end) {
            segTree[node].max = arr[start];
            segTree[node].min = arr[start];
        } else {
            int mid = floorDiv(start + end, 2);
            build(start, mid, 2 * node + 1);
            build(mid + 1, end, 2 * node + 2);
            segTree[node].min = Math.min(segTree[2 * node + 1].min, segTree[2 * node + 2].min);
            segTree[node].max = Math.max(segTree[2 * node + 1].max, segTree[2 * node + 2].max);
        }
    }

    // start l end r ; l start r end ; l start end r ; start l r end

    private static int query(int start, int end, int l, int r, int node, int k) {
        if ((l == start && r == end) || (l <= start && r <= end)) {
            if (segTree[node].min > k) return end - start + 1;
            else if (segTree[node].max < k) return 0;
            else {
                int mid = floorDiv(start + end, 2);
                return query(start, mid, l, r, 2 * node + 1, k) + query(mid + 1, end, l, r, 2 * node + 2, k);
            }
        } else if ((start <= l && end <= r) || (l <= start && r <= end) || (start <= l && r <= end)) {
            int mid = floorDiv(start + end, 2);
            return query(start, mid, l, r, 2 * node + 1, k) + query(mid + 1, end, l, r, 2 * node + 2, k);
        } else return 0;
    }
}
