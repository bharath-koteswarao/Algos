package Algorithms.strings.Hackerrank;

import java.util.Scanner;

/**
 * Created by BK on 19-10-2017.
 */
public class GameOfThrones1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String inp = sc.next();
        int[] arr = new int[26];
        boolean valid = true;
        for (int i = 0; i < inp.length(); i++) {
            arr[inp.charAt(i) - 'a'] += 1;
        }
        if (inp.length() % 2 == 0) {
            for (int i = 0; i < arr.length; i++) {
                if (arr[i] % 2 != 0) {
                    valid = false;
                    break;
                }
            }
        } else {
            int count = 0;
            for (int i = 0; i < arr.length; i++) {
                if (arr[i] % 2 != 0) {
                    count += 1;
                }
                if (count == 2) {
                    valid = false;
                    break;
                }
            }
        }
        System.out.println(valid ? "YES" : "NO");
    }
}
