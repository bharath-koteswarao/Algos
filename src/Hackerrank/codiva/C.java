package Hackerrank.codiva;

/*
 * Created by bk on 25-11-2017 17:48
 */

/*
1 1 1
werlo
hello
 */

import Datastructures.bk;

import java.util.Arrays;
import java.util.Scanner;

public class C {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sc.next();
        sc.next();
        int k = sc.nextInt();
        String s1 = sc.next(), s2 = sc.next();
        int[][] memo = new int[s1.length() + 1][s2.length() + 1];
        for (int[] ar : memo) Arrays.fill(ar, 0);
        int lcs = findLcs(s1, s2, 0, 0, memo);
        for (int[] ar : memo) bk.print_int(ar);
        System.out.println(getLcs(s1, s2, memo, s1.length() - 1, s2.length() - 1));
        if (lcs >= k) System.out.println(0);
        else if (lcs + k > s2.length() || lcs + k > s1.length()) {
            System.out.println(-1);
        } else {
            String seq = getLcs(s1, s2, memo, s1.length(), s2.length());
        }
    }

    private static String getLcs(String s1, String s2, int[][] memo, int i, int j) {
        String ret = "";
        int cur = 0;
        while (i >= 0 && j >= 0) {

        }
        return ret;
    }

    private static int findLcs(String s1, String s2, int i, int j, int[][] memo) {
        if (memo[i][j] != 0) return memo[i][j];
        else if (i != s1.length() && j != s2.length()) {
            if (s1.charAt(i) == s2.charAt(j)) {
                memo[i][j] = 1 + findLcs(s1, s2, i + 1, j + 1, memo);
                return memo[i][j];
            } else {
                memo[i][j] = Math.max(
                        findLcs(s1, s2, i, j + 1, memo),
                        findLcs(s1, s2, i + 1, j, memo)
                );
                return memo[i][j];
            }
        } else {
            return 0;
        }
    }
}
