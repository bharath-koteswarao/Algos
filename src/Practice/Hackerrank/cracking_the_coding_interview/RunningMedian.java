package Hackerrank.cracking_the_coding_interview;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

import static java.lang.Math.*;

/**
 * Created by bk on 25-06-2018.
 */
public class RunningMedian {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        ArrayList<Long> cont = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            long nu = sc.nextLong();
            int idx = Collections.binarySearch(cont, nu);
            idx = idx < 0 ? abs(idx) - 1 : idx;
            cont.add(idx, nu);
            if (i % 2 == 0) {
                System.out.println(String.format("%.1f", (float) cont.get(floorDiv(i, 2))));
            } else {
                int cei = (int) ceil((float) i / 2);
                int flr = (int) floor((float) i / 2);
                long ce = cont.get(cei);
                long fl = cont.get(flr);
                float ans = (float) (ce + fl) / 2;
                System.out.println(String.format("%.1f", ans));
            }
        }
    }
}
