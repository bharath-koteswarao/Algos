package Algorithms.Implementation;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

class Point implements Comparable {
    int x, y;
    double slope;

    public Point(int x, int y, double slope) {
        this.x = x;
        this.y = y;
        this.slope = slope;
    }

    @Override
    public String toString() {
        return "(" + this.x + ", " + this.y + ", " + this.slope + ")";
    }

    @Override
    public int compareTo(Object o) {
        Point p = (Point) o;
        /*
         * Complete this here
         */
        return 0;
    }
}

public class QueensAttack2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        int obs = sc.nextInt();
        double queen_x = sc.nextDouble(), queen_y = sc.nextDouble();
        List<Point> horPoints = new ArrayList<>();
        List<Point> verPoints = new ArrayList<>();
        List<Point> pdiagPoints = new ArrayList<>();
        List<Point> ndiagPoints = new ArrayList<>();
        for (int i = 0; i < obs; i++) {
            double x = sc.nextDouble();
            double y = sc.nextDouble();
            double num = queen_y - y;
            double den = queen_x - x;
            if (num == 0) {
                horPoints.add(new Point((int) (queen_x - x), (int) (queen_y - y), 0));
            } else if (den == 0) {
                verPoints.add(new Point((int) (queen_x - x), (int) (queen_y - y), Double.NaN));
            } else if (num / den == 1 || num / den == -1) {
                if (num / den == 1) {
                    pdiagPoints.add(new Point((int) (queen_x - x), (int) (queen_y - y), 1));
                } else {
                    ndiagPoints.add(new Point((int) (queen_x - x), (int) (queen_y - y), -1));
                }
            }
        }
        Collections.sort(horPoints);
        Collections.sort(verPoints);
        Collections.sort(pdiagPoints);
        Collections.sort(ndiagPoints);
        System.out.println(horPoints);
        System.out.println(verPoints);
        System.out.println(pdiagPoints);
        System.out.println(ndiagPoints);
    }
}
