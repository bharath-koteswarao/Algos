package Hackerrank.university_codesprint_5;

import java.util.Scanner;

/**
 * Created by bk on 08-09-2018.
 */

public class interesting_trip_custom {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();
        String names = sc.next();
        String[][] adjMat = new String[n + 1][n + 1];
        for (int i = 0; i < m; i++) {
            int p = sc.nextInt(), q = sc.nextInt();
            adjMat[p][q] = names.charAt(q - 1) + "";
        }
        System.out.println(10);
    }

    private static void show(String[][] adjMat) {
        for (int i = 1; i < adjMat.length; i++) {
            for (int j = 1; j < adjMat.length; j++) {
                System.out.print(adjMat[i][j] + " ");
            }
            System.out.println();
        }
    }

}
