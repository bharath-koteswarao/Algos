package Hackerrank;


import java.util.Scanner;

/**
 * Created by BK on 30-09-2017.
 */
public class SnakeVsWind {
    static String top_left = "top_left", top_right = "top_right";
    static String bottom_left = "bottom_left", bottom_right = "bottom_right";
    static int size;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        size = sc.nextInt();
        int[][] matrix = new int[size][size];
        char wind_dir = sc.next().charAt(0);
        int start_y = sc.nextInt();
        int start_x = sc.nextInt();
        String snake_pos = dirToGo(size, start_y, start_x);
//        System.out.println(snake_pos+" is snake position");
        switch (snake_pos) {
            case "top_left": {
                goBottomByRight(matrix);
                if (wind_dir != 'n') {
                    transpose(matrix);
                }
                break;
            }
            case "top_right": {
                goBottomByLeft(matrix);
                if (wind_dir != 'n') {
                    transpose(matrix);
                }
                break;
            }
            case "bottom_left": {
                goTopByRight(matrix);
                if (wind_dir != 's') {
                    transpose(matrix);
                }
                break;
            }
            case "bottom_right": {
                goTopByLeft(matrix);
                if (wind_dir != 's') {
                    transpose(matrix);
                }
                break;
            }
        }
        for (int[] arr : matrix) {
            print_int(arr);
        }
    }

    private static void transpose(int[][] matrix) {
        int count = 0;
        for (int i = 0; i < size; i++) {
            for (int j = 0 + count; j < size; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
            count++;
        }
    }

    private static void goTopByRight(int[][] matrix) {
        int count = 0, num = 1;
        for (int i = size - 1; i >= 0; i--) {
            if (count % 2 == 0) {
                for (int j = 0; j < size; j++) {
                    matrix[j][i] = num;
                    num++;
                }
            } else {
                for (int j = size - 1; j >= 0; j--) {
                    matrix[j][i] = num;
                    num++;
                }
            }
            count++;
        }
    }

    private static void goTopByLeft(int[][] matrix) {
        int count = 0, num = 1;
        for (int j = size - 1; j >= 0; j--) {
            if (count % 2 == 1) {
                for (int i = 0; i < size; i++) {
                    matrix[j][i] = num;
                    num++;
                }
            } else {
                for (int i = size - 1; i >= 0; i--) {
                    matrix[j][i] = num;
                    num++;
                }
            }
            count++;
        }
    }

    private static void goBottomByLeft(int[][] matrix) {
        int count = 0, num = 1;
        for (int j = 0; j < size; j++) {
            if (count % 2 == 1) {
                for (int i = 0; i < size; i++) {
                    matrix[j][i] = num;
                    num++;
                }
            } else {
                for (int i = size - 1; i >= 0; i--) {
                    matrix[j][i] = num;
                    num++;
                }
            }
            count++;
        }
    }

    private static void goBottomByRight(int[][] matrix) {
        int count = 0, num = 1;
        for (int j = 0; j < size; j++) {
            if (count % 2 == 0) {
                for (int i = 0; i < size; i++) {
                    matrix[j][i] = num;
                    num++;
                }
            } else {
                for (int i = size - 1; i >= 0; i--) {
                    matrix[j][i] = num;
                    num++;
                }
            }
            count++;
        }
    }

    private static String dirToGo(int size, int start_y, int start_x) {
        if (start_x == 0 && start_y == 0) return top_left;
        else if (start_x == size - 1 && start_y == 0) return top_right;
        else if (start_x == 0 && start_y == size - 1) return bottom_left;
        else return bottom_right;
    }

    public static void print_int(int arr[]) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}
