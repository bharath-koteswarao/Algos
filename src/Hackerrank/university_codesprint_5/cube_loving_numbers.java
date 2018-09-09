package Hackerrank.university_codesprint_5;

import java.util.ArrayList;
import java.util.Scanner;

import static java.lang.Math.*;

/**
 * Created by bk on 09-09-2018.
 */
public class cube_loving_numbers {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        int ma = (int) ceil(cbrt(n));
        ArrayList<Integer> primes = sieveOfEratosthenes(ma + 1);
        long ans = 0;
        for (int i = 0; i < primes.size(); i++) {
            long cur = floorDiv(n, (long) pow(primes.get(i), 3));
            ans += cur;
            for (int j = i + 1; j < primes.size(); j++) {
                long cub = (long) pow(primes.get(j), 3);
                ans -= floorDiv(cur, cub);
            }
        }
        System.out.println(ans);
    }

    private static ArrayList<Integer> sieveOfEratosthenes(int n) {
        boolean prime[] = new boolean[n + 1];
        for (int i = 0; i < n; i++) prime[i] = true;

        for (int p = 2; p * p <= n; p++) {
            if (prime[p]) {
                for (int i = p * 2; i <= n; i += p) prime[i] = false;
            }
        }
        ArrayList<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            if (prime[i]) primes.add(i);
        }
        return primes;
    }
}
