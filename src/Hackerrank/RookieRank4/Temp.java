package Hackerrank.RookieRank4;

/*
 * Created by bk on 18-02-2018 15:10
 */

import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

public class Temp {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        Stack<Integer> st = new Stack<>();
        int[] x = new int[n];
        x[0] = -1;
        st.push(0);
        for (int i = 1; i < n; i++) {
            int cur = arr[i];
            if (cur < arr[st.peek()]) {
                x[i] = st.peek();
                while (!st.isEmpty()) x[st.pop()] = -1;
                st.push(i);
            }
        }
        while (!st.isEmpty()) x[st.pop()] = -1;
        System.out.println(Arrays.toString(x));
    }
}
