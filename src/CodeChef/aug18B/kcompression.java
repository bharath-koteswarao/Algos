package CodeChef.aug18B;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

/**
 * Created by bk on 09-08-2018.
 */

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

class Pair implements Comparable<Pair> {
    int idx;
    int val;

    Pair(int idx, int val) {
        this.idx = idx;
        this.val = val;
    }

    @Override
    public int compareTo(Pair o) {
        if (this.val == o.val) return this.idx - o.idx;
        else return this.val - o.val;
    }

    @Override
    public String toString() {
        return "(" + this.idx + ", " + this.val + ")";
    }
}

public class kcompression {
    private static int[] arr;

    public static void main(String[] __) {
        FastIO sc = new FastIO();
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int n = sc.nextInt(), sum = sc.nextInt();
            arr = new int[n];
            for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
//            System.out.println(answer(0, arr.length, sum) + 1);
            check(1, sum);
        }
    }

    private static boolean check(int n, int sum) {
        if (n == 0) return arr.length <= sum;
        else {
            int[] ans = new int[arr.length];
            for (int i = 0; i < ans.length; i++) {
                if (ans[i] == 0) find(i, ans, n);
            }
            System.out.println(Arrays.toString(ans));
            int su = 0;
            for (int el : ans) su += el;
            return su <= sum;
        }
    }

    private static void find(int idx, int[] ans, int n) {
        PriorityQueue<Pair> heap = new PriorityQueue<>();
        int last = Math.min(idx + n, ans.length - 1);
        for (int i = idx; i <= last; i++) {
            if (arr[i] <= arr[idx] && ans[i] == 0) {
                heap.add(new Pair(i, arr[i]));
            }
        }
        Pair top = heap.peek();
        if (top != null && top.idx == idx) {
            int start = Math.max(0, idx - n);
            int end = Math.min(idx + n, ans.length - 1);
            int ma = 0;
            for (int i = start; i <= end; i++) {
                if (arr[i] < arr[idx]) ma = Math.max(ma, ans[i]);
            }
            ans[top.idx] = ma + 1;
        } else if (heap.size() == 1) {
            int start = Math.max(0, idx - n);
            int end = Math.min(idx + n, ans.length - 1);
            int ma = 0;
            for (int i = start; i <= end; i++) {
                if (arr[i] < arr[idx]) ma = Math.max(ma, ans[i]);
            }
            ans[heap.remove().idx] = ma + 1;
        } else {
            while (!heap.isEmpty()) {
                Pair cur = heap.remove();
                find(cur.idx, ans, n);
            }
        }
    }

    private static int answer(int start, int end, int sum) {
        int mid = (start + end) / 2;
        while (start != end) {
            if (check(mid, sum)) {
                start = mid + 1;
            } else end = mid - 1;
            mid = (start + end) / 2;
        }
        return check(start, sum) ? start : start - 1;
    }
}
