package Hackerearth.codearena;

/*
 * Created by bk on 06-12-2017 23:07
 */

/*
4
0 0 0 0
2 0 1 0
0 2 1 2
0 1 2 0
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class FastIO {
    private BufferedReader br;
    private StringTokenizer st;

    FastIO() {
        br = new BufferedReader(new
                InputStreamReader(System.in));
    }

    public String next() {
        while (st == null || !st.hasMoreElements()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return st.nextToken();
    }

    public int nextInt() {
        return Integer.parseInt(next());
    }

    public long nextLong() {
        return Long.parseLong(next());
    }

    public double nextDouble() {
        return Double.parseDouble(next());
    }

    public String nextLine() {
        String str = "";
        try {
            str = br.readLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return str;
    }
}

public class RituDang {
    public static void main(String[] args) {
        FastIO sc = new FastIO();
        int n = sc.nextInt();
        int[][] mat = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                mat[i][j] = sc.nextInt();
            }
        }
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (mat[0][i] == 1) list.add(i);
        }
        boolean first = false, second = false;
        for (int i : list) {
            if (check(0, i, 1, mat)) {
                first = true;
                break;
            }
        }
        list.clear();
        mat = transpose(mat);
        for (int i = 0; i < n; i++) {
            if (mat[0][i] == 2) list.add(i);
        }
        for (int i : list) {
            if (check(0, i, 2, mat)) {
                second = true;
                break;
            }
        }
        System.out.println(first);
    }

    private static int[][] transpose(int[][] mat) {
        int transpose[][] = new int[mat.length][mat.length];
        for (int c = 0; c < mat.length; c++) {
            for (int d = 0; d < mat.length; d++)
                transpose[d][c] = mat[c][d];
        }
        return transpose;
    }

    private static boolean check(int i, int j, int num, int[][] matrix) {
        if (i == matrix.length - 1) {
            return true;
        } else if (j < matrix.length - 1) {
            boolean f = false, s = false, t = false;
            if (matrix[i + 1][j] == num) f = check(i + 1, j, num, matrix);
            if (matrix[i][j + 1] == num) s = check(i, j + 1, num, matrix);
            if (matrix[i + 1][j + 1] == num) t = check(i + 1, j + 1, num, matrix);
            return f || s || t;
        } else return false;
    }

    private static boolean check2(int i, int j, int num, int[][] matrix) {
        if (j == matrix.length - 1) {
            return true;
        } else if (i < matrix.length - 1) {
            boolean f = false, s = false, t = false;
            if (matrix[i + 1][j] == num) f = check2(i + 1, j, num, matrix);
            if (matrix[i][j + 1] == num) s = check2(i, j + 1, num, matrix);
            if (matrix[i + 1][j + 1] == num) t = check2(i + 1, j + 1, num, matrix);
            return f || s || t;
        } else return false;
    }
}
