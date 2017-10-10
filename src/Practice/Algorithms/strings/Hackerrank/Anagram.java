package Algorithms.strings.Hackerrank;

import java.util.Scanner;

import static java.lang.Math.abs;
import static java.lang.Math.floorDiv;

/**
 * Created by BK on 10-10-2017.
 */
public class Anagram {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int i_tc = 0; i_tc < tc; i_tc += 1) {
            String s = sc.next();
            if (s.length() % 2 != 0) System.out.println(-1);
            else {
                String left = s.substring(0, floorDiv(s.length(), 2));
                String right = s.substring(floorDiv(s.length(), 2));
                int[] left_freq = new int[26];
                int[] right_freq = new int[26];
                for (int i = 0; i < left.length(); i++) {
                    left_freq[left.charAt(i) - 'a'] += 1;
                    right_freq[right.charAt(i) - 'a'] += 1;
                }
//                bk.print_int(left_freq);
//                bk.print_int(right_freq);
                int answer = 0;
                for (int i = 0; i < left_freq.length; i++) {
                    answer += abs(abs(left_freq[i]) - abs(right_freq[i]));
                }
                System.out.println(answer / 2);
            }
        }
    }
}
