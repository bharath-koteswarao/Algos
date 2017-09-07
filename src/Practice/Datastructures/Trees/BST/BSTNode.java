package Datastructures.Trees.BST;

/**
 * Created by BK on 07-09-2017.
 */
public class BSTNode {
    int data;
    BSTNode left;
    BSTNode right;

    public BSTNode(int data, BSTNode left, BSTNode right) {
        this.left = left;
        this.data = data;
        this.right = right;
    }
}
