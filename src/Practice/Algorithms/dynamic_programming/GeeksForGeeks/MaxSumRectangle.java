package Algorithms.dynamic_programming.GeeksForGeeks;

/*
 * Created by bk on 23-11-2017 15:29
 */


/*
4 5
1 2 -1 -4 -20 -8 -3 4 2 1 3 8 10 1 3 -4 -1 1 7 -6
*/

//todo getting wrong answer for this. Make it correct

import Datastructures.bk;

import java.util.Scanner;

public class MaxSumRectangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int rows = sc.nextInt(), cols = sc.nextInt();
            int[][] matrix = new int[rows][cols];
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    matrix[i][j] = sc.nextInt();
                }
            }
            for (int[] ar : matrix) bk.print_int(ar);
            int ans = 0;
            for (int i = 0; i < cols; i++) {
                for (int j = i + 1; j < cols; j++) {
                    int[] temp = new int[rows];
                    for (int p = 0; p < rows; p += 1) {
                        temp[p] = sum(p, i, j, matrix);
                    }
                    int cur = kadane(temp);
                    System.out.println(cur+" "+i+" "+j);
                    ans = Math.max(cur, ans);
                }
            }
            System.out.println(ans);
        }
    }

    private static int kadane(int[] array) {
        int cur = 0;
        int max = 0;
        for (int element : array) {
            cur += element;
            max = Math.max(cur, max);
            if (cur < 0) cur = 0;
        }
        return max;
    }

    private static int sum(int row, int start, int end, int[][] matrix) {
        int sum = 0;
        for (int i = start; i <= end; i++) {
            sum += matrix[row][i];
        }
        return sum;
    }
}
