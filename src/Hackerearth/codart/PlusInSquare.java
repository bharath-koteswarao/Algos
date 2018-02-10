package Hackerearth.codart;

/*
 * Created by bk on 10-02-2018 19:04
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

public class PlusInSquare {
    private static double mod = 1000000009;

    public static void main(String[] __) {
        FastIO sc = new FastIO();
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int n = sc.nextInt();
            if (n == 0) {
                System.out.println(4);
            } else if (n == 1) {
                System.out.println(6);
            } else {
                double po = Math.pow(2, n - 1);
                System.out.println((long) (2 * (po * n - (po - 1)) % mod));
            }
        }
    }
}
