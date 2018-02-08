package Codeforces.round_460;

/*
 * Created by bk on 07-02-2018 15:47
 */

import java.util.Scanner;

public class Second {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int num = 1;
        while (n > 0) {
            int sum = getSum(num);
            if (sum == 10) n -= 1;
            num += 1;
        }
        System.out.println(num - 1);
    }

    private static int getSum(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num = num / 10;
        }
        return sum;
    }
}
