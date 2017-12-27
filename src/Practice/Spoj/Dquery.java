package Spoj;

/*
 * Created by bk on 27-12-2017 15:06
 * 5
10 10 10 10 10
3
1 5
2 4
3 5
 */


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Hashtable;
import java.util.StringTokenizer;


class Query implements Comparable {
    int l, r, i;

    public Query(int l, int r, int i) {
        this.l = l;
        this.r = r;
        this.i = i;
    }

    @Override
    public String toString() {
        return "(" + this.l + ", " + this.r + ", " + this.i + ")";
    }

    @Override
    public int compareTo(Object o) {
        Query q = (Query) o;
        return this.l != q.l ? this.l - q.l : this.r - q.r;
    }
}

public class Dquery {
    public static void main(String[] __) {
        FastIO sc = new FastIO();
        int max = 0;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            max = Math.max(max, arr[i]);
        }
        int q = sc.nextInt();
        Query[] queries = new Query[q];
        for (int i = 0; i < q; i++) {
            int l = sc.nextInt(), r = sc.nextInt();
            queries[i] = new Query(l - 1, r - 1, i);
        }
        Arrays.sort(queries);
        int cl = 0, cr = 0;
        int curs = 0;
        boolean first = true;
        Hashtable<Integer, Integer> answers = new Hashtable<>();
        int[] freq = new int[max + 1];
        int ans = 0;
        for (Query query : queries) {
            int l = query.l, r = query.r;
            for (int i = cl; i < l; i++) {
                freq[arr[i]] -= 1;
                ans -= freq[arr[i]] == 0 ? 1 : 0;
            }
            for (int i = cl - 1; i >= l; i--) {
                freq[arr[i]] += 1;
                ans += freq[arr[i]] == 1 ? 1 : 0;
            }
            cl = l;
            for (int i = cr; i > r; i--) {
                freq[arr[i]] -= 1;
                ans -= freq[arr[i]] == 0 ? 1 : 0;
            }
            for (int i = cr + 1; i <= r; i++) {
                /* This loop assumes that it has calculated values for cr - 1
                 * But for first time it starts from 1 leaving zero
                 * So 0th pos should be added manually
                 */
                if (first) {
                    freq[arr[0]] += 1;
                    ans += freq[arr[0]] == 1 ? 1 : 0;
                    first = false;
                }
                freq[arr[i]] += 1;
                ans += freq[arr[i]] == 1 ? 1 : 0;
            }
            cr = r;
            answers.put(query.i, ans);
        }
        for (int i = 0; i < q; i++) {
            System.out.println(answers.get(i));
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
