package Codeforces.round_513;

import java.util.HashMap;
import java.util.Scanner;

/**
 * Created by bk on 04-10-2018.
 */
public class A {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        char[] s = sc.next().toCharArray();
        int ei = 0;
        HashMap<Character, Integer> counter = new HashMap<>();
        for (char ch : s) {
            if (counter.containsKey(ch)) {
                counter.put(ch, counter.get(ch) + 1);
            } else counter.put(ch, 1);
        }
        for (char ch : s) {
            ei += ch == '8' ? 1 : 0;
        }
        if (ei == 0) {
            System.out.println(0);
        } else {
            long ans = fact(n - 1);
            for (char key : counter.keySet()) {
                ans = ans / fact(Integer.parseInt(key + ""));
            }
            System.out.println(ans);
        }
    }

    private static long fact(int x) {
        long ret = 1;
        for (int i = 1; i <= x; i++) ret *= i;
        return ret;
    }
}
