package Hackerearth.codart;

/*
 * Created by bk on 10-02-2018 18:28
 */

import java.util.Scanner;

public class Pairs {
    private static long mod = 1000000009;

    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int n = sc.nextInt();
            long ans = 0;
            for (int i = n; i >= 0; i--) {
                for (int j = i - 1; j >= 0; j--) {
                    if (getSum(i) > getSum(j)) ans += 1;
                }
            }
            System.out.println(ans % mod);
        }
    }

    static int getSum(int n) {
        int su = 0;
        while (n > 0) {
            su += n % 10;
            n = n / 10;
        }
        return su;
    }
}
