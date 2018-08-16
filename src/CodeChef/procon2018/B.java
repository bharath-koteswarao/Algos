package CodeChef.procon2018;

/**
 * Created by bk on 16-08-2018.
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Collections;
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
    public static void main(String[] __) {
        FastIO sc = new FastIO();
        DecimalFormat df = new DecimalFormat("#.######");
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int n = sc.nextInt();
            ArrayList<Double> list = new ArrayList<>();
            for (int i = 0; i < n; i++) list.add(sc.nextDouble());
            Collections.sort(list);
            while (list.size() > 1) {
                double a = list.get(list.size() - 1);
                double b = list.get(list.size() - 2);
                list.remove(list.size() - 1);
                list.remove(list.size() - 1);
                double avg = Double.parseDouble(df.format((a + b) / 2));
                int idx = Collections.binarySearch(list, avg);
                if (idx < 0) {
                    idx = Math.abs(idx) - 1;
                }
                list.add(idx, avg);
            }
            System.out.println(list.get(0));
        }
    }
}
