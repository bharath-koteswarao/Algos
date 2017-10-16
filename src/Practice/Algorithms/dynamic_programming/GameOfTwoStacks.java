package Algorithms.dynamic_programming;

import java.util.Scanner;

/**
 * Created by BK on 08-10-2017.
 */
public class GameOfTwoStacks {
    static int[] arr1;
    static int[] arr2;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int i_tc = 0; i_tc < tc; i_tc++) {
            int n1 = sc.nextInt();
            int n2 = sc.nextInt();
            int limit = sc.nextInt();
            arr1 = new int[n1];
            arr2 = new int[n2];
            for (int i = 0; i < n1; i++) {
                arr1[i] = sc.nextInt();
            }
            for (int i = 0; i < n2; i++) {
                arr2[i] = sc.nextInt();
            }
            int answer = find_max_score(0, 0, arr1.length, arr2.length, 0, limit);
            System.out.println(answer);
        }
    }

    private static int find_max_score(int i, int j, int max_i, int max_j, int current, int limit) {
        if (i < max_i && j < max_j && current < limit) {
            return Math.max(
                    1 + find_max_score(i + 1, j, max_i, max_j, current + arr1[i], limit),
                    1 + find_max_score(i, j + 1, max_i, max_j, current + arr2[j], limit)
            );
        } else if (current >= limit) {
            return 0;
        } else if (i < max_i && current < limit) {
            return 1 + go_through_stack1(i, max_i, current, limit);
        } else if (j < max_j && current < limit) {
            return 1 + go_through_stack2(j, max_j, current, limit);
        } else {
            return 0;
        }
    }

    private static int go_through_stack2(int j, int max_j, int current, int limit) {
        if (current == limit) return 0;
        else if (j < max_j) return 1 + go_through_stack2(j + 1, max_j, current + arr2[j], limit);
        else return 0;
    }

    private static int go_through_stack1(int i, int max_i, int current, int limit) {
        if (current == limit) return 0;
        else if (i < max_i) {
            return 1 + go_through_stack1(i + 1, max_i, current + arr1[i], limit);
        } else {
            return 0;
        }
    }
}
