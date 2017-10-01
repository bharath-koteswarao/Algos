package Hackerrank;

import java.util.Scanner;

/**
 * Created by BK on 01-10-2017.
 */
public class BoBGame {
    static int k11 = 0, k12 = 0, k13 = 0, k21 = 0, k22 = 0, k23 = 0;
    static int[][][][] checker;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int tc_i = 0; tc_i < tc; tc_i++) {
            k11 = 0;    //left
            k12 = 0;    //top left
            k13 = 0;    // up
            k21 = 0;
            k22 = 0;
            k23 = 0;
            int n = sc.nextInt();
            char[][] matrix = new char[n][n];
            checker = new int[n][n][n][n];
            int k1i = -1, k1j = -1, k2i = -1, k2j = -1;
            for (int i = 0; i < n; i++) {
                matrix[i] = sc.next().toCharArray();
                for (int j = 0; j < n; j++) {
                    if (k1i == -1 || k2i == -1) {
                        if (matrix[i][j] == 'K' && k1i == -1) {
                            k1i = i;
                            k1j = j;
                        } else if (matrix[i][j] == 'K' && k1i != -1) {
                            k2i = i;
                            k2j = j;
                        }
                    }
                }
            }
            number_of_ways(k1i, k1j, k2i, k2j, matrix);
            int count = 0;
            if (k11 % 2 == 1) count++;
            if (k12 % 2 == 1) count++;
            if (k13 % 2 == 1) count++;
            if (k21 % 2 == 1) count++;
            if (k22 % 2 == 1) count++;
            if (k23 % 2 == 1) count++;
            System.out.println(count > 0 ? "WIN " + count : "LOSE");
            System.out.println(k11 + " " + k12 + " " + k13 + " " + k21 + " " + k22 + " " + k23);
        }
    }

    private static int number_of_ways(int k1i, int k1j, int k2i, int k2j, char[][] matrix) {
        if (k1i > 0 || k1j > 0 || k2i > 0 || k2j > 0) {
            // Now both of them cannot be at left most edge
            if (k1i <= 0 && k1j <= 0) {
                // Stop this k1 king and move k2 king
                if (k2j - 1 >= 0 && checker[0][0][k2i][k2j - 1] == 0 && matrix[k2i][k2j - 1] != 'X') {
                    // Move k2 to left
                    checker[0][0][k2i][k2j - 1] = 1;
                    k21 += 1 + number_of_ways(0, 0, k2i, k2j - 1, matrix);
                }
                if (k2j - 1 >= 0 && k2i - 1 >= 0 && checker[k1i][k1j][k2i - 1][k2j - 1] == 0 && matrix[k2i - 1][k2j - 1] != 'X') {
                    // Move k2 to top left
                    checker[0][0][k2i - 1][k2j - 1] = 1;
                    k22 += 1 + number_of_ways(0, 0, k2i - 1, k2j - 1, matrix);
                }
                if (k2i - 1 >= 0 && checker[0][0][k2i - 1][k2j] == 0 && matrix[k2i - 1][k2j] != 'X') {
                    // Move k2 to top
                    checker[0][0][k2i - 1][k2j] = 1;
                    k23 += 1 + number_of_ways(0, 0, k2i - 1, k2j, matrix);
                }
            } else if (k2i <= 0 && k2j <= 0) {
                // Stop moving k2 king and move k1 king
                if (k1j - 1 >= 0 && checker[k1i][k1j - 1][0][0] == 0 && matrix[k1i][k1j - 1] != 'X') {
                    // Move k1 to left
                    checker[k1i][k1j - 1][0][0] = 1;
                    k11 += 1 + number_of_ways(k1i, k1j - 1, 0, 0, matrix);
                }
                if (k1j - 1 >= 0 && k1i - 1 >= 0 && checker[k1i - 1][k1j - 1][0][0] == 0 && matrix[k1i - 1][k1j - 1] != 'X') {
                    // Move k1 to top left
                    checker[k1i - 1][k1j - 1][0][0] = 1;
                    k12 += 1 + number_of_ways(k1i - 1, k1j - 1, 0, 0, matrix);
                }
                if (k1i - 1 >= 0 && checker[k1i - 1][k1j][0][0] == 0 && matrix[k1i - 1][k1j] != 'X') {
                    // Move k1 to top
                    checker[k1i - 1][k1j][0][0] = 1;
                    k13 += 1 + number_of_ways(k1i - 1, k1j, 0, 0, matrix);
                }
            } else {
                /*
                 *  k1i-1,kj   Move up if it this configuration is not there in checker and it is not X
                 *  k1i-1,kj-1 Move top left
                 *  k1i,kj-1   Move left
                 */
                if (k1j - 1 >= 0 && checker[k1i][k1j - 1][k2i][k2j] == 0 && matrix[k1i][k1j - 1] != 'X') {
                    // Move k1 to left
                    checker[k1i][k1j - 1][k2i][k2j] = 1;
                    k11 += number_of_ways(k1i, k1j - 1, k2i, k2j, matrix);
                }
                if (k1j - 1 >= 0 && k1i - 1 >= 0 && checker[k1i - 1][k1j - 1][k2i][k2j] == 0 && matrix[k1i - 1][k1j - 1] != 'X') {
                    // Move k1 to top left
                    checker[k1i - 1][k1j - 1][k2i][k2j] = 1;
                    k12 += number_of_ways(k1i - 1, k1j - 1, k2i, k2j, matrix);
                }
                if (k1i - 1 >= 0 && checker[k1i - 1][k1j][k2i][k2j] == 0 && matrix[k1i - 1][k1j] != 'X') {
                    // Move k1 to top
                    checker[k1i - 1][k1j][k2i][k2j] = 1;
                    k13 += number_of_ways(k1i - 1, k1j, k2i, k2j, matrix);
                }
                if (k2j - 1 >= 0 && checker[k1i][k1j][k2i][k2j - 1] == 0 && matrix[k2i][k2j - 1] != 'X') {
                    // Move k2 to left
                    checker[k1i][k1j][k2i][k2j - 1] = 1;
                    k21 += number_of_ways(k1i, k1j, k2i, k2j - 1, matrix);
                }
                if (k2j - 1 >= 0 && k2i - 1 >= 0 && checker[k1i][k1j][k2i - 1][k2j - 1] == 0 && matrix[k2i - 1][k2j - 1] != 'X') {
                    // Move k2 to top left
                    checker[k1i][k1j][k2i - 1][k2j - 1] = 1;
                    k22 += number_of_ways(k1i, k1j, k2i - 1, k2j - 1, matrix);
                }
                if (k2i - 1 >= 0 && checker[k1i][k1j][k2i - 1][k2j] == 0 && matrix[k2i - 1][k2j] != 'X') {
                    // Move k2 to top
                    checker[k1i][k1j][k2i - 1][k2j] = 1;
                    k23 += number_of_ways(k1i, k1j, k2i - 1, k2j, matrix);
                }
            }
        }
        return 0;
    }
}
