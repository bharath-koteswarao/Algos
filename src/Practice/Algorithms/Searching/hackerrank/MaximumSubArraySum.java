package Algorithms.Searching.hackerrank;

/*
 * Created by bk on 24-11-2017 21:35
 */

import java.util.Scanner;

public class MaximumSubArraySum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int n = sc.nextInt();
            long m = sc.nextLong();
            long[] inp = new long[n];
            for (int i = 0; i < n; i++) {
                inp[i] = sc.nextLong();
            }
            long ma = 0, c = 0, t = 0;
            for (long el : inp) {
                c += el;
                if (c >= m) c = 0;
                t += el;
                ma = Math.max(Math.max(c, ma), t % m);
            }
            System.out.println(ma);
        }
    }
}
