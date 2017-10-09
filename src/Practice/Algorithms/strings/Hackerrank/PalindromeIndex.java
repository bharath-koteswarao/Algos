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
                int count = 0;
                while (inp.charAt(0) == inp.charAt(inp.length() - 1)) {
                    inp = inp.substring(1, inp.length() - 1);
                    count += 1;
                }
                if (isPalindrome(inp.substring(1))) {
                    System.out.println(count);
                } else {
                    System.out.println(inp.length()-1);
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
