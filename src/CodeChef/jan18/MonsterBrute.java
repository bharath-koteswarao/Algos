package CodeChef.jan18;

/*
 * Created by bk on 11-01-2018 22:43
 */

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class MonsterBrute {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int alive = n;
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            List<Integer> list = new ArrayList<>();
            build(Integer.toBinaryString(x), 0, list, "");
            for (int i : list) {
                if (i < n && arr[i] > 0) {
                    arr[i] -= y;
                    if (arr[i] <= 0) alive -= 1;
                }
            }
            System.out.println(alive);
        }
    }

    private static void build(String s, int i, List<Integer> list, String ans) {
        if (i != s.length()) {
            if (s.charAt(i) == '1') {
                build(s, i + 1, list, ans + '1');
                build(s, i + 1, list, ans + '0');
            } else {
                build(s, i + 1, list, ans + '0');
            }
        } else {
            list.add(Integer.parseInt(ans, 2));
        }
    }
}
