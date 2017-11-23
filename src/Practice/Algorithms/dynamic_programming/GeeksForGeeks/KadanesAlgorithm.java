package Algorithms.dynamic_programming.GeeksForGeeks;

/*
 * Created by bk on 23-11-2017 14:47
 */

import java.util.Scanner;

public class KadanesAlgorithm {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int n = sc.nextInt();
            int[] inp = new int[n];
            for (int i = 0; i < n; i++) {
                inp[i] = sc.nextInt();
            }
            int pos = 0, neg = 0, smallest = inp[0], biggest = inp[0];
            for (int i : inp) {
                if (i > 0) {
                    pos += 1;
                } else {
                    neg += 1;
                }
                smallest = Math.min(smallest, i);
                biggest = Math.max(biggest, i);
            }
            if (pos == n) System.out.println(sum(inp));
            else if (neg == n) System.out.println(biggest);
            else {
                int cur = 0, max = 0;
                for (int i = 0; i < inp.length; i++) {
                    cur += inp[i];
                    max = Math.max(cur, max);
                    if (cur < 0) cur = 0;
                }
                System.out.println(max);
            }
        }
    }

    private static int sum(int[] inp) {
        int s = 0;
        for (int i : inp) s += i;
        return s;
    }
}
