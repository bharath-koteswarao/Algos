package Hackerearth.paypal_challenge;

import java.util.Scanner;

/**
 * Created by bk on 01-06-2018.
 */
public class First {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            String inp = sc.next();
            String pal = inp + (new StringBuffer(inp)).reverse().toString();
            int[] counter = new int[10];
            for (int i = 0; i < pal.length(); i++) counter[inte(pal.charAt(i))] += 1;
            int ans = 0, max = 0;
            for (int i = 0; i < 10; i++) {
                if (counter[i] > max) {
                    ans = i;
                    max = counter[i];
                } else if (counter[i] == max) ans = Math.min(ans, i);
            }
            System.out.println(ans);
        }
    }

    private static int inte(char c) {
        return Integer.parseInt(c + "");
    }
}
