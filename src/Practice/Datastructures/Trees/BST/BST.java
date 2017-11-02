package Datastructures.Trees.BST;


/**
 * Created by BK on 07-09-2017.
 */
public class BST {
    private BSTNode root;

    public void constructBST(int... args) {
        for (int i : args) {
            if (root == null) {
                // BST is empty initially
                root = new BSTNode(i, null, null);
            } else {
                // Root is not null so construct the tree here
                BSTNode travellingNode = root;
                BSTNode parent = null;
                while (travellingNode != null) {
                    parent = travellingNode;
                    if (i > travellingNode.data) travellingNode = travellingNode.right;
                    else travellingNode = travellingNode.left;
                }
                if (i> parent.data)parent.right = new BSTNode(i,null,null);
                else parent.left = new BSTNode(i,null,null);
            }
        }
    }

    public BSTNode getRoot() {
        return root;
    }
}
