package CodeChef.aug18B;

/**
 * Created by bk on 09-08-2018.
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

public class kcompression {
    private static int[] arr;

    public static void main(String[] __) {
        FastIO sc = new FastIO();
        int n = sc.nextInt();
        arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = i;
        System.out.println(answer(0, arr.length));
    }

    private static boolean check(int n) {
        return n <= 15;
    }

    private static int answer(int start, int end) {
        int mid = (start + end) / 2;
        while (start != end) {
            if (check(mid)) {
                start = mid + 1;
            } else end = mid - 1;
            mid = (start + end) / 2;
        }
        return check(start) ? start : start - 1;
    }
}
