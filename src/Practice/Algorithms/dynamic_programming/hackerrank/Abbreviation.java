package Algorithms.dynamic_programming.hackerrank;

/*
 * Created by bk on 24-11-2017 18:26
 */

// todo identify the mistake in this code. Just debug this code

import Datastructures.bk;

import java.util.Scanner;

public class Abbreviation {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            String a = sc.next();
            String b = sc.next();
            int[] check = new int[26];
            for (int i = 0; i < a.length(); i++) {
                if (isCapital(a.charAt(i))) check[a.charAt(i) - 'A'] += 1;
            }
            bk.print_int(check);
            for (int i = 0; i < b.length(); i++) {
                check[b.charAt(i) - 'A'] -= 1;
            }
            bk.print_int(check);
            boolean initial = true;
            for (int i : check) {
                if (i > 0) {
                    initial = false;
                    break;
                }
            }
            if (initial) {
                boolean res = false;
                int i = 0, j = 0;
                while (true) {
                    if (b.charAt(i) == a.charAt(j) || b.charAt(i) == capitalize(a.charAt(j))) {
                        i += 1;
                        j += 1;
                    } else {
                        j += 1;
                    }
                    if (i == b.length()) {
                        res = true;
                        break;
                    } else if (j == a.length()) {
                        break;
                    }
                }
                System.out.println(res ? "YES" : "NO");
            } else {
                System.out.println("NO");
            }
        }
    }

    private static char capitalize(char ch) {
        return (char) ((int) ch - 32);
    }

    private static boolean isSmall(char ch) {
        int n = (int) ch;
        return n >= 97 && n <= 122;
    }

    private static boolean isCapital(char ch) {
        int n = (int) ch;
        return n >= 65 && n <= 90;
    }
}