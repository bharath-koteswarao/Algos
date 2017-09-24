package Algorithms.dynamic_programming;

import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by BK on 24-09-2017.
 */
public class LongestCommonSequence {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int i_tc = 0; i_tc < tc; i_tc++) {
            sc.nextInt();
            sc.nextInt();
            String s1 = sc.next();
            String s2 = sc.next();
            int[][] memo = new int[s1.length()][s2.length()];
            for (int[] arr : memo) Arrays.fill(arr, -1);
            int answer = lcs(s1, s2, memo, 0, s1.length(), 0, s2.length());
            System.out.println(answer);
        }
    }

    private static int lcs(String s1, String s2, int[][] memo, int begin1, int end1, int begin2, int end2) {
        if (begin1 == end1 || begin2 == end2) return 0;
        if (s1.charAt(begin1) == s2.charAt(begin2)) {
            return 1 + lcs(s1, s2, memo, begin1 + 1, end1, begin2 + 1, end2);
        } else {
            if (memo[begin1][begin2] == -1) {
                memo[begin1][begin2] = Math.max(lcs(
                        s1, s2, memo, begin1 + 1, end1, begin2, end2
                ), lcs(
                        s1, s2, memo, begin1, end1, begin2 + 1, end2
                ));
                return memo[begin1][begin2];
            }
            return memo[begin1][begin2];
        }
    }
}
