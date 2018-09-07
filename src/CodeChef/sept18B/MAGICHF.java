package CodeChef.sept18B;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * Created by bk on 07-09-2018.
 */
public class MAGICHF {
    public static void main(String[] __) {
        FastIO sc = new FastIO();
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int n = sc.nextInt(), x = sc.nextInt(), s = sc.nextInt();
            int[] arr = new int[n + 1];
            arr[x] = 1;
            for (int i = 0; i < s; i++) {
                int a = sc.nextInt(), b = sc.nextInt();
                int temp = arr[a];
                arr[a] = arr[b];
                arr[b] = temp;
            }
            for (int i = 0; i < arr.length; i++) {
                if (arr[i] == 1) {
                    System.out.println(i);
                    break;
                }
            }
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
