package Hackerearth.paypal_challenge;

import java.util.Arrays;
import java.util.Scanner;

/*

4 4
....
.*.*
*.*.
****


 */

/**
 * Created by bk on 01-06-2018.
 */
public class Third {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();
        String[][] mat = new String[n][m];
        for (int i = 0; i < n; i++) {
            mat[i] = sc.next().split("");
        }
        int[][] counter = new int[n][m];
        int[] ans = new int[Math.min(n, m)];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (mat[i][j].equals("*")) ans[0] += 1;
            }
        }
        System.out.println(Arrays.toString(ans));
        for (int i = 0; i < n; i++) {
            if (mat[i][0].equals("*")) counter[i][0] = 1;
            else counter[i][0] = 0;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < m; j++) {
                if (mat[i][j].equals("*")) counter[i][j] = counter[i][j - 1] + 1;
                else counter[i][j] = counter[i][j - 1];
            }
        }
        show(counter);
        if (n < m) {

        }
    }

    private static void show(int[][] counter) {
        for (int[] arr : counter) System.out.println(Arrays.toString(arr));
    }
}
