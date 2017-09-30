package Hackerrank;

import java.util.Scanner;

import static java.lang.Math.abs;
import static java.lang.Math.max;

/**
 * Created by BK on 30-09-2017.
 */
public class ErruptingVolcanoes {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        int num = sc.nextInt();
        int[][] l = new int[size][size];
        int answer = 0;
        for (int i_tc = 0; i_tc < num; i_tc++) {
            int hor = sc.nextInt();
            int ver = sc.nextInt();
            int weight = sc.nextInt();
            int left = hor - (weight - 1);
            int right = hor + (weight - 1);
            int top = ver - (weight - 1);
            int down = ver + (weight - 1);
            for (int i = left; i < right + 1; i++) {
                for (int j = top; j < down + 1; j++) {
                    if (i < size && j < size && i >= 0 && j >= 0) {
                        if (i == hor && j == ver) l[i][j] += weight;
                        else if (i - hor == 0) l[i][j] += weight - abs(j - ver);
                        else if (j - ver == 0) l[i][j] += weight - abs(i - hor);
                        else l[i][j] += weight - max(abs(i - hor), abs(j - ver));
                        answer = max(answer, l[i][j]);
                    }
                }
            }
        }
        System.out.println(answer);
    }
}
