package Codeforces;

import java.util.Scanner;

/**
 * Created by BK on 30-07-2017.
 */
public class Spinner {
    public static void main(String... args) {
        Scanner sc = new Scanner(System.in);
        char[] positions = {'v', '<', '^', '>'};
        char[] posback = {'>', '^', '<', 'v'};
        char first = sc.next().charAt(0), second = sc.next().charAt(0);
        int pos1 = 0, pos2 = 0;
        for (int i = 0; i < positions.length; i++) {
            if (first == positions[i]) pos1 = i;
        }
        for (int i = 0; i < positions.length; i++) {
            if (first == posback[i]) pos2 = i;
        }
        int n = sc.nextInt();
        char forward = positions[(n + pos1) % positions.length];
        char backward = posback[(n + pos2) % positions.length];
        if (forward == backward) {
            System.out.println("undefined");
        } else if (forward == second) {
            System.out.println("cw");
        } else if (backward == second) {
            System.out.println("ccw");
        } else {
            System.out.println("undefined");
        }
    }
}
