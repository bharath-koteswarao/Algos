package Codeforces.educational_round_36;

/*
 * Created by bk on 13-01-2018 19:57
 */

import java.util.Arrays;
import java.util.Scanner;

public class C {
    static void swap(char ar[], int i, int j) {
        char temp = ar[i];
        ar[i] = ar[j];
        ar[j] = temp;
    }

    static String findNext(char ar[], int n) {
        int i;
        for (i = n - 1; i > 0; i--) {
            if (ar[i] > ar[i - 1]) {
                break;
            }
        }
        if (i == 0) {
            return "";
        } else {
            int x = ar[i - 1], min = i;
            for (int j = i + 1; j < n; j++) {
                if (ar[j] > x && ar[j] < ar[min]) {
                    min = j;
                }
            }
            swap(ar, i - 1, min);
            Arrays.sort(ar, i, n);
            String ret = "";
            for (i = 0; i < n; i++) {
                ret += ar[i];
            }
            return ret;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong(), b = sc.nextLong();
        char digits[] = (a + "").toCharArray();
        int n = digits.length;
        long ans = 0;
        boolean found = false;
        String t = "";
        while (!(t = findNext(digits, n)).equals("")) {
            long l = Long.parseLong(t);
            if (l < b) {
                ans = l;
                found = true;
            } else break;
        }
        System.out.println(found ? ans : a);
    }
}