package Codeforces.adhoc_300;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

/**
 * Created by bk on 23-08-2018.
 */



public class tprimes {

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

    public static void main(String[] __) {
        FastIO sc = new FastIO();
        int n = sc.nextInt();
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextLong();
        Set<Long> primes = sieveOfEratosthenes((int) (Math.pow(10, 6) + 1));
        for (long x : arr) {
            long sqrt = (int) Math.sqrt(x);
            if (sqrt * sqrt == x) {
                if (primes.contains(sqrt)) System.out.println("YES");
                else System.out.println("NO");
            } else System.out.println("NO");
        }
    }

    private static Set<Long> sieveOfEratosthenes(int n) {
        Set<Long> primes = new HashSet<>();
        boolean prime[] = new boolean[n + 1];
        for (int i = 0; i < n; i++)
            prime[i] = true;

        for (int p = 2; p * p <= n; p++) {
            if (prime[p]) for (int i = p * 2; i <= n; i += p) prime[i] = false;
        }

        for (int i = 2; i <= n; i++) {
            if (prime[i]) primes.add((long) i);
        }

        return primes;
    }
}
