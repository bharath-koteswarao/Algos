package Datastructures.Stacks.Hackerrank_Problems;

import java.util.Scanner;

/**
 * Created by BK on 08-08-2017.
 */

public class GameOfTwoStacks {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int z = 0; z < tc; z++) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int x = sc.nextInt();
            int[] first = new int[n];
            int[] second = new int[m];
            for (int i = 0; i < n; i++) {
                first[i] = sc.nextInt();
            }
            for (int i = 0; i < m; i++) {
                second[i] = sc.nextInt();
            }
            int n1 = 0, n2 = 0, sum = 0, count = 0;
            while (sum < x && n1 < first.length && n2 < second.length) {
                if (first[n1] < second[n2]) {
                    sum += first[n1];
                    n1++;
                } else {
                    sum += second[n2];
                    n2++;
                }
                if (sum <= x) count++;
            }
            System.out.println(count);
        }
    }
}
