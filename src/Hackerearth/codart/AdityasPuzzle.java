package Hackerearth.codart;

/*
 * Created by bk on 10-02-2018 23:50
 */

import java.util.Scanner;

public class AdityasPuzzle {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        long m = Long.MAX_VALUE;
        for (int l = 4; l < s.length(); l++) {
            for (int i = 0; i < s.length() - l + 1; i++) {
                String temp = s.substring(i, i + l);
                if (chk(temp)) m = Math.max(m, l);
            }
        }
        System.out.println(m);
    }

    private static boolean chk(String temp) {
        int[] arr = new int[26];
        for (int i = 0; i < temp.length(); i++) {
            arr[Integer.parseInt(temp.charAt(i)+"")] += 1;
        }
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] % 2 != 1) return false;
        }
        return true;
    }
}
