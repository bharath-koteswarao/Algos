package Codeforces.round_449;

/*
 * Created by bk on 02-12-2017 19:38
 */

import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(),m = sc.nextInt();
        StringBuilder s = new StringBuilder(sc.next());
        while (m-- > 0) {
            int l = sc.nextInt(), r = sc.nextInt();
            char c1 = sc.next().charAt(0),c2 = sc.next().charAt(0);
            for (int i = l-1;i<=r-1;i++) {
                if (s.charAt(i) == c1) s.setCharAt(i,c2);
            }
        }
        System.out.println(s.toString());
    }
}
