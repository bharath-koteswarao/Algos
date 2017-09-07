package Datastructures.Trees.BST;

import java.util.Scanner;

/**
 * Created by BK on 07-09-2017.
 */
public class BSTSearch {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BST tree = new BST();
        tree.constructBST(4, 9, 2, 16, 3, 1, 7, 6, 8);
        BSTNode root = tree.getRoot();
        boolean isFound = searchForThisNode(sc.nextInt(), root);
        System.out.println(isFound ? "Found" : "This node doesn't exist");
    }

    private static boolean searchForThisNode(int data, BSTNode root) {
        if (root == null) return false;
        else {
            if (root.data == data) return true;
            else {
                System.out.println(root.data);
                return searchForThisNode(data, data > root.data ? root.right : root.left);
            }
        }
    }
}
