package Algorithms.Searching;

import Datastructures.bk;

import java.util.Scanner;
import java.util.TreeSet;

/**
 * Created by BK on 10-10-2017.
 */
public class HackerlandTransmitters {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), k = sc.nextInt();
        TreeSet<Integer> ts = new TreeSet<>();
        for (int i = 0; i < n; i += 1) {
            ts.add(sc.nextInt());
        }
        int[] inp = new int[ts.size()];
        n = ts.size();
        while (ts.size() > 0) {
            inp[--n] = ts.pollLast();
        }
        int uncovered = inp.length;
        int transmitter_count = 0;
        while (uncovered > 0) {

        }
    }
}
