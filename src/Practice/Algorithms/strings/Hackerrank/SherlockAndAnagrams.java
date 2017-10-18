package Algorithms.strings.Hackerrank;

import java.util.Scanner;

/**
 * Created by BK on 18-10-2017.
 */
public class SherlockAndAnagrams {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int i_tc = 0; i_tc < tc; i_tc++) {
            String inp = sc.next();
            int answer = 0;
            String[][] strings = new String[inp.length()][inp.length()];
            int count = 0;
            for (int i = 0; i < inp.length(); i++) {
                for (int j = 0; j < inp.length() - count; j++) {
                    strings[count][j] = (inp.substring(j, j + count + 1));
                }
                count += 1;
            }
            for (String[] s : strings) {
                for (int i = 0; i < s.length; i++) {
                    for (int j = i + 1; j < s.length; j++) {
                        if (s[i] != null && s[j] != null && s[i].length() == s[j].length()) {
                            answer = are_anagrams(s[i], s[j]) ? answer + 1 : answer;
                        }
                    }
                }
            }
            System.out.println(answer);
        }
    }

    private static boolean are_anagrams(String a, String b) {
        int[] temp = new int[26];
        for (int i = 0; i < a.length(); i++) {
            temp[a.charAt(i) - 'a'] += 1;
        }
        for (int i = 0; i < b.length(); i++) {
            temp[b.charAt(i) - 'a'] -= 1;
        }
        for (int i : temp) {
            if (i != 0) return false;
        }
        return true;
    }
}
