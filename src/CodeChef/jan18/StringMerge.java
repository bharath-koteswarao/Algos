package CodeChef.jan18;

/*
 * Created by bk on 10-01-2018 14:48
 1
10 10
apffcdgfqh
mnoazeff1h
mnoaazepffffcdgfq1hh 15
 */

import java.util.Arrays;
import java.util.Scanner;


public class StringMerge {
    static StringBuilder st1;
    static StringBuilder st2;

    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int n = sc.nextInt(), m = sc.nextInt();
            String s1 = sc.next(), s2 = sc.next();
            if (s1.equals(s2)) {
                System.out.println(n);
            } else {
                int[][] memo = new int[s1.length()][s2.length()];
                for (int[] arr : memo) Arrays.fill(arr, -1);
                st1 = new StringBuilder();
                st2 = new StringBuilder();
                char last = '_';
                for (int i = 0; i < s1.length(); i++) {
                    if (last == '_') last = s1.charAt(i);
                    if (last != s1.charAt(i)) {
                        st1.append(last);
                        last = s1.charAt(i);
                    }
                }
                st1.append(last);
                last = '_';
                for (int i = 0; i < s2.length(); i++) {
                    if (last == '_') last = s2.charAt(i);
                    if (last != s2.charAt(i)) {
                        st2.append(last);
                        last = s2.charAt(i);
                    }
                }
                st2.append(last);
                s1 = st1.toString();
                s2 = st2.toString();
                n = s1.length();
                m = s2.length();
                if (s1.equals(s2)) System.out.println(n);
                else {
                    int ans = lcs(memo, 0, n, 0, m);
                    System.out.println(m + n - ans);
                }
            }
        }
    }

    private static int lcs(int[][] memo, int begin1, int end1, int begin2, int end2) {
        if (begin1 == end1 || begin2 == end2) return 0;
        if (st1.charAt(begin1) == st2.charAt(begin2)) {
            return 1 + lcs(memo, begin1 + 1, end1, begin2 + 1, end2);
        } else {
            if (memo[begin1][begin2] == -1) {
                memo[begin1][begin2] = Math.max(lcs(memo, begin1 + 1, end1, begin2, end2),
                        lcs(memo, begin1, end1, begin2 + 1, end2));
                return memo[begin1][begin2];
            }
            return memo[begin1][begin2];
        }
    }
}
