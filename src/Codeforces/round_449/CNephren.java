package Codeforces.round_449;

/*
 * Created by bk on 02-12-2017 21:01
 */

import java.util.ArrayList;
import java.util.Hashtable;
import java.util.List;
import java.util.Scanner;

class Pair {
    public int a, b;

    Pair(int a, int b) {
        this.a = a;
        this.b = b;
    }
}

public class CNephren {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int q = sc.nextInt();
        List<Pair> pairs = new ArrayList<>();
        int max = 0;
        for (int i = 0; i < q; i++) {
            int n = sc.nextInt(), k = sc.nextInt();
            pairs.add(new Pair(n, k));
            max = Math.max(max, n);
        }
        Hashtable<Integer, String> ht = new Hashtable<>();
        ht.put(0, "What are you doing at the end of the world? Are you busy? Will you save us?");
        f(max, ht);
        for (Pair p : pairs) {
            int a = p.a, b = p.b;
            String s = ht.get(a);
            if (b > s.length()) System.out.print(".");
            else System.out.print(s.charAt(b - 1));
        }
    }

    private static void f(int n, Hashtable<Integer, String> ht) {
        for (int i = 1; i <= n; i++) {
            ht.put(i, "What are you doing while sending \"" + ht.get(i - 1) + "\"? Are you busy? Will you send \"" + ht.get(i - 1) + "\"?");
        }
    }
}
