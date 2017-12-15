package Hackerrank.world_code_sprint_12;

/*
 * Created by bk on 15-12-2017 18:49
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Hashtable;
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

public class FactorialArray {
    public static void main(String[] __) {
        FastIO sc = new FastIO();
        int n = sc.nextInt(), q = sc.nextInt();
        long inp[] = new long[n], biggest = 0;
        for (int i = 0; i < n; i++) {
            inp[i] = sc.nextInt();
            biggest = Math.max(inp[i], biggest);
        }
        Hashtable<Long, Long> ht = fillFactorials(biggest);
        System.out.println(ht);
    }

    private static Hashtable<Long, Long> fillFactorials(long biggest) {
        Hashtable<Long, Long> ht = new Hashtable<>();
        long fact = 1;
        for (long i = 1; i <= biggest; i++) {
            fact *= i;
            ht.put(i, fact);
        }
        return ht;
    }
}
