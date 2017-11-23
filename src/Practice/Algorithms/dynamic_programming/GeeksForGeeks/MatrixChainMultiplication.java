package Algorithms.dynamic_programming.GeeksForGeeks;

/*
 * Created by bk on 22-11-2017 21:13
 */

import java.util.ArrayList;
import java.util.Hashtable;
import java.util.List;
import java.util.Scanner;

class Pair {
    public int left = 0, right = 0;

    Pair(int left, int right) {
        this.left = left;
        this.right = right;
    }

    @Override
    public String toString() {
        return "(" + this.left + ", " + this.right + ")";
    }
}

public class MatrixChainMultiplication {
    static int[] inp;
    static List<Integer> answers;
    static Hashtable<String, Integer> memo;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        memo = new Hashtable<>();
        int tc = sc.nextInt();
        while (tc-- > 0) {
            answers = new ArrayList<>();
            inp = new int[sc.nextInt()];
            for (int i = 0; i < inp.length; i++) {
                inp[i] = sc.nextInt();
            }
            List<Pair> list = new ArrayList<>();
            for (int i = 0; i < inp.length - 1; i++) {
                list.add(new Pair(inp[i], inp[i + 1]));
            }
            evaluate(list, 0);
            int min = Integer.MAX_VALUE;
            for (int i : answers) {
                min = Math.min(min, i);
            }
            System.out.println(min);
        }
    }

    private static int evaluate(List<Pair> list, int sum) {
//        System.out.println(list + " " + sum);
        List<Pair> temp = new ArrayList<>(list);
        for (int i = 0; i < temp.size() - 1; i += 1) {
            if (!memo.containsKey(temp.toString())) {
                int cur = evaluate(getMerged(temp, i, i + 1), sum + (temp.get(i).left * temp.get(i).right * temp.get(i + 1).right));
                memo.put(temp.toString(), cur);
            }
        }
        if (temp.size() == 1) answers.add(sum);
        return sum;
    }

    private static List<Pair> getMerged(List<Pair> lis, int i, int j) {
        Pair p = new Pair(lis.get(i).left, lis.get(j).right);
        List<Pair> copy = new ArrayList<>(lis);
        copy.remove(j);
        copy.remove(i);
        copy.add(i, p);
        return copy;
    }
}
