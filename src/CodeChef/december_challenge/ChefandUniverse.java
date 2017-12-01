package CodeChef.december_challenge;

/*
 * Created by bk on 01-12-2017 18:53
 */

import java.util.Scanner;

import static java.lang.Math.min;

public class ChefandUniverse {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            int z = sc.nextInt();
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            long[][][] memo = new long[x + 1][y + 1][z + 1];
            for (int i = 0; i < memo.length; i++) {
                for (int j = 0; j < memo[i].length; j++) {
                    for (int k = 0; k < memo[i][j].length; k++) {
                        memo[i][j][k] = -1;
                    }
                }
            }
            long ans = convert(0, 0, 0, x, y, z, a, b, c, memo);
            System.out.println(ans);
        }
    }

    private static long convert(int p, int q, int r, int x, int y, int z, int a, int b, int c, long[][][] memo) {
        if (p == x && q == y && r == z) {
            memo[p][q][r] = 0;
            return 0;
        } else if (p > x || q > y || r > z) {
            return (long) Math.pow(10, 10);
        } else {
            if (memo[p][q][r] != -1) return memo[p][q][r];
            else {
                long f = a + convert(p + 1, q, r, x, y, z, a, b, c, memo);
                long s = a + convert(p, q + 1, r, x, y, z, a, b, c, memo);
                long t = a + convert(p, q, r + 1, x, y, z, a, b, c, memo);
                long fo = b + convert(p + 1, q + 1, r, x, y, z, a, b, c, memo);
                long fi = b + convert(p, q + 1, r + 1, x, y, z, a, b, c, memo);
                long si = b + convert(p + 1, q, r + 1, x, y, z, a, b, c, memo);
                long se = c + convert(p + 1, q + 1, r + 1, x, y, z, a, b, c, memo);
                long m1 = min(f, s);
                long m2 = min(t, m1);
                long m3 = min(fo, m2);
                long m4 = min(fi, m3);
                long m5 = min(si, m4);
                memo[p][q][r] = min(se, m5);
                return memo[p][q][r];
            }
        }
    }
}
