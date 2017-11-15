package Hackerrank.WeekOfCode35;

import Datastructures.bk;

import java.util.Scanner;

public class Problem_C {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int l = sc.nextInt();
        int b = sc.nextInt();
        int[][] toy = new int[l + 2][b + 2];
        for (int i = 0; i < l; i++) {
            for (int j = 0; j < b; j++) {
                toy[i + 1][j + 1] = sc.nextInt();
            }
        }
        for (int[] ar : toy) {
            bk.print_int(ar);
        }
        int cost = 0;
        for (int i = 1; i < l + 1; i++) {
            for (int j = 1; j < b + 1; j++) {
                if (toy[i][j] > toy[i - 1][j]) {
                    cost += toy[i][j] - toy[i - 1][j];
                }
                if (toy[i][j] > toy[i][j - 1]) {
                    cost += toy[i][j] - toy[i][j - 1];
                }
                if (toy[i][j] > toy[i + 1][j]) {
                    cost += toy[i][j] - toy[i + 1][j];
                }
                if (toy[i][j] > toy[i][j + 1]) {
                    cost += toy[i][j] - toy[i][j + 1];
                }
                cost += 2;
            }
        }
        System.out.println(cost);
    }
}
