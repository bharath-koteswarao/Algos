package Hackerrank.cracking_the_coding_interview;

import java.util.Hashtable;
import java.util.Scanner;

public class LonelyInteger {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int a[] = new int[n];
        for (int a_i = 0; a_i < n; a_i++) {
            a[a_i] = in.nextInt();
        }
        Hashtable<Integer, Integer> ht = new Hashtable<>();
        for (int i = 0; i < a.length; i++) {
            int el = a[i];
            if (ht.containsKey(el)) {
                System.out.println(ht.get(el));

            } else ht.put(el, 1);
        }
        for (int i : a) {
            if (ht.get(i) == 1) {
                System.out.println(i);
                break;
            }
        }
    }
}
