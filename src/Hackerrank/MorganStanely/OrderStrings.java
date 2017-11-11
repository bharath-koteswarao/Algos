package Hackerrank.MorganStanely;


import java.util.Scanner;

class Pair implements Comparable {
    int num = 0, weight = 0;

    Pair(int num, int weight) {
        this.num = num;
        this.weight = weight;
    }

    @Override
    public int compareTo(Object o) {
        if (this.num != ((Pair) o).num) return Math.min(this.num, ((Pair) o).num);
        else {
            if (this.weight > ((Pair) o).weight) {
                return this.num;
            } else {
                return ((Pair) o).num;
            }
        }
    }
}

public class OrderStrings {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {

        }
    }
}
