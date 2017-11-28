package Datastructures.SegmentTree;

/*
 * Created by bk on 28-11-2017 15:44
 */

public class SegmentTree {
    public int size;
    public SegmentTree(int[] array) {
        this.size = array.length;
        Node[] tree = new Node[size];
    }
}
