package CodeChef.oct18b;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

/**
 * Created by bk on 08-10-2018.
 */
public class Hmappy {
    public static void main(String[] __) {
        FastIO sc = new FastIO();
        int n = sc.nextInt();
        int k = sc.nextInt();
        long balloons[] = new long[n];
        long cost[] = new long[n];
        for (int i = 0; i < n; i++) balloons[i] = sc.nextLong();
        for (int i = 0; i < n; i++) cost[i] = sc.nextLong();
        PriorityQueue<Pair> heap = new PriorityQueue<>();
        for (int i = 0; i < n; i++) heap.add(new Pair(balloons[i], cost[i]));
        while (k-- > 0) {
            Pair top = heap.remove();
            if (top.balloons == 0) break;
            top.balloons -= 1;
            heap.add(top);
        }
        Pair top = heap.remove();
        System.out.println(multiply(top.balloons, top.cost));
    }

    private static int getSize(long num) {
        int ctr = 0;
        while (num != 0) {
            ctr++;
            num /= 10;
        }
        return ctr;
    }

    private static long multiply(long x, long y) {
        int size1 = getSize(x);
        int size2 = getSize(y);
        int N = Math.max(size1, size2);
        if (N < 10) return x * y;
        N = (N / 2) + (N % 2);
        long m = (long) Math.pow(10, N);
        long b = x / m;
        long a = x - (b * m);
        long d = y / m;
        long c = y - (d * N);
        long z0 = multiply(a, c);
        long z1 = multiply(a + b, c + d);
        long z2 = multiply(b, d);
        return z0 + ((z1 - z0 - z2) * m) + (z2 * (long) (Math.pow(10, 2 * N)));
    }


    static class Pair implements Comparable<Pair> {

        long balloons;
        long cost;

        Pair(long balloons, long cost) {
            this.balloons = balloons;
            this.cost = cost;
        }

        @Override
        public int compareTo(Pair o) {
            return -Double.compare(multiply(balloons, cost), multiply(o.balloons, o.cost));
        }
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
