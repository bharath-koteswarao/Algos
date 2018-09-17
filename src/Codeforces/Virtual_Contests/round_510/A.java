package Codeforces.Virtual_Contests.round_510;

import java.util.PriorityQueue;
import java.util.Scanner;

/**
 * Created by bk on 17-09-2018.
 */
public class A {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        int ma = Integer.MIN_VALUE;
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            ma = Math.max(ma, arr[i]);
        }
        for (int x : arr) heap.add(x);
        ma += m;
        while (m > 0) {
            int cur = heap.poll();
            heap.add(cur + 1);
            m -= 1;
        }
        int min = Integer.MIN_VALUE;
        while (!heap.isEmpty()) min = Math.max(min, heap.poll());
        System.out.println(min + " " + ma);
    }
}
