package Hackerearth.codearena.craig;

import java.util.Scanner;

/**
 * Created by bk on 25-08-2018.
 */
public class mcardle {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int n = sc.nextInt();
            int[][] mat = new int[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    mat[i][j] = sc.nextInt();
                }
            }
            int ans = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    for (int x = 0; x < n; x++) {
                        for (int y = 0; y < n; y++) {
                            if (mat[i][j] > mat[x][y] && i <= x && j <= y) ans += 1;
                        }
                    }
                }
            }
            System.out.println(ans);
        }
    }
}
