package Codeforces.round__463;

/**
 * Created by bk on 06-09-2018.
 * <p>
 * <p>
 * Solid evidence to say that python is not for competitive programming
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class B {

    static long pre[][];
    private static long memo[];

    public static void main(String[] __) {
        memo = new long[1000000];
        pre = new long[10][1000000];

        for (int i = 0; i < 10; i++) pre[i][i] = 1;

        for (int i = 2; i <= 1000000; i++) {
            int val = f(i);
            for (int j = 0; j < 9; j++) {
                if (j == val - 1) pre[j][i - 1] = pre[j][i - 2] + 1;
                else pre[j][i - 1] = pre[j][i - 2];
            }
        }

        FastIO sc = new FastIO();
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int l = sc.nextInt(), r = sc.nextInt(), k = sc.nextInt();
            --l;
            --r;
            if (l == 0) System.out.println(pre[k - 1][r]);
            else System.out.println(pre[k - 1][r] - pre[k - 1][l - 1]);
        }

    }

    private static int f(int x) {
        if (x < 10) return x;
        int prod = 1;
        while (x != 0) {
            if (x % 10 != 0) prod *= (x % 10);
            x /= 10;
        }
        return f(prod);
    }

    static class FastIO {
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
}
