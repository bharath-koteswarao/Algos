package Algorithms.strings.Hackerrank;

import java.util.Scanner;

/**
 * Created by BK on 19-10-2017.
 */
public class StringConstruction {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int tc_i = 0; tc_i < tc; tc_i++) {
            String s = sc.next();
            int[] arr = new int[26];
            for (int i = 0; i < s.length(); i++) {
                arr[s.charAt(i) - 'a'] += 1;
            }
            int count = 0;
            for (int i = 0; i < arr.length; i++) {
                count += arr[i] == 0 ? 0 : 1;
            }
            System.out.println(count);
        }
    }
}
