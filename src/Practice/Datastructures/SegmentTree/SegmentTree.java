package Datastructures.SegmentTree;

/*
 * Created by bk on 09-12-2017 15:54
 */

import static java.lang.Math.floorDiv;

public class SegmentTree {
    private static Node[] tree;
    private static int[] arr;

    public static void main(String[] __) {
        arr = new int[]{1, 2, 3, 4, 5, 6, 7};
        int n = arr.length;
        tree = new Node[(2 * n) - 1];
        for (int i = 0; i < tree.length; i++) tree[i] = new Node();
        build(0, n - 1, 0);
        print(tree);
        update(0, n - 1, 0, 6, 1);
        print(tree);
    }

    private static void print(Node[] tree) {
        for (Node node : tree) {
            System.out.print(node.data + " ");
        }
        System.out.println();
    }

    private static void build(int start, int end, int node) {
        if (start == end) {
            tree[node].data = arr[start];
        } else {
            int mid = floorDiv(start + end, 2);
            build(start, mid, (2 * node) + 1);
            build(mid + 1, end, (2 * node) + 2);
            tree[node].data = tree[(2 * node) + 1].data + tree[(2 * node) + 2].data;
        }
    }

    private static void update(int start, int end, int node, int zeroBasedIndex, int diff) {
        if (start == end) {
            tree[node].data += diff;
        } else {
            tree[node].data += diff;
            int mid = floorDiv(start + end, 2);
            if (zeroBasedIndex <= mid) update(start, mid, (2 * node) + 1, zeroBasedIndex, diff);
            else update(mid + 1, end, (2 * node) + 2, zeroBasedIndex, diff);
        }
    }
}
