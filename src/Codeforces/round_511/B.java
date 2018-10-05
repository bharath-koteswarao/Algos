package Codeforces.round_511;

import java.util.Scanner;

/**
 * Created by bk on 22-09-2018.
 */
public class B {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int ans = 0;
        double max = 0;
        for (int i = 0; i < n; i++) {
            int a = sc.nextInt(), b = sc.nextInt();
            if (Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2)) > max) {
                max = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));
                ans = a + b;
            }
        }
        System.out.println(ans);
    }
}
