package Codeforces.round_458_and_codecraft;

/*
 * Created by bk on 23-01-2018 22:17
 */

import java.util.Scanner;

import static java.lang.Math.floorDiv;


class Node {
    int gcd = 0;

    @Override
    public String toString() {
        return gcd + " ";
    }
}

public class D_Problem {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Node[] segTree = new Node[4 * n];
        for (int i = 0; i < segTree.length; i++) {
            segTree[i] = new Node();
        }
        build(segTree, arr, 0, n - 1, 0);
        for (Node node : segTree) System.out.println(n);
    }

    private static void build(Node[] segTree, int[] arr, int start, int end, int node) {
        if (start == end) {
            segTree[node].gcd = arr[start];
        } else {
            int mid = floorDiv(start + end, 2);
            build(segTree, arr, start, mid, (2 * node) + 1);
            build(segTree, arr, mid + 1, end, (2 * node) + 2);
            segTree[node].gcd = segTree[2 * node + 1].gcd + segTree[2 * node + 2].gcd;
        }
    }
}
