package Hackerrank.week_of_code_36;

/*
 * Created by bk on 11-02-2018 19:19
 */

import java.util.Arrays;
import java.util.Scanner;

import static java.lang.Math.abs;
import static java.lang.Math.min;

public class RaceAgTime {
    static long[][] movingCost;
    static long[][] memo;

    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] heights = new long[n + 1];
        long[] prices = new long[n + 1];
        heights[0] = sc.nextInt();
        prices[0] = 0;
        for (int i = 1; i < n; i++) heights[i] = sc.nextInt();
        for (int i = 1; i < n; i++) prices[i] = sc.nextInt();
        movingCost = new long[n + 1][n + 1];
        for (long[] arr : movingCost) Arrays.fill(arr, -1);
        for (int i = 0; i < n + 1; i++) {
            boolean breakNext = false;
            for (int j = i + 1; j < n + 1; j++) {
                if (breakNext) break;
                else {
                    if (heights[j] > heights[i]) breakNext = true;
                    long cost = (j == n ? (0) : abs(heights[i] - heights[j])) + prices[j];
                    movingCost[i][j] = cost;
                }
            }
        }
        movingCost[0][0] = 0;
        for (long[] ar : movingCost) System.out.println(Arrays.toString(ar));
        long ans = getAns(0, 1, 0, n);
        System.out.println(ans);
    }

    private static long getAns(int i, int j, long ans, int n) {
        System.out.println(i+" "+j);
        if (j == n) return ans;
        else {
            long mi = Long.MAX_VALUE;
            while (movingCost[i][j] != -1 && j < n) {
                mi = min(mi, getAns(j, j + 1, ans + movingCost[i][j], n));
                j += 1;
            }
            return mi;
        }
    }
}
