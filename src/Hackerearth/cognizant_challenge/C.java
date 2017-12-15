package Hackerearth.cognizant_challenge;

/*
 * Created by bk on 15-12-2017 21:23
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

import static java.lang.Math.abs;

public class C {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int n = sc.nextInt();
            int[] inp = new int[n];
            for (int i = 0; i < n; i++) {
                inp[i] = sc.nextInt();
            }
            List<Integer> list = new ArrayList<>();
            int ans = 0;
            for (int i = 0; i < inp.length; i++) {
                int pos = abs(Collections.binarySearch(list, inp[i])) - 1;
                if (pos == 0) {
                    list.add(0, inp[i]);
                    ans -= 1;
                } else {
                    ans += list.get(pos - 1);
                    list.add(pos, inp[i]);
                }
            }
            System.out.println(ans);
        }
    }
}
