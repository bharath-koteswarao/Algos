package Hackerrank.university_codesprint_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashSet;
import java.util.StringTokenizer;

class Node implements Comparator<Node> {
    int x;
    int w;

    Node(int x, int w) {
        this.x = x;
        this.w = w;
    }

    public int compare(Node a, Node b) {
        return a.w - b.w;
    }

    public String toString() {
        return " " + w;
    }
}

public class Solution {
    public static void main(String[] args) {
        FastReader in = new FastReader();
        int t = in.nextInt();
        StringBuffer bf = new StringBuffer();
        for (int a0 = 0; a0 < t; a0++) {
            int n = in.nextInt();
            int m = in.nextInt();
            ArrayList<Node> graph[] = new ArrayList[n];
            for (int i = 0; i < n; i++) {
                graph[i] = new ArrayList<>();
            }
            for (int a1 = 0; a1 < m; a1++) {
                int x = in.nextInt();
                int y = in.nextInt();
                int r = in.nextInt();
                graph[x - 1].add(new Node(y - 1, r));
                graph[y - 1].add(new Node(x - 1, r));
            }
            int s = in.nextInt();
            s--;
            int ans[] = new int[n];
            for (int i = 0; i < n; i++)
                ans[i] = 100001;
            ans[s] = 0;
            boolean visited[] = new boolean[n];
            visited[s] = true;
            HashSet<Integer> k = new HashSet<>();
            k.add(s);
            for (int i = 0; i < n; i++) {
                int n2 = s;
                int min = 1000000;
                for (Integer x : k) {
                    for (Node temp : graph[x]) {
                        if (!visited[temp.x]) {
                            if (min > temp.w + ans[x]) {
                                min = temp.w + ans[x];
                                n2 = temp.x;
                            }

                        }
                    }
                }
                if (min != 1000000) {
                    ans[n2] = min;
                    visited[n2] = true;
                    k.add(n2);
                }


            }
            for (int i2 = 0; i2 < n; i2++) {
                if (ans[i2] == 100001)
                    ans[i2] = -1;
                if (i2 != s)
                    bf.append("" + ans[i2] + " ");


            }
            bf.append("\n");
        }

        System.out.println(bf);
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new
                    InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }

}