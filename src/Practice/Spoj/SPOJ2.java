package Spoj;

/*
 * Created by bk on 05-12-2017 10:33
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class SPOJ2 {
    public static void main(String[] args) {
        FastIO sc = new FastIO();
        int tc = sc.nextInt(), max = 0;
        int[] tcs = new int[tc];
        for (int i = 0; i < tc; i++) {
            tcs[i] = sc.nextInt();
            max = Math.max(max, tcs[i]);
        }
        boolean[] primes = sieve(max);
        for (int i : tcs) {
            for (int p = 2; p <= i; p++) {
                if (primes[p]) System.out.print(p+" ");
            }
            System.out.println();
        }
    }

    static private boolean[] sieve(int n) {
        boolean prime[] = new boolean[n + 1];
        for (int i = 0; i < n; i++)
            prime[i] = true;
        for (int p = 2; p * p <= n; p++) {
            if (prime[p]) {
                for (int i = p * 2; i <= n; i += p)
                    prime[i] = false;
            }
        }
        return prime;
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
