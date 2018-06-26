package Hackerrank.cracking_the_coding_interview;

import java.math.BigInteger;
import java.util.Scanner;

/**
 * Created by bk on 26-06-2018.
 */
public class Primality {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int nu = sc.nextInt();
            System.out.println((new BigInteger(nu + "")).isProbablePrime(1) ? "Prime" : "Not prime");
        }
    }
}
