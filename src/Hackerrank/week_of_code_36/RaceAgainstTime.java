package Hackerrank.week_of_code_36;

/*
 * Created by bk on 08-02-2018 19:11
 */

/*
4
5
2 6 2
2 3 2

7
3
2 6 7 1 2 3
1 -2 3 -4 5 1
 */

import java.util.Arrays;
import java.util.Scanner;

import static java.lang.Math.abs;

class Pair {
    int i, j;
    long val;

    Pair(int i, int j, long val) {
        this.i = i;
        this.j = j;
        this.val = val;
    }

    @Override
    public String toString() {
        return "(" + this.i + ", " + this.j + ", " + this.val + ")";
    }
}

class MinHeap {
    private static final int FRONT = 1;
    private Pair[] Heap;
    private int size;
    private int maxsize;

    public MinHeap(int maxsize) {
        this.maxsize = maxsize;
        this.size = 0;
        Heap = new Pair[this.maxsize + 1];
        Heap[0] = new Pair(0, 0, 0);
        Heap[0].val = Integer.MIN_VALUE;
    }

    private int parent(int pos) {
        return pos / 2;
    }

    private int leftChild(int pos) {
        return (2 * pos);
    }

    private int rightChild(int pos) {
        return (2 * pos) + 1;
    }

    private boolean isLeaf(int pos) {
        return pos >= (size / 2) && pos <= size;
    }

    private void swap(int fpos, int spos) {
        long tmp;
        tmp = Heap[fpos].val;
        Heap[fpos] = Heap[spos];
        Heap[spos].val = tmp;
    }

    private void minHeapify(int pos) {
        if (!isLeaf(pos)) {
            if (Heap[pos].val > Heap[leftChild(pos)].val || Heap[pos].val > Heap[rightChild(pos)].val) {
                if (Heap[leftChild(pos)].val < Heap[rightChild(pos)].val) {
                    swap(pos, leftChild(pos));
                    minHeapify(leftChild(pos));
                } else {
                    swap(pos, rightChild(pos));
                    minHeapify(rightChild(pos));
                }
            }
        }
    }

    public void insert(Pair element) {
        Heap[++size] = new Pair(element.i, element.j, element.val);
        int current = size;

        while (Heap[current].val < Heap[parent(current)].val) {
            swap(current, parent(current));
            current = parent(current);
        }
    }

    public void print() {
        for (int i = 1; i <= size / 2; i++) {
            System.out.print(" PARENT : " + Heap[i] + " LEFT CHILD : " + Heap[2 * i]
                    + " RIGHT CHILD :" + Heap[2 * i + 1]);
            System.out.println();
        }
    }

    public void minHeap() {
        for (int pos = (size / 2); pos >= 1; pos--) {
            minHeapify(pos);
        }
    }

    public Pair remove() {
        if (size == 0) return null;
        Pair popped = Heap[FRONT];
        Heap[FRONT] = Heap[size--];
        minHeapify(FRONT);
        return popped;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    @Override
    public String toString() {
        return Arrays.toString(this.Heap);
    }
}

public class RaceAgainstTime {
    static long[][] minValue;
    static long[][] movingCost;

    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] heights = new long[n + 1];
        long[] prices = new long[n + 1];
        heights[0] = sc.nextInt();
        prices[0] = 0;
        for (int i = 1; i < n; i++) heights[i] = sc.nextInt();
        for (int i = 1; i < n; i++) prices[i] = sc.nextInt();
        movingCost = new long[n + 1][n + 1];
        for (long[] arr : movingCost) Arrays.fill(arr, -1);
        for (int i = 0; i < n + 1; i++) {
            boolean breakNext = false;
            for (int j = i + 1; j < n + 1; j++) {
                if (breakNext) break;
                else {
                    if (heights[j] > heights[i]) breakNext = true;
                    long cost = (j == n ? (Long.MAX_VALUE - Integer.MAX_VALUE) : abs(heights[i] - heights[j])) + prices[j];
                    movingCost[i][j] = cost;
                }
            }
        }
//        for (long[] arr : movingCost) System.out.println(Arrays.toString(arr));
        boolean[][] fixedPath = new boolean[n + 1][n + 1];
        minValue = new long[n + 1][n + 1];
        for (long[] arr : minValue) Arrays.fill(arr, Long.MAX_VALUE - Integer.MAX_VALUE);
        minValue[0][0] = 0;
        MinHeap mh = new MinHeap((n + 1) * (n + 1));
        for (int i = 0; i < n + 1; i++) {
            for (int j = i + 1; j < n + 1; j++) {
                if (movingCost[i][j] != -1) mh.insert(new Pair(i, j, movingCost[i][j]));
            }
        }
        System.out.println(mh);
        mh.insert(new Pair(0, 0, 0));
        Pair cur = mh.remove();
        System.out.println(mh);
//        while (cur != null) {
//            int x = cur.i, y = cur.j;
//            while (movingCost[x][y] != -1 && y < n) {
//                if (!fixedPath[x][y]) relax(cur, x, y);
//                y += 1;
//            }
//            fixedPath[cur.i][cur.j] = true;
//            cur = mh.remove();
//        }
//        for (int i = 0; i < n; i++) {
//            minValue[i][n] -= (Long.MAX_VALUE - Integer.MAX_VALUE);
//        }
//        for (long[] arr : minValue) System.out.println(Arrays.toString(arr));
    }

    private static void relax(Pair cur, int x, int y) {
        minValue[x][y] = Math.min(minValue[x][y], minValue[cur.i][cur.j] + movingCost[x][y]);
        System.out.println(cur + " " + minValue[x][y] + " " + minValue[cur.i][cur.j] + " " + movingCost[x][y]);
    }
}
