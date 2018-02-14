package Hackerrank.week_of_code_36;

/*
 * Created by bk on 11-02-2018 19:19
 */

import java.util.Arrays;
import java.util.Scanner;

import static java.lang.Math.abs;

public class RaceAgTime {
    static long[][] movingCost;
    static long[][] memo;
    static long[] heights;
    static long[] prices;

    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        heights = new long[n + 1];
        prices = new long[n + 1];
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
//        for (long[] ar : movingCost) System.out.println(Arrays.toString(ar));
        System.out.println(getAns(0,0,n));
    }

    private static long getAns(int idx, long ans, int n) {
        if (idx == n) return ans;
        else {
            long min = Long.MAX_VALUE;
            boolean breakNext = false;
            while (idx < n & !breakNext) {
                min = Math.min(min, getAns(idx + 1, ans + (idx + 1 == n ? 0 : abs(heights[idx + 1] - heights[idx])) + prices[idx], n));
                if (breakNext) break;
                breakNext = heights[idx + 1] > heights[idx];
                idx += 1;
            }
            return min;
        }
    }
}
