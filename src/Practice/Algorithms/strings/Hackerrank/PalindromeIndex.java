package Algorithms.strings.Hackerrank;

import java.util.Scanner;

/**
 * Created by BK on 09-10-2017.
 */
public class PalindromeIndex {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int i_tc = 0; i_tc < tc; i_tc++) {
            String inp = sc.next();
            if (isPalindrome(inp)) System.out.println(-1);
            else {
                int i = 0;
                boolean found = false;
                int length = inp.length();
                while (!found) {
                    if (inp.charAt(i) == inp.charAt(length - i - 1)) {
                        i += 1;
                    } else {
                        if (isPalindrome(inp.substring(0,i)+inp.substring(i+1))) System.out.println(i);
                        else System.out.println(length - i - 1);
                        found = true;
                    }
                }
            }
        }
    }

    private static boolean isPalindrome(String inp) {
        for (int i = 0; i < Math.floorDiv(inp.length(), 2); i++) {
            if (inp.charAt(i) != inp.charAt(inp.length() - i - 1)) return false;
        }
        return true;
    }
}
