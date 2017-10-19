package Algorithms.strings.Hackerrank;

import Datastructures.bk;

import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by BK on 19-10-2017.
 */
public class CommonChild {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str1 = sc.next();
        String str2 = sc.next();
        int max = Math.max(str1.length(), str2.length());
        int[][] memo = new int[max + 1][max + 1];
        for (int[] arr : memo) {
            Arrays.fill(arr, -1);
        }
        int ans = find(str1, str2, 0, 0, memo);
        System.out.println(ans);
    }

    private static int find(String str1, String str2, int i, int j, int[][] memo) {
        if (memo[i][j] != -1) {
            return memo[i][j];
        } else if (i >= str1.length() || j >= str2.length()) {
            memo[i][j] = 0;
            return memo[i][j];
        } else if (str1.charAt(i) == str2.charAt(j)) {
            memo[i][j] = 1 + find(str1, str2, i + 1, j + 1, memo);
            return memo[i][j];
        } else {
            memo[i][j] = Math.max(
                    find(str1, str2, i + 1, j, memo),
                    find(str1, str2, i, j + 1, memo)
            );
            return memo[i][j];
        }
    }
}
