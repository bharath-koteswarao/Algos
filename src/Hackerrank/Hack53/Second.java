package Hackerrank.Hack53;

/*
 * Created by bk on 02-03-2018 21:04
 */

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Pair {
    int x, y;

    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Second {

    static int matrix[][] = {{0, 1, 2, 3}, {4, 5, 6, 7}, {8, 9, 10, 11}, {12, 13, 14, 15}};

    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt(), x = sc.nextInt(), y = sc.nextInt();
        if ((n * m - x - y) == 0 || (n * m - x - y) % 2 == 1) {
            System.out.println("NO");
        } else {
            System.out.println("YES");
            List<Pair> pairs = new ArrayList<>();
//            for (int i = x; i < n * m - y; i++) {
//                int ro = i / 4, co = i % 4 * ((i / 4 + 1) & 1) + (3 - i % 4) * ((i / 4) & 1);
////            int el = matrix[i / 4][i % 4 * ((i / 4 + 1) & 1) + (3 - i % 4) * ((i / 4) & 1)];
//                pairs.add(new Pair(ro, co));
//            }
            boolean r = false;
            for (int i = 0; i < n; i++) {
                if (i == 0) {
                    for (int j = x; j < m; j++) {
                        pairs.add(new Pair(i, j));
                    }
                } else if (i == n - 1) {
                    if (r) {
                        for (int j = m - y - 1; j >= 0; j--) {
                            pairs.add(new Pair(i, j));
                        }
                    } else {
                        for (int j = 0; j < m - y; j++) {
                            pairs.add(new Pair(i, j));
                        }
                    }
                } else {
                    if (r) {
                        for (int j = m - 1; j >= 0; j--) {
                            pairs.add(new Pair(i, j));
                        }
                    } else {
                        for (int j = 0; j < m; j++) {
                            pairs.add(new Pair(i, j));
                        }
                    }
                }
                r = !r;
            }
            System.out.println(pairs.size() / 2);
            for (int i = 0; i < pairs.size() - 1; i += 2) {
                System.out.print((pairs.get(i).x + 1) + " " + (pairs.get(i).y + 1) + " ");
                System.out.println((pairs.get(i + 1).x + 1) + " " + (pairs.get(i + 1).y + 1) + " ");
            }
        }
    }
}
