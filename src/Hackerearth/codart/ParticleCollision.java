package Hackerearth.codart;

/*
 * Created by bk on 10-02-2018 15:26
 */

import java.util.Scanner;

import static java.lang.Math.floorDiv;

public class ParticleCollision {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int n = sc.nextInt();
            long ans = 0;
            long total = floorDiv(n * (n + 1), 2);
            long s = 1;
            for (int i = 1; i < n; i++) {
                ans += i * (total - s);
                s += (i + 1);
            }
            System.out.println(ans);
        }
    }
}
