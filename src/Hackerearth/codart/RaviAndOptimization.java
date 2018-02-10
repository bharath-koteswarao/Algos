package Hackerearth.codart;

/*
 * Created by bk on 10-02-2018 16:41
 */

import java.util.Scanner;

public class RaviAndOptimization {
    public static void main(String[] __) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] ai = new int[n];
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            String inp = in.next();
            ai[i] = getNum(inp);
            max = Math.max(max, ai[i]);
        }
        int N = 32 - Integer.numberOfLeadingZeros(max);
        int a[] = new int[1 << N];
        for (int i = 0; i < n; i++) {
            a[ai[i]]++;
        }
        int F[] = new int[1 << N];
        for (int i = 0; i < (1 << N); ++i) {
            F[i] += a[i];
        }

        for (int i = 0; i < N; ++i) {
            for (int mask = 0; mask < (1 << N); ++mask) {
                if ((mask & (1 << i)) > 0)
                    F[mask] += F[mask ^ (1 << i)];
            }
        }

        long ans = 0;
        int val = (1 << N) - 1;
        for (int i = 0; i < n; i++) {
            ans += F[(~ai[i]) & val];
        }
        System.out.println(ans);
    }

    private static int getNum(String s) {
        int[] arr = new int[26];
        for (int i = 0; i < s.length(); i++) {
            arr[(int) s.charAt(i) - 'a'] = 1;
        }
        String st = "";
        for (int i = 0; i < arr.length; i++) {
            st += arr[i];
        }
        return Integer.parseInt(st, 2);
    }
}
