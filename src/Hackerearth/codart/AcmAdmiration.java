package Hackerearth.codart;

/*
 * Created by bk on 10-02-2018 22:04
 */

import java.util.Scanner;

public class AcmAdmiration {

    // function to count the divisors
    static int countDivisors(int n) {
        int cnt = 0;
        for (int i = 1; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                // If divisors are equal,
                // count only one
                if (n / i == i)
                    cnt++;

                else // Otherwise count both
                    cnt = cnt + 2;
            }
        }
        return cnt;
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int n = sc.nextInt();
            int ans = 0;
            for (int i = 0; i <= n; i++) {
                if ((countDivisors(i) - 1) % 2 == 1) ans += 1;
            }
            System.out.println(ans);
        }
    }
}