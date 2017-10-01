package Hackerrank;

import java.util.Scanner;

/**
 * Created by BK on 01-10-2017.
 */
public class snake_wind_final {
    static int n;
    static int c = 1;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int[][] matrix = new int[n][n];
        char wind_dir = sc.next().charAt(0);
        int x = sc.nextInt();
        int y = sc.nextInt();
        if (wind_dir == 'n') {
            if (x == 0 && y == 0) {
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        if (i % 2 == 1)
                            matrix[i][n - 1 - j] = c++;
                        else
                            matrix[i][j] = c++;
                    }
                }
            }
            if (x == 0 && y == n - 1) {
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        if (i % 2 == 0)
                            matrix[i][n - 1 - j] = c++;
                        else
                            matrix[i][j] = c++;
                    }
                }
            }
            if (x == n - 1 && y == 0) {
                for (int i = 0; i < n; i++) {
                    matrix[n - 1 - i][0] = c++;
                }
                for (int i = 0; i < n; i++) {
                    for (int j = 1; j < n; j++) {
                        System.out.println(i + ", " + j);
                        if (i % 2 == 0)
                            matrix[i][j] = c++;
                        else
                            matrix[i][n - j] = c++;
                    }
                }
            }
            if (x == n - 1 && y == n - 1) {
                for (int i = 0; i < n; i++) {
                    matrix[n - 1 - i][n - 1] = c++;
                }
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j <= n - 2; j++) {
                        if (i % 2 == 0)
                            matrix[i][n - 2 - j] = c++;
                        else
                            matrix[i][j] = c++;
                    }
                }
            }
        } else if (wind_dir == 's') {
            if (x == 0 && y == 0) {
                // Should be calculated
            } else if (x == n - 1 && y == 0) {
                goTopByRight(matrix);
            } else if (x == n - 1 && y == n - 1) {
                goTopByLeft(matrix);
            }
            if (x == 0 && y == n - 1) {
                // should be calculated
            }
        } else if (wind_dir == 'e') {
            if (x == 0 && y == 0) {
                for (int i = 0; i < n; i++) {
                    matrix[0][i] = c++;
                }
                for (int i = n - 1; i >= 0; i--) {
                    for (int j = 1; j < n; j++) {
                        if ((n - 1 - i) % 2 == 1)
                            matrix[n - j][i] = c++;
                        else
                            matrix[j][i] = c++;
                    }
                }
            }
            if (x == 0 && y == n - 1) {
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        if (i % 2 == 0)
                            matrix[j][n - 1 - i] = c++;
                        else
                            matrix[n - 1 - j][n - 1 - i] = c++;
                    }
                }
            }
            if (x == n - 1 && y == 0) {
                for (int i = 0; i < n; i++) {
                    matrix[n - 1][i] = c++;
                }
                for (int i = n - 1; i >= 0; i--) {
                    for (int j = 1; j < n; j++) {
                        if ((n - 1 - i) % 2 == 0)
                            matrix[n - 1 - j][i] = c++;
                        else
                            matrix[j - 1][i] = c++;
                    }
                }
            }
            if (x == n - 1 && y == n - 1) {
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        if (i % 2 == 1)
                            matrix[j][n - 1 - i] = c++;
                        else
                            matrix[n - 1 - j][n - 1 - i] = c++;
                    }
                }
            }
        } else if (wind_dir == 'w') {
            if (x == 0 && y == 0) {
                goBottomByRight(matrix);
                transpose(matrix);
            } else if (x == n - 1 && y == 0) {
                goTopByRight(matrix);
                transpose(matrix);
            } else if (x == 0 && y == n - 1) {
                // should be calculated
            } else if (x == n - 1 && y == n - 1) {
                // should be calculated
            }
        }
        for(int[] ar:matrix){
            for (int p=0;p<ar.length;p++) {
                System.out.print(ar[p]+" ");
            }
            System.out.println();
        }
    }

    private static void transpose(int[][] matrix) {
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0 + count; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
            count++;
        }
    }

    private static void goTopByRight(int[][] matrix) {
        int count = 0, num = 1;
        for (int i = n - 1; i >= 0; i--) {
            if (count % 2 == 0) {
                for (int j = 0; j < n; j++) {
                    matrix[j][i] = num;
                    num++;
                }
            } else {
                for (int j = n - 1; j >= 0; j--) {
                    matrix[j][i] = num;
                    num++;
                }
            }
            count++;
        }
    }

    private static void goTopByLeft(int[][] matrix) {
        int count = 0, num = 1;
        for (int j = n - 1; j >= 0; j--) {
            if (count % 2 == 1) {
                for (int i = 0; i < n; i++) {
                    matrix[j][i] = num;
                    num++;
                }
            } else {
                for (int i = n - 1; i >= 0; i--) {
                    matrix[j][i] = num;
                    num++;
                }
            }
            count++;
        }
    }

    private static void goBottomByLeft(int[][] matrix) {
        int count = 0, num = 1;
        for (int j = 0; j < n; j++) {
            if (count % 2 == 1) {
                for (int i = 0; i < n; i++) {
                    matrix[j][i] = num;
                    num++;
                }
            } else {
                for (int i = n - 1; i >= 0; i--) {
                    matrix[j][i] = num;
                    num++;
                }
            }
            count++;
        }
    }

    private static void goBottomByRight(int[][] matrix) {
        int count = 0, num = 1;
        for (int j = 0; j < n; j++) {
            if (count % 2 == 0) {
                for (int i = 0; i < n; i++) {
                    matrix[j][i] = num;
                    num++;
                }
            } else {
                for (int i = n - 1; i >= 0; i--) {
                    matrix[j][i] = num;
                    num++;
                }
            }
            count++;
        }
    }
}
