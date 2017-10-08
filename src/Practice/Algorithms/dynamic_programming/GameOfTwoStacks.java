package Algorithms.dynamic_programming;

import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by BK on 08-10-2017.
 */
public class GameOfTwoStacks {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int i_tc = 0; i_tc < tc; i_tc++) {
            int n1 = sc.nextInt();
            int n2 = sc.nextInt();
            int limit = sc.nextInt();
            int[] arr1 = new int[n1];
            int[] arr2 = new int[n2];
            for (int i = 0; i < n1; i++) {
                arr1[i] = sc.nextInt();
            }
            for (int i = 0; i < n2; i++) {
                arr2[i] = sc.nextInt();
            }
            int[][] memo = new int[n1][n2];
            for (int[] arr : memo) {
                Arrays.fill(arr, -100);
            }
            int ans = find_max_score(arr1, arr2, 0, 0, limit, n1, n2, memo);
            System.out.println(ans);
        }
    }

    private static int find_max_score(int[] arr1, int[] arr2, int start1, int start2, int limit, int max_start1, int max_start2, int[][] memo) {

        if (start1 < max_start1 && start2 < max_start2 && limit > 0) {
            if (limit - arr1[start1] >= 0 && limit - arr2[start2] >= 0) {
                if (memo[start1][start2] != -100) {
                    return memo[start1][start2];
                } else {
                    memo[start1][start2] = Math.max(
                            1 + find_max_score(arr1, arr2, start1 + 1, start2, limit - arr1[start1], max_start1, max_start2, memo),
                            1 + find_max_score(arr1, arr2, start1, start2 + 1, limit - arr2[start2], max_start1, max_start2, memo)
                    );
                    return memo[start1][start2];
                }
            } else if ((limit - arr1[start1]) >= 0) {
                if (memo[start1][start2] != -100) {
                    return memo[start1][start2];
                } else {
                    memo[start1][start2] = 1 + find_max_score(arr1, arr2, start1 + 1, start2, limit - arr1[start1], max_start1, max_start2, memo);
                    return memo[start1][start2];
                }
            } else if ((limit - arr2[start2]) >= 0) {
                if (memo[start1][start2] != -100) {
                    return memo[start1][start2];
                } else {
                    memo[start1][start2] = 1 + find_max_score(arr1, arr2, start1, start2 + 1, limit - arr2[start2], max_start1, max_start2, memo);
                    return memo[start1][start2];
                }
            } else {
                return 0;
            }
        } else {
            return 0;
        }
    }
}
