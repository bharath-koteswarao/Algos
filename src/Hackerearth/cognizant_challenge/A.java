package Hackerearth.cognizant_challenge;

/*
 * Created by bk on 15-12-2017 21:13
 */

import java.util.Scanner;

public class A {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        StringBuffer st = new StringBuffer(sc.next());
        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            int a = sc.nextInt();
            char b = sc.next().charAt(0);
            a -= 1;
            st.setCharAt(a, b);
        }
        int m = sc.nextInt();
        System.out.println(st);
        String s = st.toString();
        for (int i = 0; i < m; i++) {
            int a = sc.nextInt(), b = sc.nextInt();
            a -= 1;
            b -= 1;
            s = s.substring(0, a) + rev(s.substring(a, b + 1)) + s.substring(b + 1);
        }
        System.out.println(s);
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            count += s.charAt(i) == st.charAt(i) ? 1 : 0;
        }
        System.out.println(count);
    }

    private static String rev(String s) {
        String ret = "";
        for (int i = s.length() - 1; i >= 0; i -= 1) {
            ret += s.charAt(i);
        }
        return ret;
    }
}
