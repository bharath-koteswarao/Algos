package Hackerearth.codearena;

/*
 * Created by bk on 08-12-2017 00:34
 */

import java.io.BufferedInputStream;
import java.util.Hashtable;
import java.util.Scanner;

public class NidhiBedi {
    public static void main(String[] args) {
        Scanner sc = new Scanner(new BufferedInputStream(System.in));
        while (sc.hasNext()) {
            Hashtable<Integer, Integer> ht = new Hashtable<>();
            int n = sc.nextInt();
            int ans = get_max(n, ht);
            System.out.println(ans);
        }

    }

    private static int get_max(int n, Hashtable<Integer, Integer> ht) {
        if (n <= 11) {
            return n;
        } else {
            if (ht.containsKey(n)) return ht.get(n);
            else {
                int a = get_max(Math.floorDiv(n, 2), ht);
                int b = get_max(Math.floorDiv(n, 3), ht);
                int c = get_max(Math.floorDiv(n, 4), ht);
                ht.put(n, Math.max(a + b + c, n));
                return ht.get(n);
            }
        }
    }
}
