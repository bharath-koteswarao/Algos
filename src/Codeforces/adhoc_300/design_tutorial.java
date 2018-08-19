package Codeforces.adhoc_300;

import java.math.BigInteger;
import java.util.Scanner;

/**
 * Created by bk on 19-08-2018.
 */
public class design_tutorial {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n % 4 == 0) {
            System.out.println((n / 2) + " " + (n / 2));
        } else {
            int a = n - 2;
            while (isPrime(a) || isPrime(n - a)) {
                a -= 1;
            }
            System.out.println(a + " " + (n - a));
        }
    }

    private static boolean isPrime(int n) {
        return (new BigInteger(n + "")).isProbablePrime(1);
    }
}
