package CodeChef.oct18b;

import org.jetbrains.annotations.NotNull;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.Scanner;

/**
 * Created by bk on 05-10-2018.
 */


public class surchess {
    private static int[][] mat;
    private static int[][] invalid;
    private static int[][] correct;
    private static ArrayList<Pair> invalidPairs = new ArrayList<>();

    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();
        mat = new int[n][m];
        invalid = new int[n][m];
        correct = new int[n][m];
        HashMap<Integer, Integer> invalidX = new HashMap<>();
        HashMap<Integer, Integer> invalidy = new HashMap<>();
        PriorityQueue<Pair> heap = new PriorityQueue<>();
        int invalidCount = 0;
        for (int i = 0; i < n; i++) {
            String inp = sc.next();
            for (int j = 0; j < m; j++) {
                mat[i][j] = inp.charAt(j) == '1' ? 1 : 0;
            }
        }

        correct[0][0] = mat[0][0];
        for (int i = 1; i < m; i++) {
            correct[0][i] = correct[0][i - 1] == 1 ? 0 : 1;
        }

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < m; j++) {
                correct[i][j] = correct[i - 1][j] == 0 ? 1 : 0;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (mat[i][j] != correct[i][j]) {
                    invalid[i][j] = 1;
                    invalidCount += 1;
                    invalidPairs.add(new Pair(i, j));
                    invalidX.put(i, 1);
                    invalidy.put(j, 1);
                }
            }
        }
        int q = sc.nextInt();
        int[] queries = new int[q];
        for (int i = 0; i < q; i++) {
            queries[i] = sc.nextInt();
        }


        HashMap<Integer, Integer> answer = new HashMap<>();
        answer.put(invalidCount, Math.min(n, m));
        for (Pair pair : invalidPairs) {
            int top = 0, bottom = 0, left = 0, right = 0;

            int curX = pair.x;
            int curY = pair.y;


        }
    }

    private static int getRev(int x) {
        return (x + 1) % 2;
    }

    static class Pair implements Comparable<Pair> {

        int x, y;
        int max;

        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "(" + x + ", " + y + ")";
        }

        @Override
        public int compareTo(@NotNull Pair o) {
            return this.max - o.max;
        }

    }
}
