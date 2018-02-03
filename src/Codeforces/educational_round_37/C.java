package Codeforces.educational_round_37;

/*
 * Created by bk on 04-02-2018 00:05
 */

import java.util.Arrays;
import java.util.Scanner;

public class C {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        String valid = sc.next();
        int[] l = new int[n];
        for (int i = 0; i < n - 1; i++) l[i] = valid.charAt(i) == '1' ? 1 : 0;
        int i = 0;
        while (i < n - 1) {
//            System.out.println(Arrays.toString(arr));
            if (l[i] == 1) {
                int start = i;
                while (l[i] == 1 && i < n - 1) i += 1;
                Arrays.sort(arr, start, i + 1);
            } else i += 1;
        }
        boolean correct = true;
        for (i = 0; i < n; i++) {
            if (arr[i] != i + 1) correct = false;
            if (!correct) break;
        }
        System.out.println(correct ? "YES" : "NO");
    }
}
