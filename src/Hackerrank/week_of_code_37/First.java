package Hackerrank.week_of_code_37;

import java.text.DecimalFormat;
import java.util.Scanner;

/**
 * Created by koteswarao on 16-04-2018.
 */
public class First {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        java.text.DecimalFormat df = new DecimalFormat("0.00");
        int n = sc.nextInt();
        int score = 0, count = 0;
        for (int i = 0; i < n; i++) {
            int temp = sc.nextInt();
            if (temp >= 90) {
                score += temp;
                count += 1;
            }
        }
        if (count == 0) {
            System.out.println("0.00");
        } else {
            System.out.println(df.format((float) score / (float) count));
        }
    }
}
