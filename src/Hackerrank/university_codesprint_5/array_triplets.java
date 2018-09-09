package Hackerrank.university_codesprint_5;

import java.util.ArrayList;
import java.util.Scanner;


public class array_triplets {
    static boolean[][] dp;
    static ArrayList<ArrayList<Integer>> answers;


    private static void printSubsetsRec(int arr[], int i, int sum, ArrayList<Integer> p) {
        if (i == 0 && sum != 0 && dp[0][sum]) {
            p.add(arr[i]);
            answers.add(new ArrayList<>(p));
            p.clear();
            return;
        }

        if (i == 0 && sum == 0) {
            answers.add(new ArrayList<>(p));
            p.clear();
            return;
        }

        if (dp[i - 1][sum]) {
            ArrayList<Integer> b = new ArrayList<>(p);
            printSubsetsRec(arr, i - 1, sum, b);
        }

        if (sum >= arr[i] && dp[i - 1][sum - arr[i]]) {
            p.add(arr[i]);
            printSubsetsRec(arr, i - 1, sum - arr[i], p);
        }
    }

    private static void findSubsets(int arr[], int n, int sum) {
        if (n == 0 || sum < 0)
            return;

        dp = new boolean[n][sum + 1];
        for (int i = 0; i < n; ++i) {
            dp[i][0] = true;
        }

        if (arr[0] <= sum)
            dp[0][arr[0]] = true;

        for (int i = 1; i < n; ++i)
            for (int j = 0; j < sum + 1; ++j)
                dp[i][j] = (arr[i] <= j) ? (dp[i - 1][j] ||
                        dp[i - 1][j - arr[i]])
                        : dp[i - 1][j];
        if (!dp[n - 1][sum]) {
            System.out.println("There are no subsets with" +
                    " sum " + sum);
            return;
        }
        ArrayList<Integer> p = new ArrayList<>();
        printSubsetsRec(arr, n - 1, sum, p);
    }

    public static void main(String args[]) {
        answers = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int sum = 0;
        for (int x : arr) sum += x;
        if (sum % 3 != 0) {
            System.out.println(0);
        } else {
            findSubsets(arr, n, sum / 3);
            System.out.println(answers);
        }
    }

    private static long factorial(int size) {
        long ret = 1;
        for (int i = 2; i <= size; i++) ret *= i;
        return ret;
    }
}
