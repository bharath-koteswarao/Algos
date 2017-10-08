package Algorithms.strings.Hackerrank;

import java.util.Scanner;

/**
 * Created by BK on 08-10-2017.
 */
public class HackerrankInAString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int i = 0; i < tc; i++) {
            String s = sc.next(), comp = "hackerrank";
            while (!comp.equals("") && !s.equals("")) {
                if (s.charAt(0) == comp.charAt(0)) {
                    s = s.substring(1);
                    comp = comp.substring(1);
                } else {
                    s = s.substring(1);
                }
            }
            System.out.println(comp.equals("") ? "YES" : "NO");
        }
    }
}
