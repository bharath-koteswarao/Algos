package Algorithms.Searching.CodeChef;

import Datastructures.bk;

import java.util.Arrays;
import java.util.Scanner;


public class SnakeEating {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int ti = 0; ti < tc; ti++) {
            int size = sc.nextInt(), queries = sc.nextInt();
            double[] inp = new double[size];
            for (int i = 0; i < size; i++) {
                inp[i] = sc.nextInt();
            }
            double prefixSum[] = new double[size];
            Arrays.sort(inp);
            prefixSum[0] = inp[0];
            for (int i = 1; i < size; i++) {
                prefixSum[i] += prefixSum[i - 1] + inp[i];
            }
            bk.print_double(inp);
            for (int i = 0; i < queries; i++) {
                int count = 0;
                int query = sc.nextInt();
                int anchorEnd = binarySearch(0, inp.length - 1, inp, query - 0.5);
                count += inp.length - 1 - anchorEnd;
                if (count == inp.length - 1) {
                    System.out.println(count);
                } else {
                    int len = anchorEnd;
                    int x = getOptimalX(prefixSum, len, query);
                    System.out.println(inp.length-1-x);
                }
            }
        }
    }

    private static int getOptimalX(double[] prefixSum, int len, int req) {
        int x = len / 2;
        while (true) {
            if (x > req * (len - x) - sum(prefixSum, len - x + 1, len)) {
                x += x / 2;
                if (x == len) return x;
            } else if (x == req * (len - x) - sum(prefixSum, len - x + 1, len)) {
                return x;
            } else {
                x -= x / 2;
                if (x == 0) return x;
            }
        }
    }

    private static double sum(double[] prefixSum, int start, int end) {
        return start == 0 ? prefixSum[end] : prefixSum[end] - prefixSum[start - 1];
    }

    private static int binarySearch(int start, int end, double[] arr, double ele) {
        if (start >= end) {
            return start;
        } else {
            int mid = start + (end - start) / 2;
            if (arr[mid] > ele) {
                return binarySearch(start, mid - 1, arr, ele);
            } else {
                return binarySearch(mid + 1, end, arr, ele);
            }
        }
    }
}
