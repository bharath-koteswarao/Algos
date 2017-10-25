package Algorithms.Searching.CodeChef;

import java.util.Arrays;
import java.util.Scanner;

public class SnakeEating {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int ti = 0; ti < tc; ti++) {
            int size = sc.nextInt(), queries = sc.nextInt();
            int[] temp = new int[size];
            for (int i = 0; i < size; i++) {
                temp[i] = sc.nextInt();
            }
            Arrays.sort(temp);
            int[] inp = new int[size];
            for (int i = 0; i < temp.length; i++) {
                inp[size - i - 1] = temp[i];
            }
            for (int q = 0; q < queries; q++) {
                int query = sc.nextInt();
                int count = 0;
                for (int i = 0; i < size; i++) {
                    if (inp[i] >= query) {
                        count += 1;
                    } else {
                        int sum = inp[i];
                        i += 1;
                        while (sum < query && i < size) {
                            sum += 1;
                            i += 1;
                        }
                        if (sum >= query) {
                            count += 1;
                        }
                    }
                }
                System.out.println(count);
            }
        }
    }
}
