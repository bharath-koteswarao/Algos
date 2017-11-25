package Hackerrank.codiva;

/*
 * Created by bk on 25-11-2017 17:48
 */

import Datastructures.bk;

import java.util.Scanner;

public class C {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sc.next();
        sc.next();
        int k = sc.nextInt();
        String s1 = sc.next(), s2 = sc.next();
        int[][] memo = new int[Math.max(s1.length(), s2.length()) + 1][Math.max(s1.length(), s2.length()) + 1];
        for (int[] ar : memo) {
            for (int i = 0; i < ar.length; i++) {
                ar[i] = -1;
            }
        }
        findLcs(s1, s2, 0, 0, memo);
        for (int[] ar:memo) bk.print_int(ar);
    }

    private static int findLcs(String s1, String s2, int i, int j, int[][] memo) {
        if (i < s1.length() && j < s2.length()) {
            if (s1.charAt(i) == s2.charAt(j)){
                if (memo[i+1][j+1] == -1) {
                    memo[i+1][j+1] = findLcs(s1, s2, i + 1, j + 1, memo);
                }
                return 1 + memo[i+1][j+1];
            }
            else {
                if (memo[i][j + 1] == -1) {
                    memo[i][j + 1] = findLcs(s1, s2, i, j + 1, memo);
                }
                if (memo[i + 1][j] == -1) {
                    memo[i + 1][j] = findLcs(s1, s2, i + 1, j, memo);
                }
                return Math.max(
                        memo[i][j + 1], memo[i + 1][j]
                );
            }
        }
        return 0;
    }
}
