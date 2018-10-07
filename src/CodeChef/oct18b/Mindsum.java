//package CodeChef.oct18b;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

/**
 * Created by bk on 07-10-2018.
 */
class Mindsum {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            long n = sc.nextLong(), d = sc.nextLong();
            System.out.println(calc(n, d));
        }
    }

    private static String calc(long n, long d) {
        int count = 100000;
        long ans = 11, steps = Long.MAX_VALUE;
        HashMap<Long, Integer> visited = new HashMap<>();
        List<Long> current = List.of(n);
        int level = 0;
        while (count-- > 0) {
            List<Long> next = new ArrayList<>();
            for (long x : current) {
                if (x < ans) {
                    ans = x;
                    steps = level;
                } else if (x == ans && level < steps) steps = level;
                if (!visited.containsKey(x + d)) {
                    visited.put(x + d, 1);
                    next.add(x + d);
                }
                long digS = digSum(x);
                if (!visited.containsKey(digS)) {
                    visited.put(digS, 1);
                    next.add(digS);
                }
            }
            level += 1;
            current = new ArrayList<>(next);
        }
        return ans + " " + steps;
    }

    private static long digSum(long n) {
        long ret = 0;
        while (n > 0) {
            ret += n % 10;
            n = n / 10;
        }
        return ret;
    }

}
