package Codeforces;

import Practice.Datastructures.bk;

import java.util.Scanner;

/**
 * Created by BK on 12-08-2017.
 */
public class AryaAndBran {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt(), sum = 0;
        int[] candies = new int[n];
        candies[0] = Math.min(sc.nextInt(), 8);
        for (int i = 1; i < n; i++) {
            candies[i] = candies[i - 1] + Math.min(sc.nextInt(), 8);
        }
        for (int i = 0; i < candies.length; i++) {
            System.out.println(candies[i] + " " + i);
        }
        if (candies[candies.length - 1] < k) {
            System.out.println(-1);
            System.exit(0);
        }
        bk.print_int(candies);
        for (int i = 0; i < candies.length; i++) {
            if (candies[i] >= k) {
                System.out.println(i + 1);
                break;
            }
        }
    }
}