package Algorithms.strings.Hackerrank;

import java.util.Scanner;

public class MakingAnagrams {

    static int makingAnagrams(String s1, String s2) {
        // Complete this function
        int[] first = new int[26];
        for (int i = 0; i < s1.length(); i++) {
            first[s1.charAt(i) - 'a'] += 1;
        }
        for (int i = 0; i < s2.length(); i++) {
            first[s2.charAt(i) - 'a'] -= 1;
        }
        int count = 0;
        for (int i : first) {
            count += Math.abs(i);
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s1 = in.next();
        String s2 = in.next();
        int result = makingAnagrams(s1, s2);
        System.out.println(result);
    }
}
