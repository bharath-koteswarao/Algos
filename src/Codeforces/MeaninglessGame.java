package Codeforces;

/**
 * Created by BK on 30-07-2017.
 */

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class MeaninglessGame {

    public static List<Integer> primeFactors(int numbers) {
        int n = numbers;
        List<Integer> factors = new ArrayList<>();
        for (int i = 2; i <= n / i; i++) {
            while (n % i == 0) {
                factors.add(i);
                n /= i;
            }
        }
        if (n > 1) {
            factors.add(n);
        }
        return factors;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int i = 0; i < tc; i++) {
            int intezerNotZero = 0, factorOfThree = 0;
            int a = sc.nextInt(), b = sc.nextInt(), largestPrimeFactor = 0;
            List<Integer> l1 = primeFactors(a);
            List<Integer> l2 = primeFactors(b);


            for (int j = 0; j < l1.size(); j++) {
                if (largestPrimeFactor < l1.get(j)) largestPrimeFactor = l1.get(j);
            }


            for (int j = 0; j < l2.size(); j++) {
                if (largestPrimeFactor < l2.get(j)) largestPrimeFactor = l2.get(j);
            }


            int arr[] = new int[largestPrimeFactor + 1];
            for (int j = 0; j < l1.size(); j++) {
                arr[l1.get(j)]++;
            }
            for (int j = 0; j < l2.size(); j++) {
                arr[l2.get(j)]++;
            }
            System.out.println(largestPrimeFactor);

            for (int j = 0; j < arr.length; j++) {
                if (arr[j] != 0) intezerNotZero++;
            }
            for (int j = 0; j < arr.length; j++) {
                if (arr[j] % 3 == 0 && arr[j] != 0) factorOfThree++;
            }
            if (intezerNotZero == factorOfThree) System.out.println("Yes");
            else {
                System.out.println("No");
            }
        }
    }
}