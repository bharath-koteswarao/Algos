package Algorithms.Implementation;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class NonDivisibleSubset {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), k = sc.nextInt();
        int[] inp = new int[n];
        for (int i = 0; i < n; i++) {
            inp[i] = sc.nextInt() % k;
        }
    }
}
