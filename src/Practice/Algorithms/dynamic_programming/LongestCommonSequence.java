package Algorithms.dynamic_programming;

import Datastructures.bk;

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
            int[][] bu_memo = new int[s1.length() + 1][s2.length() + 1];
            int bu_ans = bottom_up(s1, s2, bu_memo);
            for (int[] ar:bu_memo) bk.print_int(ar);
            System.out.println(bu_ans);
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
    private static int bottom_up(String s1, String s2, int[][] bu_memo) {
        for (int j = s2.length() - 1; j >= 0; j--) {
            for (int i = s1.length() - 1; i >= 0; i--) {
                if (s1.charAt(i) == s2.charAt(j)) bu_memo[i][j] = 1 + bu_memo[i + 1][j + 1];
                else bu_memo[i][j] = Math.max(bu_memo[i][j + 1], bu_memo[i + 1][j]);
            }
        }
        return bu_memo[0][0];
    }
}
