package Algorithms.dynamic_programming.GeeksForGeeks;

/*
 * Created by bk on 24-11-2017 12:27
 */

import java.util.Scanner;

class InterleavedStrings {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            String a = sc.next(), b = sc.next(), c = sc.next();
            System.out.println(check(a, c) && check(b, c) ? 1 : 0);
        }
    }

    private static boolean check(String a, String c) {
        int i = 0, j = 0;
        while (true) {
            if (a.charAt(i) == c.charAt(j)) {
                i += 1;
                j += 1;
            } else {
                j += 1;
            }
            if (i == a.length()) {
                return true;
            } else if (j == c.length()) {
                return false;
            }
        }
    }
}
