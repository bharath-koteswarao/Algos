package Datastructures.Arrays;

/**
 * Created by BK on 09-10-2017.
 */

import java.util.Scanner;

public class ArrayManipulation {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();
        long inp[] = new long[n];
        for (int i = 0; i < m; i++) {
            int a = sc.nextInt(), b = sc.nextInt(), k = sc.nextInt();
            inp[a - 1] += k;
            if (b < n) {
                inp[b] -= k;
            }
        }
        long sum = 0, max = -1;
        for (int i = 0; i < inp.length; i++) {
            sum += inp[i];
            max = Math.max(max, sum);
        }
        System.out.println(max);
    }
}