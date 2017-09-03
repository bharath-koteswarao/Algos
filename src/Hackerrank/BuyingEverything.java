package Hackerrank;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.TreeSet;

/**
 * Created by BK on 02-09-2017.
 */
public class BuyingEverything {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt(), k = sc.nextInt(), onesCount = 0;
        int rightMost = 0;
        List<Integer> ones = new ArrayList<>();
        int[] buildings = new int[n];
        for (int i = 0; i < n; i++) {
            buildings[i] = sc.nextInt();
            onesCount = buildings[i] == 1 ? onesCount + 1 : onesCount;
            if (buildings[i] == 1) ones.add(i);
        }
        if (onesCount < m) {
            System.out.println(-1);
        } else {
            if (ones.size() == 1) {
                System.out.println(ones.get(0));
            } else {
                int proceed = ones.size() - m + 1;
                TreeSet<Integer> ts = new TreeSet<>();
                for (int i = 0; i < proceed; i++) {
                    int total = ones.get(i), count = 1;
                    for (int j = i + 1; j < i + 4; j++) {
                        total += (ones.get(j) - ones.get(j - 1)) * k * count;
                        count++;
                    }
                    ts.add(total);
                }
                System.out.println(ts);
            }
        }
    }
}
