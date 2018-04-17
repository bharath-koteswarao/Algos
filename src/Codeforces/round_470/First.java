package Codeforces.round_470;

/*
 * Created by bk on 10-03-2018 21:17
 */

import java.util.Scanner;

public class First {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt(), c = sc.nextInt();
        char[][] arr = new char[r][c];
        for (int i = 0; i < r; i++) {
            arr[i] = sc.next().toCharArray();
        }
        int w = 0;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (arr[i][j] == 'W') w += 1;
            }
        }
        if (w == 0) prnt(arr);
        else {
            boolean valid = true;
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    try {
                        if (arr[i][j] == 'S') {
                            if (arr[i + 1][j] == 'W' || arr[i - 1][j] == 'W' || arr[i][j - 1] == 'W' || arr[i][j + 1] == 'W') {
                                valid = false;
                            } else {
                                if (arr[i + 1][j] == '.') arr[i + 1][j] = 'D';
                                if (arr[i - 1][j] == '.') arr[i - 1][j] = 'D';
                                if (arr[i][j - 1] == '.') arr[i][j - 1] = 'D';
                                if (arr[i][j + 1] == '.') arr[i][j + 1] = 'D';
                            }
                        }
                    } catch (Exception ignored) {
                    }
                    if (!valid) break;
                }
                if (!valid) break;
            }
            if (valid) prnt(arr);
            else {
                System.out.println("No");
            }
        }
    }

    private static void prnt(char[][] arr) {
        for (char[] a : arr) {
            for (char x : a) System.out.print(x);
            System.out.println();
        }
    }
}
