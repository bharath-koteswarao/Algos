package CodeChef.jan18;

/*
 * Created by bk on 05-01-2018 17:52
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
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

public class KCON {
    public static void main(String[] __) {
        FastIO sc = new FastIO();
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int n = sc.nextInt(), k = sc.nextInt();
            List<Integer> list = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                list.add(sc.nextInt());
            }
            int p = 0, ne = 0, sum = 0, max = 0;
            for (int i : list) {
                if (i >= 0) p += 1;
                else ne += 1;
                sum += i;
                max = Math.max(max, i);
            }
            if (p == n) {
                System.out.println(k * sum);
            } else if (ne == n) {
                System.out.println(max);
            } else {
                List<Integer> l = new ArrayList<>();
                int s = 0;
                for (int i : list) {
                    if (i >= 0) s += i;
                    else {
                        l.add(s);
                        l.add(i);
                        s = 0;
                    }
                }
                if (s != 0) l.add(s);
                list = l;
                double cur = 0, ma = -1000000000000.0;
                for (int i = 0; i < n * k; i++) {
                    cur += list.get(ind(i, n));
                    ma = Math.max(ma, cur);
                    cur = cur < 0 ? 0 : cur;
                }
                System.out.println((long) ma);
            }
        }
    }

    private static int ind(long x, int n) {
        return (int) (x % n);
    }
}
