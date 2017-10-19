package Algorithms.strings.Hackerrank;

import java.util.Scanner;
import java.util.TreeSet;

/**
 * Created by BK on 19-10-2017.
 */
public class TwoCharacters {
    public static void main(String[] p) {
        Scanner sc = new Scanner(System.in);
        sc.next();
        String s = sc.next();
        TreeSet<Character> ts = new TreeSet<>();
        for (int i = 0; i < s.length(); i++) {
            ts.add(s.charAt(i));
        }
        char arr[] = new char[ts.size()];
        int t = 0;
        while (!ts.isEmpty()) {
            arr[t] = ts.pollFirst();
            t += 1;
        }
        int max = 0;
        for (int i = 0; i < arr.length; i++) {
            String temp = "";
            for (int j = i + 1; j < arr.length; j++) {
                for (int k = 0; k < s.length(); k++) {
                    char curr = s.charAt(k);
                    if (curr == arr[i] || curr == arr[j]) {
                        temp += (s.charAt(k));
                    }
                }
                System.out.println(temp);
                if (validate(temp)) {
                    System.out.println(temp);
                    max = Math.max(max, temp.length());
                }
            }
        }
        System.out.println(max);
    }

    private static boolean validate(String temp) {
        for (int i = 0; i < temp.length() - 1; i++) {
            if (temp.charAt(i) == temp.charAt(i + 1)) return false;
        }
        return true;
    }
}
