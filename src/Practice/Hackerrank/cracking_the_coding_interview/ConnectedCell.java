package Hackerrank.cracking_the_coding_interview;

import java.util.ArrayList;
import java.util.Scanner;

import static java.lang.Long.max;

/**
 * Created by bk on 26-06-2018.
 */
class Pair {
    int x;
    int y;

    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}

public class ConnectedCell {
    static long[][] mat;
    static boolean[][] visited;

    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();
        mat = new long[n][m];
        visited = new boolean[n][m];
        long ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                mat[i][j] = sc.nextLong();
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (mat[i][j] == 1) {
                    if (!visited[i][j]) {
                        visited[i][j] = true;
                        ans = max(ans, 1 + dfsVisit(i, j, n, m));
                    }
                }
            }
        }
        System.out.println(ans);
    }

    private static long dfsVisit(int i, int j, int n, int m) {
        ArrayList<Pair> adj = getAdj(n, m, i, j);
        long ans = 0;
        for (Pair pair : adj) {
            if (!visited[pair.x][pair.y]) {
                visited[pair.x][pair.y] = true;
                ans += 1 + dfsVisit(pair.x, pair.y, n, m);
            }
        }
        return ans;
    }


    private static ArrayList<Pair> getAdj(int n, int m, int i, int j) {
        ArrayList<Pair> al = new ArrayList<>();
        if (i - 1 >= 0 && j - 1 >= 0 && mat[i - 1][j - 1] == 1) al.add(new Pair(i - 1, j - 1));
        if (i - 1 >= 0 && mat[i - 1][j] == 1) al.add(new Pair(i - 1, j));
        if (i - 1 >= 0 && j + 1 < m && mat[i - 1][j + 1] == 1) al.add(new Pair(i - 1, j + 1));
        if (j + 1 < m && mat[i][j + 1] == 1) al.add(new Pair(i, j + 1));
        if (i + 1 < n && j + 1 < m && mat[i + 1][j + 1] == 1) al.add(new Pair(i + 1, j + 1));
        if (i + 1 < n && mat[i + 1][j] == 1) al.add(new Pair(i + 1, j));
        if (i + 1 < n && j - 1 >= 0 && mat[i + 1][j - 1] == 1) al.add(new Pair(i + 1, j - 1));
        if (j - 1 >= 0 && mat[i][j - 1] == 1) al.add(new Pair(i, j - 1));
        return al;
    }
}
