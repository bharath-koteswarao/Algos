package CodeChef.feb18;

/*
 * Created by bk on 05-02-2018 23:35
 */

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import static java.lang.Math.floorDiv;

class Point {
    public long x, y;

    public Point(long x, long y) {
        this.x = x;
        this.y = y;
    }
}

public class Poinpoly {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int req = floorDiv(n, 10);
        List<Point> points = new ArrayList<>();
        List<Point> answers = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            points.add(new Point(sc.nextLong(), sc.nextLong()));
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < i + n - 1; j++) {
                long x1 = points.get(i).x, y1 = points.get(i).y;
                long x2 = points.get(i).x, y2 = points.get(i).y;
                long num = y2 - y1, den = x2 - x1;
                long gc = gcd(num, den);
                num = floorDiv(num, gc);
                den = floorDiv(den, gc);
            }
        }
    }

    private static long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
