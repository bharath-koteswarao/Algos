package Algorithms.strings.Hackerrank;

import java.util.Hashtable;
import java.util.Scanner;

/**
 * Created by BK on 08-10-2017.
 */
public class CaesarAndCipher {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Hashtable<Integer, Character> smalls = new Hashtable<>();
        Hashtable<Integer, Character> capitals = new Hashtable<>();
        for (int i = 0; i < 26; i++) {
            smalls.put(i, (char) ('a' + i));
        }
        for (int i=0;i<26;i++) {
            capitals.put(i,(char)('A'+i));
        }
        sc.next();
        String s = sc.next(),answer = "";
        int rotate = sc.nextInt();
        for (int i=0;i<s.length();i++) {
            if (smalls.containsKey(s.charAt(i)-'a')) {
                answer += smalls.get((s.charAt(i)-'a' + rotate) % 26);
            } else if (capitals.containsKey(s.charAt(i) - 'A')) {
                answer += capitals.get((s.charAt(i) - 'A' + rotate) % 26);
            } else {
                answer += s.charAt(i);
            }
        }
        System.out.println(answer);
    }
}