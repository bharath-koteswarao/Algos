package CodeChef.sept18B;

/**
 * Created by bk on 07-09-2018.
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
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

public class CHEFADV {
    public static void main(String[] __) {
        FastIO sc = new FastIO();
        int tc = sc.nextInt();
        String yes = "Chefirnemo";
        String no = "Pofik";
        while (tc-- > 0) {
            long n = sc.nextLong(), m = sc.nextLong(), x = sc.nextLong(), y = sc.nextLong();
            long r1 = (n - 1) % x, r2 = (m - 1) % y;
            if (r1 == 0 && r2 == 0) System.out.println(yes);
            else if ((n - 2) % x == 0 && (m - 2) % y == 0) System.out.println(yes);
            else System.out.println(no);
        }
    }
}
