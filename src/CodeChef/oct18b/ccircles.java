package CodeChef.oct18b;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

import static java.lang.Math.abs;
import static java.lang.Math.pow;
import static java.lang.Math.sqrt;

/**
 * Created by bk on 11-10-2018.
 */
public class ccircles {
    public static void main(String[] __) {
        FastIO sc = new FastIO();
        int n = sc.nextInt();
        int q = sc.nextInt();

        ArrayList<Circle> circles = new ArrayList<>();
        for (int i = 0; i < n; i++) circles.add(new Circle(sc.nextLong(), sc.nextLong(), sc.nextLong()));
        for (int q_i = 0; q_i < q; q_i++) {
            int k = sc.nextInt();
            int ans = 0;
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    Circle c1 = circles.get(i);
                    Circle c2 = circles.get(j);
                    double c1c2 = twoPointDistance(c1, c2);
                    Circle small = new Circle(c1.x, c1.y, abs(c1.r - k));
                    Circle big = new Circle(c1.x, c1.y, c1.r + k);
                    if (liesBetween(c2, small, big)) ans += 1;
                }
            }
        }
    }

    private static boolean liesBetween(Circle c2, Circle small, Circle big) {
        Point center = new Point(small.x, small.y);
        long radius_small = small.r;
        long radius_big = big.r;
        double dist = twoPointDistance(small, c2);
        double nd = dist - c2.r;
        double fd = dist + c2.r;
        if (nd <= radius_small && fd >= radius_big) return true;
        else if (radius_small <= nd && nd <= radius_big) return true;
        else return nd <= radius_small && radius_small <= fd && fd <= radius_big;
    }

    private static double twoPointDistance(Circle c1, Circle c2) {
        return sqrt(pow(abs(c1.x - c2.x), 2) + pow(abs(c1.y - c2.y), 2));
    }

    static class Point {
        long x;
        long y;

        Point(long x, long y) {
            this.x = x;
            this.y = y;
        }
    }

    static class Circle {
        long x, y, r;

        Circle(long x, long y, long r) {
            this.x = x;
            this.y = y;
            this.r = r;
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
