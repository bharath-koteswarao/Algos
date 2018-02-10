package Hackerearth.codart;

/*
 * Created by bk on 10-02-2018 15:47
 */

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class PlayWithNumbers {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), q = sc.nextInt();
        int[] arr = new int[q];
        for (int i = 0; i < q; i++) {
            arr[i] = sc.nextInt();
        }
        List<Integer> combs = new ArrayList<>();
        for (int i = 1; i < Math.pow(2, q); i++) {
            String str = Integer.toBinaryString(i);
        }
    }
}
