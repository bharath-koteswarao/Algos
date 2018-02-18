package Hackerrank.RookieRank4;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import static java.lang.Math.max;

/*
 * Created by bk on 18-02-2018 19:36
 */
class Node {
    int key;
    int height = 0;
    Node left = null;
    Node right = null;

    Node(int key) {
        this.key = key;
    }
}

public class C {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            if (!list.contains(x)) list.add(x);
        }
        Node root = new Node(list.get(0));
        for (int i = 1; i < list.size(); i++) {
            Node temp = root;
            insert(new Node(list.get(i)), temp);
        }
        int h = getHeight(root);
        System.out.println(h);
        int ih = getIH(root);
        System.out.println(ih);
    }

    private static int getIH(Node node) {
        if (node == null) return 0;
        else return node.height + getIH(node.right) + getIH(node.left);
    }

    private static int getHeight(Node node) {
        if (node.left == null && node.right == null) {
            node.height = 0;
            return 0;
        } else if (node.left == null) {
            node.height = 1 + getHeight(node.right);
            return node.height;
        } else if (node.right == null) {
            node.height = 1 + getHeight(node.left);
            return node.height;
        } else {
            node.height = max(1 + getHeight(node.left), 1 + getHeight(node.right));
            return node.height;
        }
    }

    private static void insert(Node node, Node root) {
        Node parent = null;
        while (root != null) {
            if (node.key > root.key) {
                parent = root;
                root = root.right;
            } else {
                parent = root;
                root = root.left;
            }
        }
        if (node.key > parent.key) parent.right = node;
        else parent.left = node;
    }
}
