package Codeforces.round_457;

/*
 * Created by bk on 20-01-2018 11:07
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

import static java.lang.Math.floorDiv;

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

public class Second {
    public static void main(String... __) {
        FastIO sc = new FastIO();
        long n = sc.nextLong(), k = sc.nextLong();
        String bin = Long.toBinaryString(n);
        List<Integer> ones = new ArrayList<>();
        for (int i = 0; i < bin.length(); i++) {
            if (bin.charAt(i) == '1') {
                ones.add(i);
            }
        }
        System.out.println(ones);
        Collections.reverse(ones);
        System.out.println(ones);
        if (k < ones.size()) {
            System.out.println("No");
        } else {
            long dif = k - ones.size();
            StringBuilder ans = new StringBuilder();
            if (dif == 0) {
                for (int i : ones) ans.append(i);
                System.out.println("Yes");
                System.out.println(ans);
            } else {
                max_heapify(ones);
                for (int i = 0; i < dif; i++) {
                    int num = pop_heap(ones);
                    push_heap(ones, num - 1);
                    push_heap(ones, num - 1);
                }
                ones.sort(Collections.reverseOrder());
                for (int i : ones) ans.append(i);
                System.out.println("Yes");
                System.out.println(ans);
            }
        }
    }

    private static void push_heap(List<Integer> list, int val) {
        list.add(val);
        siftup(list, list.size() - 1);
    }

    private static void siftup(List<Integer> list, int i) {
        int parent = floorDiv(list.size(), 2);
        if (list.get(parent) < list.get(i)) Collections.swap(list, i, parent);
        if (parent > 0) siftup(list, parent);
    }

    private static int pop_heap(List<Integer> list) {
        int n = list.size() - 1;
        Collections.swap(list, 0, n);
        int max = list.remove(n);
        siftdown(list, 0);
        return max;
    }

    private static void max_heapify(List<Integer> list) {
        int n = list.size() - 1;
        for (int i = floorDiv(n, 2); i >= 0; i -= 1) {
            siftdown(list, i);
        }
    }

    private static void siftdown(List<Integer> list, int i) {
        int child = 2 * i + 1;
        if (child <= list.size() - 1) {
            if ((child + 1 <= list.size() - 1) && list.get(child + 1) > list.get(child)) child += 1;
            if (list.get(i) < list.get(child)) {
                Collections.swap(list, i, child);
                siftdown(list, child);
            }
        }
    }
}
