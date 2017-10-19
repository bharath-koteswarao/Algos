package Algorithms.strings.Hackerrank;

import java.util.Hashtable;
import java.util.Scanner;

/**
 * Created by BK on 19-10-2017.
 */
public class TwoStrings {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int tc_i = 0; tc_i < tc; tc_i++) {
            String s1 = sc.next(), s2 = sc.next();
            boolean valid = false;
            Hashtable<Character, Integer> ht = new Hashtable<>();
            for (int i = 0; i < s1.length(); i++) {
                if (!ht.containsKey(s1.charAt(i))) {
                    ht.put(s1.charAt(i), 1);
                }
            }
            for (int i=0;i<s2.length();i++) {
                if (ht.containsKey(s2.charAt(i))) {
                    valid = true;
                }
            }
            System.out.println(valid?"YES":"NO");
        }
    }
}
