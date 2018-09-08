package Hackerrank.university_codesprint_5;

import java.util.Scanner;

public class limit_xor {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        Node root = new Node();
        insertToTrie(0, root);
        int pre = 0;
        long ans = 0;
        for (int i = 0; i < n; i++) {
            pre ^= a[i];
            ans += find(pre, k, root);
            insertToTrie(pre, root);
        }
        System.out.println(ans);
    }

    private static void insertToTrie(int p, Node root) {
        Node temp = root;
        for (int i = 31; i >= 0; i--) {
            int val = (p & (1 << i)) >= 1 ? 1 : 0;
            if (val == 1) {
                temp.right++;
                if (temp.arr[val] == null) temp.arr[val] = new Node();
                temp = temp.arr[val];
            } else {
                temp.left++;
                if (temp.arr[val] == null) temp.arr[val] = new Node();
                temp = temp.arr[val];
            }
        }
    }

    private static long find(int pre_xor, int k, Node root) {
        Node temp = root;
        long res = 0;
        for (int i = 31; i >= 0; i--) {
            int val1 = (pre_xor & (1 << i)) >= 1 ? 1 : 0;
            int val2 = (k & (1 << i)) >= 1 ? 1 : 0;
            if (val2 == 1) {
                if (val1 == 1) {
                    res += temp.right;
                    if (temp.arr[1 - val1] == null) return res;
                    temp = temp.arr[1 - val1];
                } else {
                    res += temp.left;
                    if (temp.arr[1 - val1] == null) return res;
                    temp = temp.arr[1 - val1];

                }
            } else {
                if (temp.arr[val1] == null) return res;
                temp = temp.arr[val1];
            }
        }
        return res;
    }

    static class Node {
        int value;
        int left;
        int right;
        Node[] arr = new Node[2];

        Node() {
            value = 0;
            left = 0;
            right = 0;
            arr[0] = null;
            arr[1] = null;
        }
    }
}
