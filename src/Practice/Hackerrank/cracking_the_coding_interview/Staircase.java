package Hackerrank.cracking_the_coding_interview;

import java.util.Hashtable;
import java.util.Scanner;

/**
 * Created by bk on 26-06-2018.
 */
public class Staircase {
    static Hashtable<Long, Long> memo;

    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        memo = new Hashtable<>();
        memo.put(0L, 1L);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            long n = sc.nextLong();
            if (memo.containsKey(n)) System.out.println(memo.get(n));
            else {
                int[] arr = {1, 2, 3};
                long ans = get(n, arr);
                System.out.println(ans);
            }
        }
    }

    private static long get(long n, int[] arr) {
        if (memo.containsKey(n)) return memo.get(n);
        else {
            if (n == 0) return 1;
            else if (n <= 0) return 0;
            else {
                long ans = 0;
                for (int i : arr) ans += get(n - i, arr);
                memo.put(n, ans);
                return ans;
            }
        }
    }
}
