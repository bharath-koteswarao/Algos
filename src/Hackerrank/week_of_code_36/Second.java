package Hackerrank.week_of_code_36;

/*
 * Created by bk on 06-02-2018 12:55
 */

import java.util.Scanner;

public class Second {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        int min = 0, max = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            max += arr[i] == 1 ? 1 : 0;
        }
        for (int i = 0; i < n - 1; i++) {
            if (arr[i] == 1) {
                if (arr[i + 1] == 1) arr[i + 1] = 0;
                arr[i] = 0;
                min += 1;
            }
        }
        if (arr[n - 1] == 1) min += 1;
        System.out.println(max + " " + min);
    }
}
