package Algorithms.Implementation;

import Datastructures.bk;

import java.util.Arrays;
import java.util.Scanner;

public class LarrysArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int size = sc.nextInt();
            int[] inp = new int[size];
            for (int i = 0; i < size; i++) {
                inp[i] = sc.nextInt();
            }
            if (size == 3) {
                boolean res = check(0, 2, inp);
                System.out.println(res ? "YES" : "NO");
            } else {
                for (int i = 0; i < size - 3; i++) {
                    if (inp[i + 3] > inp[i + 2]) {
                        boolean res = check(i, i + 3, inp);
                        bk.print_int(inp);
                    }
                }
                int[] copy = inp;
                boolean valid = true;
                Arrays.sort(copy);
                for (int i=0;i<size;i++) {
                    if (copy[i] != inp[i]) {
                        valid = false;
                        break;
                    }
                }
                System.out.println(valid?"YES":"NO");
            }
        }
    }

    private static boolean check(int start, int end, int[] inp) {
        int mid = start + 1;
        if (inp[end] <= inp[start] && inp[start] <= inp[mid]) {
            int temp1 = inp[start], temp2 = inp[mid], temp3 = inp[end];
            inp[start] = temp3;
            inp[mid] = temp1;
            inp[end] = temp2;
            return true;
        } else if (inp[mid] <= inp[end] && inp[end] <= inp[start]) {
            int temp1 = inp[start], temp2 = inp[mid], temp3 = inp[end];
            inp[start] = temp2;
            inp[mid] = temp3;
            inp[end] = temp1;
            return true;
        }
        return false;
    }
}
