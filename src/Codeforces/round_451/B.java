package Codeforces.round_451;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * Created by bk on 07-09-2018.
 */
public class B {
    public static void main(String[] __) {
        FastIO sc = new FastIO();
        long n = sc.nextLong();
        long a = sc.nextLong();
        long b = sc.nextLong();
        long g = gcd(a, b);
        if (n % g == 0 && n >= Math.max(a, b)) {
            System.out.println("YES");
            long x = 0, y = 0;
            if (a > b) {
                x = n / a;
                n = n % a;
                if (n % b == 0) y = n / b;
                else {
                    x -= 1;
                    n += a;
                    y = n / b;
                }
                System.out.println(x + " " + y);
            } else {
                x = n / b;
                n = n % b;
                if (n % a == 0) {
                    y = n / a;
                } else {
                    x -= 1;
                    n += b;
                    y = n / a;
                }
                System.out.println(y + " " + x);
            }
        } else System.out.println("NO");
    }

    public static long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
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
