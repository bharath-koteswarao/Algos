package Hackerrank;

import java.util.HashMap;
import java.util.Scanner;

/**
 * Created by BK on 02-09-2017.
 */
public class BeautifulArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int j = 0; j < tc; j++) {
            int n = sc.nextInt();
            long[] input = new long[n];
            for (int i = 0; i < n; i++) {
                input[i] = sc.nextLong();
            }
            boolean isBeautiful = checkAscending(input) && checkUnique(input) && checkRange(input);
            System.out.println(isBeautiful ? "Beautiful" : "Ugly");
        }
    }

    private static boolean checkAscending(long[] input) {
        int count = 0;
        for (int i = 0; i < input.length - 1; i++) {
            if (input[i + 1] > input[i]) count++;
        }
        return !(count == input.length - 1);
    }

    private static boolean checkUnique(long[] input) {
        HashMap<Long, Integer> map = new HashMap<>();
        for (int i = 0; i < input.length; i++) {
            if (map.get(input[i]) == null) {
                map.put(input[i], 0);
            } else {
                return false;
            }
        }
        return true;
    }

    private static boolean checkRange(long[] input) {
        int n = input.length;
        for (int i = 0; i < n; i++) {
            if (input[i] > n) return false;
        }
        return true;
    }
}
