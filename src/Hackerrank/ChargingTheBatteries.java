package Hackerrank;

import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by BK on 07-08-2017.
 */
public class ChargingTheBatteries {
    public static void main(String... args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt(), k = sc.nextInt();
        int[] newCoordinates = new int[m];
        for (int i = 0; i < m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            newCoordinates[i] = (x >= y) ? (x + y) : (-1 * (x + y));
        }
        Arrays.sort(newCoordinates);
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < newCoordinates.length; i++) {
            if ((i + k - 1) < newCoordinates.length) {
                int d1 = newCoordinates[i];
                int d2 = newCoordinates[(i + k - 1)];
                if ((d1 >= 0 && d2 >= 0) || (d1 < 0 && d2 < 0)) {
                    d1 = Math.abs(d1);
                    d2 = Math.abs(d2);
                    int comp = Math.abs(d1 - d2);
                    min = min > comp ? comp : min;
                } else {
                    d1 = Math.abs(d1);
                    d2 = Math.abs(d2);
                    int comp = Math.abs(d1 + d2);
                    min = min > comp ? comp : min;
                }
            } else {
                int d1 = newCoordinates[i];
                int d2 = newCoordinates[(i + k - 1) % newCoordinates.length];
                d1 = Math.abs(d1);
                d2 = Math.abs(d2);
                int comp = 4 * n - (d1 + d2);
                min = min > comp ? comp : min;
            }
        }
        System.out.println(min);
    }
}
