package Codeforces.round_466;

/*
 * Created by bk on 24-02-2018 15:24
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
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

public class B {
    static int k, a, b;
    static int n;
    static long[] memo;

    public static void main(String[] __) {
        FastIO sc = new FastIO();
        n = sc.nextInt();
        k = sc.nextInt();
        a = sc.nextInt();
        b = sc.nextInt();
        memo = new long[n + 1];
        Arrays.fill(memo, -1);
        long ans = getAns(n);
        System.out.println(ans);
    }

    private static long getAns(int n) {
        if (memo[n] != -1) return memo[n];
        else {
            if (n == 1) return 0;
            else if (n % k == 0) {
                return Math.min(a + getAns(n - 1), b + getAns(n / k));
            } else return a + getAns(n - 1);
        }
    }
}
